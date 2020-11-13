def menu_utama():
	print("")
	n = input("Masukkan Nama Konsumen: ")
	print("Nama Konsumen :",n)
	print ("""
		Masukkan Pilihan
		1. Bayar
		2. Keluar
			""")
	print("")


def menu_utama1():
	print("""
		Masukkan Pilihan
		1. Bayar
		2. Keluar
			""")
	print("")
	
			
def pilihan():
	x = int(input("Masukan Pilihan : "))

	if x == 1:
		mk = makanan()

	pil = 1
	while pil !=6:
		print ("""
		Pilih Makanan
		1. NASI GORENG
		2. MIE AYAM
		3. Bihun Goreng
		4. Mie goreng
		5. Capcay
		6. Minuman
			""")
		pil = int(input("Masukkan pilihan anda : "))
		print()
		if pil == 1:
			print ("")
			x = int(input("Jumlah porsi : "))
			mk = makanan()
			mk.nasi_goreng(x)
			pil=6
			
		if pil == 2:
			print ("")
			x = int(input("Jumlah porsi : "))
			mk = makanan()
			mk.mie_ayam(x)
			pil=6
			
		if pil == 3:
			print ("")
			x = int(input("Jumlah porsi : "))
			mk = makanan()
			mk.bihun_goreng(x)
			pil=6
			
		if pil == 4:
			print ("")
			x = int(input("Jumlah porsi : "))
			mk = makanan()
			mk.mie_goreng(x)
			pil=6
			
		if pil == 5:
			print ("")
			x = (input("Jumlah porsi : "))
			mk = makanan()
			mk.capcay(x)
			print()
			pil=6
		else:
			exit

			
									


	pil = 0
	mn = minuman()
	while pil !=6:
		print ("""
			Pilih Minuman
			1. Air mineral
			2. Es teh manis
			3. Es Jeruk
			4. Jus Alpukat
			5. Jus Mangga
				""")
		pil = int(input("Masukkan pilihan anda : "))
		print
		if pil == 1:
			print ("")
			z = int(input("Jumlah gelas : "))
			mn = minuman()
			mn.air_mineral(z)
			pil=6
			back_menu()
		if pil == 2:
			print ("")
			z = int(input("Jumlah gelas : "))
			mn = minuman()
			mn.es_teh_manis(z)
			pil=6
			back_menu()
		if pil == 3:
			print ("")
			z = int(input("Jumlah gelas : "))
			mn = minuman()
			mn.es_jeruk(z)
			pil=6
			back_menu()
		if pil == 4:
			print ("")
			z = int(input("Jumlah gelas : "))
			mn = minuman()
			mn.jus_alpukat(z)
			pil=6
			back_menu()
		if pil == 5:
			print ("")
			z = int(input("Jumlah gelas : "))
			mn = minuman()
			mn.jus_mangga(z)
			pil=6
			back_menu()
		
		  


class makanan():
	def nasi_goreng (self,x):
		jmlhpsn = x * 7000
		print("Harga nasi goreng = Rp 7000")
		print ("Total Harga = Rp ", jmlhpsn)
		return jmlhpsn
	def mie_ayam (self,x):
		jmlhpsn = x * 6000
		print("Harga Mie Ayam = Rp 6000")
		print ("Total Harga = Rp ",jmlhpsn)
		return jmlhpsn
	def bihun_goreng (self,x):
		jmlhpsn = x * 7500
		print("Harga bihun goreng = Rp 7500")
		print ("Total Seluruhnya = Rp ", jmlhpsn)
		return jmlhpsn
	def mie_goreng (self,x):
		jmlhpsn = x * 8000
		print ("Harga mie goreng = Rp 8000")
		print ("Total Seluruhnya = Rp ", jmlhpsn)
		return jmlhpsn
	def capcay (self,x):
		jmlhpsn = x * 5000
		print ("Harga capcay = Rp 5000")
		print ("Total Seluruhnya = Rp ", jmlhpsn)
		return jmlhpsn
	
class minuman():
	def air_mineral (self,z):
		jmlhpsn2 = z * 3000
		print ("Harga Air Mineral = Rp 3000")
		print ("Total Minuman = Rp ",jmlhpsn2)
		return jmlhpsn2
	def es_teh_manis (self,z):
		jmlhpsn2 = z * 2000
		print("Harga Es Teh Manis = Rp 2000")
		print ("Total Minuman = Rp ",jmlhpsn2)
		return jmlhpsn2
	def es_jeruk (self,z):
		jmlhpsn2 = z * 3500
		print ("Harga Es Jeruk = Rp 3500")
		print("Total Minuman = Rp ",jmlhpsn2)
		return jmlhpsn2
	def jus_alpukat (self,z):
		jmlhpsn2 = z * 5000
		print ("Harga Jus Alpukat = Rp 5000")
		print ("Total Minuman = Rp ",jmlhpsn2)
		return jmlhpsn2
	def jus_mangga (self,z):
		jmlhpsn2 = z * 4000
		print ("Harga Jus Mangga = Rp 4000")
		print ("Total Minuman = Rp ",jmlhpsn2)
		return jmlhpsn2


def back_menu():
	print ('Apakah anda ingin memesan lagi? [Y/N] :')
	back = input().upper()
	if back == "Y":
		menu_utama1()
		pilihan()
		print("")
	else:
		print("Terima Kasih !")
		exit


menu_utama()
pilihan()

