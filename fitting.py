# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 23:51:08 2024

@author: aurom
"""
import numpy as np
from astropy.utils.data import download_file
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from astropy.table import Table
import os
from astropy.visualization import quantity_support
from specutils import Spectrum1D
from astropy import units as u
quantity_support() 
import warnings
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from scipy.ndimage import gaussian_filter1d
from scipy.signal import fftconvolve
import astropy.constants as const

# Here we read in a FITS table
path="C:\\Users\\aurom\\OneDrive\\Escritorio\\IndStudyProject\\"
os.chdir(path)

filename = 'abell2744-ddt-v1_prism-clear_2756_110003.spec.fits' #Remember to write fits
hdu_list = fits.open(filename, memmap=True)
evt_data = Table(hdu_list[1].data)


flux=evt_data["flux"]#* u.Unit('erg cm-2 s-1 AA-1') 
zobj=5.66
c= 2.99792e10
#from voigt import spectrum_n


wave=evt_data["wave"]#* u.AA 

flux1=(flux*c*(1e-29))/(wave)**2 #change to ffrec to flambda
errors=(evt_data["err"]*c*(1e-29))/(wave)**2 

#Fit of continuum
spec = Spectrum1D(flux=flux1* u.Unit('erg cm-2 s-1 AA-1'), spectral_axis=wave* u.um  ) 
spec2 = Spectrum1D(flux=errors* u.Unit('erg cm-2 s-1 AA-1'), spectral_axis=wave* u.um  ) 
nt=np.where((1.07<wave) & (wave<2)|(1.5<wave) & (wave<2.4)|(2.4<wave) & (wave<3.1)|(3.4<wave) & (wave<4.2)
|(4.5<wave) & (wave<6))
#plt.plot(wave,flux1)
#plt.show()
c1 = np.polyfit(wave[nt],flux1[nt], 8)
facF = np.poly1d(c1)(wave)

#Normalize spectrum with continuum
shift=100#110

cont_norm_spec = spec / facF
errorn=spec2/facF    
wavef=(cont_norm_spec.spectral_axis.to_value()*1e4)+shift
# Gauss function for lines
def gauss(x, a, x0, sigma, b,c):
    return a * np.exp(-(x - x0)**2 / (2 * sigma**2))+(b*x+c)


# Data
x = wave
y = flux1#


# Restrictions
x_restricted1 = x[(x >= 2.) & (x <= 2.8)]
y_restricted1 = y[(x >= 2.) & (x <= 2.8)]

x_restricted2 = x[(x >= 3.) & (x <= 3.8)]
y_restricted2 = y[(x >= 3.) & (x <= 3.8)]

x_restricted = x[(x >= 4.2) & (x <= 4.7)]
y_restricted = y[(x >= 4.2) & (x <= 4.7)]

x_restricted3 = x[(x >= 3.1) & (x <= 5.32)]
y_restricted3 = y[(x >= 3.1) & (x <= 5.32)]


# Gaussian fit with initial guess
if_alpha=2.42e-19
if_OII=1.6e-19
if_OIII=3e-19
iw_alpha=0.01
b = 0.1e-22
c = 0.1e-21

popt, pcov = curve_fit(gauss, x_restricted, y_restricted, p0=[if_alpha, 4.38, iw_alpha,b,c])#HALPHA
popt1, pcov1 = curve_fit(gauss, x_restricted1, y_restricted1, p0=[if_OII, 2.48, iw_alpha,b,c])#0II
popt2, pcov2 = curve_fit(gauss, x_restricted2, y_restricted2, p0=[if_OIII, 3.332, iw_alpha,b,c])#OIII
popt3, pcov3 = curve_fit(gauss, x_restricted3, y_restricted3, p0=[if_alpha/2.86, 3.24, iw_alpha,b,c])#HB

print(popt)

#Error
perr1 = np.sqrt(np.diag(pcov1))#Error in OIII
perr2 = np.sqrt(np.diag(pcov2))#Error in OII
#y1=list1[6][indices]
#mse=mean_squared_error(x1,y1)
#mae=mean_absolute_error(x1,y1) 

perr = np.sqrt(np.diag(pcov)) #Error in Halfa
perr3 = np.sqrt(np.diag(pcov3)) 
#r2 = r2_score(x1, y1)


#Adjust em lines   
y_fit = gauss(x, *popt)#list2[1,:] 
y_fit2 = gauss(x, *popt2)#+zerosl#+list2[1,:]
y_fit1 = gauss(x, *popt1)#list2[1,:]
y_fit3= gauss(x, *popt3)
#Gaussian filter


filter1=gaussian_filter1d(input=zerosl, sigma=3.8e-3)
#print(filter1[40:50])

#Error in voigt profile
indices = (wavef >= 8000) & (wavef <= 10000)
aflux=cont_norm_spec.flux.to_value()
sigma=errorn.flux.to_value()
chi_s=np.sum(((aflux[indices]-filter1[indices])**2)/(sigma[indices])**2)
dof=len(aflux[indices])-1
errorv=chi_s/dof
#print(errorv)

#Region
indices = (x >= 0.8) & (x <= 1)
#Apply region into profile
x1=cont_norm_spec.spectral_axis[indices]


#print(zerosl[40:50])
#FWHM Halfa
fwhm_ha=2.35*perr[0]
#print(fwhm_ha)

#Luminosity and SFR 
fline_ha=np.sqrt(2*np.pi)*popt[0]*popt[2]*1e4
fline_OIII=np.sqrt(2*np.pi)*popt2[0]*popt2[2]*1e4
fline_OII=np.sqrt(2*np.pi)*popt1[0]*popt1[2]*1e4
fline_hb=np.sqrt(2*np.pi)*popt3[0]*popt3[2]*1e4
dl=55101.7
D_L=dl*3.08568e24
L_ha=4*np.pi*(D_L**2)*fline_ha
L_OIII=4*np.pi*(D_L**2)*fline_OIII
L_OII=4*np.pi*(D_L**2)*fline_OII
L_hb=4*np.pi*(D_L**2)*fline_hb
SFR_ha= 7.9e-42*L_ha
print(L_ha,SFR_ha)
Lerr=perr[0]*4*np.pi*(D_L**2)

#For sigma NII
imin=zobj*0.6600+0.6600
imax=zobj*0.6700+0.6700
intervalo=np.where((x>=imin)&(x<=imax))
std1=np.std(y[intervalo])
sigma3=3*std1
fline_NII=np.sqrt(2*np.pi)*sigma3*popt[2]*1e4

print('sigma3:',fline_NII)

######################################################################################
### Graph data and the fit

#plt.figure(figsize=(8, 5))
plt.step(x,flux1,label="Spectrum z=5.66",linewidth=1)
plt.title('Emission line profile of: '+filename+"\n")
plt.plot(x[(x >= 2.4) & (x <= 2.6)], y_fit1[(x >= 2.4) & (x <= 2.6)], color="purple",linestyle="--", label=r'[OII] Gaussian profile')
plt.plot(x[(x >= 3.25) & (x <= 3.4)], y_fit2[(x >= 3.25) & (x <= 3.4)], 'deeppink',linestyle="--", label='[OIII]Gaussian profile')
plt.plot(x[(x >= 4.3) & (x <= 4.5)], y_fit[(x >= 4.3) & (x <= 4.5)], color="orangered",linestyle="--", label=r'H$\alpha$ Gaussian profile')
plt.plot(x[(x >= 3.2) & (x <= 3.34)], y_fit3[(x >= 3.2) & (x <= 3.34)], color="aqua",linestyle="--", label=r'H$\beta$ Gaussian profile')

plt.xlabel("$\lambda_{obs}$ [$\mu m $]")
plt.ylabel(r"$f_{\lambda} [erg ~ cm^{-2} s^{-1} \AA$]")
#plt.plot(x, y_fit3, color="turquoise",linestyle="--", label=r'H$\beta$ Gaussian profile')
plt.ylim(-0.05e-19,0.5e-19)
plt.xlim(2.1,4.8)
#plt.errorbar(cont_norm_spec.spectral_axis,cont_norm_sp3ec.flux,yerr=sigma,elinewidth=0.1,fmt="o",capsize=0.1,color='orchid')
plt.legend()
plt.savefig('2756_110003.png', dpi=300, bbox_inches='tight')
plt.show()

#plt.errorbar(cont_norm_spec.spectral_axis,cont_norm_sp3ec.flux,yerr=sigma,elinewidth=0.1,fmt="o",capsize=0.1,color='orchid')

#plt.plot(x_restricted1, y_restricted1*0.1e16, color='lightseagreen',linestyle="-")#label='Restricted data [OII]'
#plt.fill_betweenx(4,5, color='gray', alpha=0.3)
#plt.plot(x_restricted2, y_restricted2*0.1e16, color='lightseagreen',linestyle="-")#label='Restricted data [OIII]'
#plt.plot(x_restricted, y_restricted*0.1e16, color='lightseagreen',linestyle="-")# label=r'Restricted data H$\alpha$'
###############################################################
#Plot Lyman alfa break
lobs=zobj*0.1215 +0.1215
plt.axvline(lobs*1e4,color='lightpink',linestyle="-.",linewidth=1,label=r'Lyman $\alpha$ ')
plt.step(wavef,cont_norm_spec.flux,label="Spectrum z=5.66",linewidth=1,where='mid')
plt.errorbar(wavef,cont_norm_spec.flux.to_value(),yerr=errors/facF,linewidth=0.5,capsize=0.3,color='royalblue',ls='none')

plt.ylim(-1,2.8)
plt.xlim(7300,10000)
plt.title('Emission line profile of: '+filename+"\n")
plt.ylabel(r"Normalized $f_{\lambda}$")
plt.xlabel("$\lambda_{obs}$ [$\AA $]")

cd = N[10]
Nf = f"{cd:.3e}" 
#plt.plot(cont_norm_spec.spectral_axis,list2[14],label='Voigt profile',linestyle='--',color='green')
#plt.plot(cont_norm_spec.spectral_axis,zerosl,label='Voigt profile',linestyle='-.',color='red')
plt.plot(wavef,filter1,color="green",label='Voigt profile model\n$n_H=$'+str(Nf),linestyle='-')
#print(list2[14,:])
plt.legend()
plt.savefig('2756_110003v.png', dpi=300)
plt.show()

#plt.plot(cont_norm_spec.spectral_axis,facF)
#plt.show()


#Lines to check continuum fit
#plt.step(cont_norm_spec.spectral_axis,spec.flux,color='red')
#plt.plot(cont_norm_spec.spectral_axis,facF)
#plt.show()

#Print results
print("Results [OII]")
print(f"Amplitude : {popt1[0]:.2f} ± {perr1[0]:.4f}")
#Lines to check continuum fit
#plt.step(cont_norm_spec.spectral_axis,spec.flux,color='red')
print(f"Center (x0): {popt1[1]:.2f} ± {perr1[1]:.4f}")
print(f"Width (sigma): {popt1[2]:.2f} ± {perr1[2]:.4f}\n")

print("Results [OIII]")
print(f"Amplitude : {popt2[0]:.2f} ± {perr2[0]:.4f}")
print(f"Center (x0): {popt2[1]:.2f} ± {perr2[1]:.4f}")
print(f"Width (sigma): {popt2[2]:.2f} ± {perr2[2]:.4f}\n")

print(r"Results H$\alpha$")
print(f"Amplitude: {popt[0]:.2f} ± {perr[0]:.4f}")
print(f"Center(x0): {popt[1]:.2f} ± {perr[1]:.4f}")
print(f"Width(sigma): {popt[2]:.2f} ± {perr[2]:.4f}\n")


print('Error voigt profile:',errorv, "\n$\chi^2$:",chi_s)
print('Selected column density',N[10])

#print(cont_norm_spec)

#Save data
with open("Spectradata_1.txt", "w") as archivo:
    archivo.write("Name\tz\tFluxha\tErrorFluxha\tFluxOIII\tErrorFluxOIII\tFluxOII\tErrorFluxOII\tHbeta\tErrorFluxhb\tLumha\tLumerr\tSFRha\tColumden\tErrorVoigt\tsigma3\twha\tfline_NII\n")  # Encabezado con tabulaciones
    archivo.write(f"{filename}\t{zobj}\t{fline_ha}\t{perr[0]}\t{fline_OIII}\tf{perr2[0]}\t{fline_OII}\t{perr1[0]}\t{fline_hb}\t{perr3[0]}\t{L_ha}\t{Lerr}\t{SFR_ha}\t{N[10]}\t{errorv}\t{sigma3}\t{popt[2]}\t{fline_NII}")


    #archivo.write("Name\tz\tFluxha\tFluxOIII\tFluxOII\tLumha\tLumOIII\tLumOII\tSFRha\tColumden\t\n")  # Encabezado con tabulaciones
    #archivo.write(f"{filename}\t{zobj}\t{fline_ha}\t{fline_OIII}\t{fline_OII}\t{L_ha}\t{SFR_ha}\t{N[11]}")

