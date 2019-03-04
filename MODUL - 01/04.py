def rerata(x):
	"""Hitung Rata Rata dari List"""
	jml=0
	banyak=0
	for angka in x:
		jml+=angka
		banyak+=1
	return jml/banyak
print(rerata([1,2,3,4,5]))
