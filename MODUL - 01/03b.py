def jumlahHurufVokal(x):
	vokal="AIUEOaiueo"
	jmlhuruf=len(x)
	jmlkonsonan=0
	for karakter in x:
		if karakter not in vokal:
			jmlkonsonan+=1
	return (jmlhuruf, jmlkonsonan)
k=jumlahHurufVokal("Surakarta")
print(k)