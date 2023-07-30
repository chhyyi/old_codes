'''
[2023-07-30]
backup codes from previous works.
This code used on the paper Yoo et al., Sci. Reports 6, 33416 (2016)
to plot figures

[original description>]
this script calculate transmission from two Efield file
(with sample, without sample) exported by CST MWS.
1. import y-component efield data from 2 file.
2. Loop : Points along a contour.
    2.1. Substrate E-field of w/osample from w/sample.
    2.2. Add efield on some rectangle plane,
    of which central is the points of the loop.
    
3. print two list. position and Efield.

Parameters:
 input file name
     w/osample, w/sample
 port size x,y
 starting point/terminal point of contour


 *in this case,  we have used 528 * 684 mm^2 simulation space.
 so I may choose contour... [(0,-270) -> (0,270)] or [(-210,0) -> (210,0)]
'''




import numpy as np
import matplotlib.pyplot as plt

#------parameters------


#file names
samplefile='xy_pz30.txt' 
wo_sample='xy_wosample_pz30.txt'
output=open("graph.txt","w")

#port size
px=90
py=120

#contour
stp=[-200.0,0.0] #list, starting point (x,y), remember z-component is fixed in this case.
tep=[200.0,0.0] #list, terminal point (x,y)
cep=stp

#others
points=50

dist=np.zeros(points+1) #result data, position.
field_sum=np.zeros(points+1) #result data, field.
field_sum2=np.zeros(points+1) #result data, field.

rawdata=np.loadtxt(samplefile,skiprows=2)
rawdata2=np.loadtxt(wo_sample,skiprows=2)
pos=np.zeros((len(rawdata),2))
field=np.zeros((len(rawdata),2))

pos2=np.zeros((len(rawdata2),2))
field2=np.zeros((len(rawdata2),2))


#initialization
pos[:,0]=rawdata[:,0]
pos[:,1]=rawdata[:,1]
field[:,0]=rawdata[:,4]
field[:,1]=rawdata[:,7]

pos2[:,0]=rawdata2[:,0]
pos2[:,1]=rawdata2[:,1]
field2[:,0]=rawdata2[:,4]
field2[:,1]=rawdata2[:,7]

count=0
count2=0
count_prev=0
count_prev2=0

for i in range(points+1):


    
    cep=(stp+float(i)*(np.subtract(tep,stp)/float(points))) #central points now we calculate the sum of efield.
    dist[i]=np.linalg.norm(cep-stp)
    print dist
    for j in range(len(rawdata)):
        if np.absolute(cep[0]-pos[j,0])<px/2.0:
            if np.absolute(cep[1]-pos[j,1])<py/2.0:
                field_sum[i]+=rawdata[j,4]*rawdata[j,4]+rawdata[j,7]*rawdata[j,7]
                count+=1
    field_sum[i]=field_sum[i]/count

    for j in range(len(rawdata2)):
        if np.absolute(cep[0]-pos2[j,0])<px/2.0:
            if np.absolute(cep[1]-pos2[j,1])<py/2.0:
                field_sum2[i]+=rawdata2[j,4]*rawdata2[j,4]+rawdata2[j,7]*rawdata2[j,7]
                count2+=1
    field_sum2[i]=field_sum2[i]/count2

    #verifying every data points had same points invloved in mesh.
    if count!=count_prev:
        print ('count not same!')
    if count!=count2:
        print ('count not same!')

    count_prev=count
    count_prev2=count2
    
    count2=0
    count=0

print dist
print field_sum

plt.figure()
plt.plot(dist,field_sum/field_sum2)
plt.show()
                        
for i in range(points+1):
    output.write(str(dist[i])+'\t'+str(field_sum[i]/field_sum2[i])+'\n')

output.close()
