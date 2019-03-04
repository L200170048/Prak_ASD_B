import random
jawaban=random.randint(1,100)

print("Permainan Tebak Angka")
print("Saya menyimpan angka bulat antara 1 sampai 100. coba tebak")
live=1
while live <= 7:
	inputan=int(input("Masukkan tebakkan ke-"+str(live)+":>"))
	if inputan==jawaban:
		print("Ya. Anda Benar")
		break;
	elif inputan<jawaban:
		print("Itu terlalu kecil")
	elif inputan>jawaban:
		print("Itu terlalu Besar")
	live+=1
print("Jawbannya :", jawaban)
