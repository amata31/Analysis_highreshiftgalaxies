# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 16:06:52 2024

@author: aurom
"""


import numpy as np
import glob
import matplotlib.pyplot as plt
import pandas as pd
# Seleccionar todos los archivos .csv en el directorio actual
archivos = glob.glob("*.txt")
falfa=[]
fbeta=[]
fOIII=[]
fn=[]
w=[]
sigma3=[]


# Iterar sobre los archivos y leer sus datos con genfromtxt
for archivo in archivos:  
      # Asume un archivo CSV con delimitador y sin encabezado  
    data1 = np.genfromtxt(archivo, skip_header=1)  
    falfa.append(data1[2])
    fbeta.append(data1[8])
    fOIII.append(data1[4])
    sigma3.append(data1[15])
    w.append(data1[16])
    #fn.append(data1[16])
    

#print(data1[17]) #fn[21]
#
#print(fn)
#Integrated flux
#for 
#fn=np.sqrt(2*np.pi)*sigma3*w*1e4


#Calcultate quotients
x=[]
y=[]
kewley_y=[]
kauffmann_y=[]
for i in range(len(archivos)):
    fn=np.sqrt(2*np.pi)*sigma3[i]*w[i]*1e4
    y.append(np.log10(fOIII[i]/abs(fbeta[i])))
    x.append(np.log10(fn/falfa[i]))   
    
#print(x[21])    
plt.scatter(x,y,color='black',s=9,marker=r"$\uparrow$")  
#BPT lines
y_max=1.6
y_min=-0.2
x_max=0.3#0.3
x_min=-1.7

plt.ylim(y_min,y_max)
plt.xlim(x_min,x_max)


x_a=np.arange(-5,0.049,.01)
x_b=np.arange(-5,0.469,0.01)
#x_c=np.arange(xt,1.0,0.01)
k03=0.61/(x_a-0.05)+1.3
ke01=0.61/(x_b-0.47)+1.19

            #(Ya-0.61/(Xa-0.47)-1.19)
#yc=1.01*x_c+0.48
plt.plot(x_a,k03,"r--",label='Kauffmann 2003',lw=1)
plt.plot(x_b,ke01,"blue",label='Kewley 2001',lw=1)

plt.legend()

plt.annotate(1, (x[0], y[0]),textcoords="offset points", xytext=(1,3),rotation=1)
plt.annotate(10, (x[1], y[1]),textcoords="offset points", xytext=(2,-1),rotation=1)
plt.annotate(11, (x[2], y[2]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(12, (x[3], y[3]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(13, (x[4], y[4]),textcoords="offset points", xytext=(1,3),rotation=1)
plt.annotate(14, (x[5], y[5]),textcoords="offset points", xytext=(3,-4),rotation=1)
plt.annotate(15, (x[6], y[6]),textcoords="offset points", xytext=(-3,4),rotation=1)
plt.annotate(16, (x[7], y[7]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(17, (x[8], y[8]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(18, (x[9], y[9]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(19, (x[10], y[10]),textcoords="offset points", xytext=(0,2),rotation=1)
plt.annotate(2, (x[11], y[11]),textcoords="offset points", xytext=(3,2),rotation=1)
plt.annotate(20, (x[12], y[12]),textcoords="offset points", xytext=(2,1),rotation=1)
plt.annotate(21, (x[13], y[13]),textcoords="offset points", xytext=(3,3),rotation=0)
plt.annotate(22, (x[14], y[14]),textcoords="offset points", xytext=(1,-1),rotation=1)
plt.annotate(23, (x[15], y[15]),textcoords="offset points", xytext=(1,1),rotation=1)
plt.annotate(24, (x[16], y[16]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(25, (x[17], y[17]),textcoords="offset points", xytext=(3,1),rotation=1)
plt.annotate(26, (x[18], y[18]),textcoords="offset points", xytext=(-1,7),rotation=1)
plt.annotate(27, (x[19], y[19]),textcoords="offset points", xytext=(1,1),rotation=1)
plt.annotate(3, (x[20], y[20]),textcoords="offset points", xytext=(1,1),rotation=1)
plt.annotate(4, (x[21], y[21]),textcoords="offset points", xytext=(3,3),rotation=1)
plt.annotate(5, (x[22], y[22]),textcoords="offset points", xytext=(2,-4),rotation=1)
plt.annotate(6, (x[23], y[23]),textcoords="offset points", xytext=(1,2),rotation=1)
plt.annotate(7, (x[24], y[24]),textcoords="offset points", xytext=(-1,5),rotation=1)
plt.annotate(8, (x[25], y[25]),textcoords="offset points", xytext=(2,-1),rotation=1)
plt.annotate(9, (x[26], y[26]),textcoords="offset points", xytext=(2,1),rotation=1)

plt.text(-1.55, 1.3, "AGN", fontsize=12, color="black",weight='bold')
plt.text(-1.5, 0, "SF", fontsize=12, color="black",weight='bold')
plt.text(-0.33, 0, "Comp", fontsize=12, color="black",weight='bold')
#plt.text(0.01, 0.4, "LINERs", fontsize=11, color="black")
plt.ylabel(r'log([OIII]/H$\beta$)')
plt.xlabel(r"log(3$\sigma$ [NII]/H$\alpha$)")
plt.title('BPT diagram with 3$\sigma$ limits')
plt.savefig('BPT.png', dpi=300)
plt.show()




with open("Cocientes.txt", "w") as archivo:
    archivo.write(f"t{x[0]}\t{y[0]}\n")
    archivo.write(f"t{x[11]}\t{y[11]}\n")
    archivo.write(f"t{x[20]}\t{y[20]}\n")
    archivo.write(f"t{x[21]}\t{y[21]}\n")
    archivo.write(f"t{x[22]}\t{y[22]}\n")
    archivo.write(f"t{x[23]}\t{y[23]}\n")
    archivo.write(f"t{x[24]}\t{y[24]}\n")
    archivo.write(f"t{x[25]}\t{y[25]}\n")
    archivo.write(f"t{x[26]}\t{y[26]}\n")
    archivo.write(f"t{x[1]}\t{y[1]}\n")
    archivo.write(f"t{x[2]}\t{y[2]}\n")
    archivo.write(f"t{x[3]}\t{y[3]}\n")
    archivo.write(f"t{x[4]}\t{y[4]}\n")
    archivo.write(f"t{x[5]}\t{y[5]}\n")
    archivo.write(f"t{x[6]}\t{y[6]}\n")
    archivo.write(f"t{x[7]}\t{y[7]}\n")
    archivo.write(f"t{x[8]}\t{y[8]}\n")
    archivo.write(f"t{x[9]}\t{y[9]}\n")
    archivo.write(f"t{x[10]}\t{y[10]}\n")
    archivo.write(f"t{x[12]}\t{y[12]}\n")
    archivo.write(f"t{x[13]}\t{y[13]}\n")
    archivo.write(f"t{x[14]}\t{y[14]}\n")
    archivo.write(f"t{x[15]}\t{y[15]}\n")
    archivo.write(f"t{x[16]}\t{y[16]}\n")
    archivo.write(f"t{x[17]}\t{y[17]}\n")
    archivo.write(f"t{x[18]}\t{y[18]}\n")
    archivo.write(f"t{x[19]}\t{y[19]}\n")
    













