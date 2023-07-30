'''
2023-07-30
backup simple codes from previous works.
This code used on the paper Yi et al., J. Phys. D. 49, 195103 (2016)
'''

import numpy as np
from pylab import plot,show

PI=3.141592

name=""
output=open(name+'_fin.txt','w')

#sample, middle, magnitude
a=np.loadtxt(name+"smp.txt",skiprows=2)
smm=a[:,1]
freq=a[:,0]


#sample, middle, arg
b=np.loadtxt(name+"sma.txt",skiprows=2)
sma=b[:,1]

#sample, short, mag
c=np.loadtxt(name+"ssp.txt",skiprows=2)
ssm=c[:,1]

#sample, short, arg
d=np.loadtxt(name+"ssa.txt",skiprows=2)
ssa=d[:,1]


#mirror, middle, mag
e=np.loadtxt(name+"mmp.txt",skiprows=2)
mmm=e[:,1]

#mirror, middle, arg
f=np.loadtxt(name+"mma.txt",skiprows=2)
mma=f[:,1]

#mirror, short, mag
g=np.loadtxt(name+"msp.txt",skiprows=2)
msm=g[:,1]

#mirror, short, arg
h=np.loadtxt(name+"msa.txt",skiprows=2)
msa=h[:,1]


smx=smm*np.cos(np.radians(sma)) #sample mirror x-value
smy=smm*np.sin(np.radians(sma))
ssx=ssm*np.cos(np.radians(ssa))
ssy=ssm*np.sin(np.radians(ssa))

sx=smx-ssx #sample x-value
sy=smy-ssy


sm=np.sqrt(sx*sx+sy*sy) #sample magnitude

mmx=mmm*np.cos(np.radians(mma))
mmy=mmm*np.sin(np.radians(mma))
msx=msm*np.cos(np.radians(msa))
msy=msm*np.sin(np.radians(msa))

mx=mmx-msx
my=mmy-msy

mm=np.sqrt(mx*mx+my*my)

length=len(mm)

for i in range(length):
    output.write(str(freq[i]))
    output.write('\t')
    output.write(str(sm[i]/mm[i]))
    output.write('\n')

plot(freq,sm/mm)
show()
output.close()
