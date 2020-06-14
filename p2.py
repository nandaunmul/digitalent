# nama file p2.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 0

#netacad email cth: 'abcd@gmail.com'
email='nanda.arista@fkip.unmul.ac.id'
 
# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini

#Graded

def isPointInCircle(x,y,r,center=(0,0)):
  # MULAI KODEMU DI SINI
  x0=center[0]
  y0=center[1]
  if (x-x0)**2+(y-y0)**2 <= r**2:
      return True
  else:
      return False

#CEK OUTPUT KODE ANDA
print(isPointInCircle(1,1,1,center=(0,0)),isPointInCircle(1,0,1,center=(0,0)),
      isPointInCircle(1,1,1,center=(1,0)),isPointInCircle(0,0,1,center=(1,1)))


#Graded
import random


def generateRandomSquarePoints(n,length,center=(0,0)):
  # MULAI KODEMU DI SINI
  minx  = center[0]-length/2
  maksx = center[0]+length/2
  miny  = center[1]-length/2
  maksy = center[1]+length/2
  
  # Gunakan list comprehension dengan variable minx, miny, length, dan n
  points = [[random.uniform(minx, maksx), random.uniform(miny, maksy)] for acak in range(n)]

  return points

#CEK OUTPUT KODE ANDA
random.seed(0)

# generate 100 point di dalam persegi dengan panjang sisi 1 dan berpusat di (0,0)
points = generateRandomSquarePoints(100,1)
print(points[10:15])

#CEK OUTPUT KODE ANDA VISUALISASI
# Mari kita Visualisasikan 
# Jika sama dengan gambar di bawah ini maka keluaran sesuai harapan
import matplotlib.pyplot as plt
x,y = zip(*points)

# persegi dengan panjang sisi 1 dan berpusat di (0,0)
r1 = plt.Rectangle((-0.5,-0.5),1,1,color='r', fill=False)
c1 = plt.Circle((0,0), 0.5, color='b', fill=False)
fig, ax = plt.subplots(figsize=(9,9)) 
ax.add_artist(r1)
ax.add_artist(c1)
plt.xlim(-0.6,0.6)
plt.ylim(-0.6,0.6)
plt.scatter(x,y,s=100,marker='x')
plt.show()


#Graded

def MCCircleArea(r,n=100,center=(0,0)):
  # MULAI KODEMU DI SINI
  sisi=2*r
  luaspersegi=sisi*sisi
  ntitikdalam=0
  #for i in range(n):
  #    x=generateRandomSquarePoints(n,sisi,center)[i][0]
  #    y=generateRandomSquarePoints(n,sisi,center)[i][1]
  #    if isPointInCircle(x,y,r,center) == True:
  #        ntitikdalam+=1
  for x,y in generateRandomSquarePoints(n,sisi,center):
      if isPointInCircle(x,y,r,center) == True:
          ntitikdalam+=1
  luaslingkaran=(ntitikdalam/n)*luaspersegi
  return luaslingkaran

#CEK OUTPUT KODE ANDA

random.seed(0)
print(MCCircleArea(1,100),MCCircleArea(1,10,center=(10,10)))


#Graded

def LLNPiMC(nsim,nsample):
  # MULAI KODEMU DI SINI
  simpi=0
  for i in range(nsample):
      simpi+=MCCircleArea(1,nsim)
  return simpi/nsample

#CEK OUTPUT KODE ANDA

import math

random.seed(0)
estpi = LLNPiMC(10000,500)

print('est_pi:',estpi)
print('act_pi:',math.pi)


# Graded
def relativeError(act,est):
  
  # MULAI KODEMU DI SINI
  return abs((est-act)/act)*100

#CEK OUTPUT KODE ANDA
print('error relatif:',relativeError(math.pi,estpi),'%')