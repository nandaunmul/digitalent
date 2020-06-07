# nama file p1.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded
# Isikan juga priority file

# untuk resubmisi, grader hanya akan mengambil priority yang paling besar
# jadi kalau anda ingin merevisi kode anda:
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0

priority = 0


#netacad email cth: 'abcd@gmail.com'
email='nanda.arista@fkip.unmul.ac.id'

# copy-paste semua #Graded cells di bawah ini

# PASTE KODE ANDA DISINI 
#Graded

# Manual, filter, list comprehension
def letter_catalog(items,letter='A'):
  list_nya=[]
  banyaknya=len(items)
  for i in range(banyaknya):
    if items[i][0]==letter:
      list_nya.append(items[i])
  return print(list_nya)
  
# Cek output kode anda
letter_catalog(['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries'],letter='A')

#Graded

def counter_item(items):
  # MULAI KODEMU DI SINI
  kamus={}
  for i in items:
    if i not in kamus:
      kamus[i]=1
    else:
      kamus[i]+=1
  #print(kamus)
  return kamus  

# Cek output kode anda
counter_item(['Apple','Apple','Apple','Blueberries','Blueberries','Blueberries'])

#Graded

# dua variable berikut jangan diubah
fruits = ['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries','Date Fruit','Grapes','Guava','Jackfruit','Kiwifruit']
prices = [6,5,3,10,12,7,14,15,8,7,9]

# list buah
chart = ['Blueberries','Blueberries','Grapes','Apple','Apple','Apple','Blueberries','Guava','Jackfruit','Blueberries','Jackfruit']

# MULAI KODEMU DI SINI
if len(fruits)==len(prices):
    fruit_price = {}
    for i in range(len(fruits)):
        fruit_price[fruits[i]]=prices[i]

def total_price(dcounter,fprice):
  # MULAI KODEMU DI SINI
  harga=0
  for buah, beli in dcounter.items():
      harga+=beli*fprice[buah]
  #print(harga)
  return harga

total_price(counter_item(chart),fruit_price)

#Graded

def discounted_price(total,discount,minprice=100):
  #pass
  # MULAI KODEMU DI SINI
  if total>=minprice:
      total-=discount*total/100
      #print(total)
      return total      

discounted_price(total_price(counter_item(chart),fruit_price),10,minprice=100)

#Graded

def print_summary(items,fprice):
  #pass
  # MULAI KODEMU DI SINI
  daftar_awal=counter_item(items)
  daftar_awal=sorted(daftar_awal.items())
  daftar={}
  for butir in daftar_awal:
      daftar[butir[0]]=butir[1]
  for namabuah in daftar:
      print(daftar[namabuah]," ",namabuah," : ",daftar[namabuah]*fprice[namabuah],"\n",sep="",end="")
  print("total :",total_price(counter_item(chart),fruit_price))
  print("discount price :",discounted_price(total_price(counter_item(chart),fruit_price),10,minprice=100))
      
print_summary(chart,fruit_price)
