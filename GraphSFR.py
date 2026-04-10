# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 10:14:37 2024

@author: aurom
"""

#Make graphic of SFR and column density and SFR


import numpy as np
import glob
import matplotlib.pyplot as plt
import pandas as pd
# Seleccionar todos los archivos .csv en el directorio actual
archivos = glob.glob("*.txt")
SFR=[]
z=[]
CD=[]
list1=[]
# Iterar sobre los archivos y leer sus datos con genfromtxt
for archivo in archivos:  
    data = np.genfromtxt(archivo, skip_header=1)  # Asume un archivo CSV con delimitador y sin encabezado    
    SFR.append(data[12])
    z.append(data[1])
    CD.append(np.log10(data[13]))
#print(data[15])    
n=list(range(1,len(archivos)+1))


 #if list1[0,0].any()<5.9:
plt.scatter(CD,SFR,s=9,c=z,cmap='viridis_r',alpha=1)
cbar= plt.colorbar()
cbar.set_label('Z',labelpad=10) 

#else :
 #       plt.scatter(CD[i],SFR[i],c='blue',s=5)
    
plt.xlabel("log($N_H$)")
plt.ylabel(r"$SFR_{H\alpha}$")
plt.title(r"$SFR$ vs $N_H$",fontsize=14)
#for i, txt in enumerate(n):
 #   plt.annotate(txt, (CD[i], SFR[i]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(1, (CD[0], SFR[0]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(10, (CD[1], SFR[1]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(11, (CD[2], SFR[2]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(12, (CD[3], SFR[3]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(13, (CD[4], SFR[4]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(14, (CD[5], SFR[5]),textcoords="offset points", xytext=(3,-4),rotation=1)
plt.annotate(15, (CD[6], SFR[6]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(16, (CD[7], SFR[7]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(17, (CD[8], SFR[8]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(18, (CD[9], SFR[9]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(19, (CD[10], SFR[10]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(2, (CD[11], SFR[11]),textcoords="offset points", xytext=(-0.8,1),rotation=1)
plt.annotate(20, (CD[12], SFR[12]),textcoords="offset points", xytext=(2,1),rotation=1)
plt.annotate(21, (CD[13], SFR[13]),textcoords="offset points", xytext=(-1,6),rotation=1)
plt.annotate(22, (CD[14], SFR[14]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(23, (CD[15], SFR[15]),textcoords="offset points", xytext=(3,-1),rotation=1)
plt.annotate(24, (CD[16], SFR[16]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(25, (CD[17], SFR[17]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(26, (CD[18], SFR[18]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(27, (CD[19], SFR[19]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(3, (CD[20], SFR[20]),textcoords="offset points", xytext=(1,1),rotation=1)
plt.annotate(4, (CD[21], SFR[21]),textcoords="offset points", xytext=(3,3),rotation=1)
plt.annotate(5, (CD[22], SFR[22]),textcoords="offset points", xytext=(-1,-11),rotation=1)
plt.annotate(6, (CD[23], SFR[23]),textcoords="offset points", xytext=(-1,-11),rotation=1)
plt.annotate(7, (CD[24], SFR[24]),textcoords="offset points", xytext=(-1,5),rotation=1)
plt.annotate(8, (CD[25], SFR[25]),textcoords="offset points", xytext=(-15,1),rotation=1)
plt.annotate(9, (CD[26], SFR[26]),textcoords="offset points", xytext=(2,1),rotation=1)


plt.savefig('SFRvsCD.png', dpi=300)
plt.show()
print(z[11])

plt.scatter(z,SFR,s=9,c=z,cmap='viridis_r')
plt.xlabel("$Z$",font='Arial')
plt.ylabel(r"$SFR_{H\alpha}$")

plt.title(r"$SFR$ vs $Z$",fontsize=14)
#for i, txt in enumerate(n):
 #   plt.annotate(txt, (z[i], SFR[i]),textcoords="offset points", xytext=(3,1))
plt.annotate(1, (z[0], SFR[0]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(10, (z[1], SFR[1]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(11, (z[2], SFR[2]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(12, (z[3], SFR[3]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(13, (z[4], SFR[4]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(14, (z[5], SFR[5]),textcoords="offset points", xytext=(1,-4),rotation=1)
plt.annotate(15, (z[6], SFR[6]),textcoords="offset points", xytext=(-4,4),rotation=1)
plt.annotate(16, (z[7], SFR[7]),textcoords="offset points", xytext=(1,1),rotation=1)
plt.annotate(17, (z[8], SFR[8]),textcoords="offset points", xytext=(1,1),rotation=1)
plt.annotate(18, (z[9], SFR[9]),textcoords="offset points", xytext=(-14,1),rotation=1)
plt.annotate(19, (z[10], SFR[10]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(2, (z[11], SFR[11]),textcoords="offset points", xytext=(2,1),rotation=1)
plt.annotate(20, (z[12], SFR[12]),textcoords="offset points", xytext=(-1,-0.5),rotation=1)
plt.annotate(21, (z[13], SFR[13]),textcoords="offset points", xytext=(-1,7),rotation=1)
plt.annotate(22, (z[14], SFR[14]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(23, (z[15], SFR[15]),textcoords="offset points", xytext=(3,-1),rotation=1)
plt.annotate(24, (z[16], SFR[16]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(25, (z[17], SFR[17]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(26, (z[18], SFR[18]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(27, (z[19], SFR[19]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(3, (z[20], SFR[20]),textcoords="offset points", xytext=(1,3),rotation=1)
plt.annotate(4, (z[21], SFR[21]),textcoords="offset points", xytext=(3,3),rotation=1)
plt.annotate(5, (z[22], SFR[22]),textcoords="offset points", xytext=(-1,-11),rotation=1)
plt.annotate(6, (z[23], SFR[23]),textcoords="offset points", xytext=(-1,-11),rotation=1)
plt.annotate(7, (z[24], SFR[24]),textcoords="offset points", xytext=(-1,5),rotation=1)
plt.annotate(8, (z[25], SFR[25]),textcoords="offset points", xytext=(-15,1),rotation=1)
plt.annotate(9, (z[26], SFR[26]),textcoords="offset points", xytext=(2,-4),rotation=1)

cbar= plt.colorbar()
cbar.set_label('Z',labelpad=10) 
plt.savefig('SFRvsz.png', dpi=300)
plt.show()










