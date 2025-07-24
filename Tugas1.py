# Buat progam baru toko.py
# Buat list od dictionary,bernama items
# key items: nama,stok,harga
# 1. isi list of dictionary tersebut sebanyak 5 items 
# 2. tampilan list ari list of dictionary menggunakan perulangan for atau while
# 3. buat fuction create untuk menambahkan item ke list of dictionary 


# 1. isi list of dictionary tersebut sebanyak 5 items 
Barang1 = {"nama":"eyeliner","stok":10,"harga":50000}
Barang2 = {"nama":"foundation","stok":15,"harga":100000}
Barang3 = {"nama":"mascara","stok":5,"harga":20000}
Barang4 = {"nama":"bedak","stok":12,"harga":25000}
Barang5 = {"nama":"alis","stok":2,"harga":12000}

merkBarang = [Barang1,Barang2,Barang3,Barang4,Barang5]



# 2. tampilan list ari list of dictionary menggunakan perulangan for atau while
for i in range (len(merkBarang)):
    print("Nama barang-", i,":",merkBarang[i]["nama"])
   
   
   
# 3. buat fuction create untuk menambahkan item ke list of dictionary  
def creat():
    nama = str(input())
    stok = str(input())
    harga = int(input())
    Barang6= {"nama":nama,"stok":stok,"harga":harga}
    merkBarang.append(Barang6)

    
creat()
print(merkBarang)
    


