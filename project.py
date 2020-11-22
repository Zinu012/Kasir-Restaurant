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
			mkn = int(input("Jumlah porsi : "))
			jmlhpsn = mkn * 12000
			print("Harga nasi goreng = Rp 12000")
			print ("Total Harga = Rp ", jmlhpsn)
			pil=6
			
		if pil == 2:
			mkn = int(input("Jumlah porsi : "))
			jmlhpsn = mkn * 11000
			print("Harga Mie Ayam = Rp 11000")
			print ("Total Harga = Rp ",jmlhpsn)
			pil=6
			
		if pil == 3:
			mkn = int(input("Jumlah porsi : "))
			jmlhpsn = mkn * 7500
			print("Harga bihun goreng = Rp 7500")
			print ("Total Harga = Rp ", jmlhpsn)
			pil=6
			
		if pil == 4:
			mkn = int(input("Jumlah porsi : "))
			jmlhpsn = mkn * 8000
			print ("Harga mie goreng = Rp 8000")
			print ("Total Harga = Rp ", jmlhpsn)
			pil=6
			
		if pil == 5:
			mkn = (input("Jumlah porsi : "))
			jmlhpsn = mkn * 5000
			print ("Harga capcay = Rp 5000")
			print ("Total Harga = Rp ", jmlhpsn)
			pil=6
		else:
			exit

			
									


	pil = 0
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
			mnm = int(input("Jumlah gelas : "))
			jmlhpsn2 = (mnm * 3000) 
			print ("Harga Air Mineral = Rp 3000")
			print ("Total Minuman = Rp ",jmlhpsn2)
			pil=6
			Total_seluruhnya = jmlhpsn + jmlhpsn2
			print ("Total harga seluruh pesanan adalah ",Total_seluruhnya)
			Mny = int(input("Masukkan jumlah uang "))
			Kembalian = Mny - Total_seluruhnya
			print("Total kembalian = ",Kembalian)
			back_menu()			

		if pil == 2:
			mnm = int(input("Jumlah gelas : "))
			jmlhpsn2 = (mnm * 2000) 
			print("Harga Es Teh Manis = Rp 2000")
			print ("Total Minuman = Rp ",jmlhpsn2)
			pil=6
			Total_seluruhnya = jmlhpsn + jmlhpsn2
			print ("Total harga seluruh pesanan adalah ",Total_seluruhnya)
			Mny = int(input("Masukkan jumlah uang "))
			Kembalian = Mny - Total_seluruhnya
			print("Total kembalian = ",Kembalian)
			
			back_menu()
		if pil == 3:
			mnm = int(input("Jumlah gelas : "))
			jmlhpsn2 = (mnm * 3500) 
			print ("Harga Es Jeruk = Rp 3500")
			print("Total Minuman = Rp ",jmlhpsn2)
			pil=6
			Total_seluruhnya = jmlhpsn + jmlhpsn2
			print ("Total harga seluruh pesanan adalah ",Total_seluruhnya)
			Mny = int(input("Masukkan jumlah uang "))
			Kembalian = Mny - Total_seluruhnya
			print("Total kembalian = ",Kembalian)
			back_menu()
		if pil == 4:
			mnm = int(input("Jumlah gelas : "))
			jmlhpsn2 = (mnm * 5000) 
			print ("Harga Jus Alpukat = Rp 5000")
			print ("Total Minuman = Rp ",jmlhpsn2)
			pil=6
			Total_seluruhnya = jmlhpsn + jmlhpsn2
			print ("Total harga seluruh pesanan adalah ",Total_seluruhnya)
			Mny = int(input("Masukkan jumlah uang "))
			Kembalian = Mny - Total_seluruhnya
			print("Total kembalian = ",Kembalian)
			back_menu()
		if pil == 5:
			mnm = int(input("Jumlah gelas : "))
			jmlhpsn2 = (mnm * 4000) 
			print ("Harga Jus Mangga = Rp 4000")
			print ("Total Minuman = Rp ",jmlhpsn2)
			pil=6
			Total_seluruhnya = jmlhpsn + jmlhpsn2
			print ("Total harga seluruh pesanan adalah ",Total_seluruhnya)
			Mny = int(input("Masukkan jumlah uang "))
			Kembalian = Mny - Total_seluruhnya
			print("Total kembalian = ",Kembalian)
			back_menu()
		
		  
def back_menu():
	print ('Apakah anda ingin memesan lagi? [Y/N] :')
	back = input().upper()
	if back == "Y":
		menu_utama1()
		pilihan()
	else:
		print("Terima Kasih !")
		exit


menu_utama()
pilihan()

