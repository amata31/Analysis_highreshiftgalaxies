# ==== VOIGT PROFILE ===============
import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt
import os
from astropy.io import fits
from astropy.table import Table

path="C:\\Users\\aurom\\OneDrive\\Escritorio\\IndStudyProject\\"
os.chdir(path)
# Here we read in a FITS table
filename = 'abell2744-ddt-v1_prism-clear_2756_110003.spec.fits'
hdu_list = fits.open(filename, memmap=True)
evt_data = Table(hdu_list[1].data)
wave=evt_data["wave"]#* u.AA 
flux=evt_data["flux"]#* u.Unit('erg cm-2 s-1 AA-1') 




def H(a, x):
    """Voigt Profile Approximation from T. Tepper-Garcia (2006, 2007)."""
    P = x**2
    H0 = np.exp(-x**2)
    Q = 1.5/x**2
    return H0 - a/np.sqrt(np.pi)/P * (H0*H0*(4.*P*P + 7.*P + 4. + Q) - Q - 1)

def Voigt(wl, l0, f, N, b, gam, z=0):
    """
    Calculate the optical depth Voigt profile.
    Parameters
    ----------
    wl : array_like, shape (N)
        Wavelength grid in Angstroms at which to evaluate the optical depth.
    l0 : float
        Rest frame transition wavelength in Angstroms.
        Oscillator strength.
    f : float
    N : float
        Column density in units of cm^-2.
    b : float
        Velocity width of the Voigt profile in cm/s.
    gam : float
        Radiation damping constant, or Einstein constant (A_ul)
    z : float
        The redshift of the observed wavelength grid `l`.
    Returns
    -------***
    tau : array_like, shape (N)
        Optical depth array evaluated at the input grid wavelengths `l`.
    """
    # ==== PARAMETERS ==================
    c = 2.99792e10        # cm/s
    m_e = 9.1094e-28       # g
    e = 4.8032e-10        # cgs units
    # ==================================
    # Calculate Profile
    C_a = np.sqrt(np.pi)*e**2*f*l0*1.e-8/m_e/c/b
    a = l0*1.e-8*gam/(4.*np.pi*b)
    # dl_D = b/c*l0
    wl = wl/(z+1.)
    # x = (wl - l0)/dl_D + 0.000001
    x = (c / b) * (1. - l0/wl)
    tau = np.float64(C_a) * N * H(a, x)
    return tau
 
N = 10**np.linspace(17,23,20)    # make an array of coloum densities
wave_l = 1215.6701    # atomic quantities for HI Lya
gamma = 6.265e+08
f_ij= 0.41640

b=2.e6              #  choose Doppler parameter in cm/s   (2e6 cm = 20 km/s) 
wl= wave*1e4# make a wavelength array,I changed to angstroms
ew_res=[]

# Main code

zobj=5.66
lobs=zobj*wave_l +wave_l
list2 =np.zeros(len(spectrum))
interval=np.where((lobs<wl) & (wl<1))  
for id_N in N:
     tau = Voigt(wl/6.66,wave_l,f_ij,id_N,b,gamma)
     spectrum=np.exp(-tau)     # generate spectrum 
     plt.plot(wl,spectrum)
     list2 = np.vstack([list2,spectrum])

  

newlist=list2[11,:] #11
minimum=np.min(newlist)
indexa = np.where(newlist ==minimum )#0.011360890876690344
print(minimum,indexa)    
listfinal=newlist[40:]
#print(listfinal)

#Program to set everything to zero before minimum
zerosl=list(np.zeros(len(spectrum)-len(listfinal)))
    
len(zerosl)
listf=zerosl.extend(listfinal)
flist=listfinal[:10]
#print(flist)

#print(list2[14,:])   #complete list of voigt profile selected line
#print(N[13]) ##check column density for selected profile
    

#########################################Other lines of original code
    #ew=integrate.trapz(wl, spectrum)
    #ew_res.append(ew)
#plt.xlabel('log N(HI)')
#plt.ylabel('log EW')
#lt.plot(np.log10(N),np.log10(ew_res))


