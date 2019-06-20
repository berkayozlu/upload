while (True):
	print ('----------The Great Calculator----------')
	print ('a = Toplama')
	print ('b = cikarma')
	print ('c = carpma')
	print ('d = bolme')
	print ('e = cikis')
	deisgen = input ('Yapmak istediniz islemi secin:')
	if deisgen == 'e':
		break

	elif deisgen == 'a':
		adeger1 = input ('Deger 1:')
		adeger2 = input ('Deger 2:')
		sonuca = (int(adeger1) + int(adeger2))
		print (sonuca)
	elif deisgen == 'b':
		bdeger1 = input ('Deger 1:')
		bdeger2 = input ('Deger 2:')
		sonucb = (int(bdeger1) - int(bdeger2))
		print (sonucb)
	elif deisgen == 'c':
		cdeger1 = input ('Deger 1:')
		cdeger2 = input ('Deger 2:')
		sonucc = (int(cdeger1) * int(cdeger2))
		print (sonucc)
	elif deisgen == 'd':
		ddeger1 = input ('Deger 1:')
		ddeger2 = input ('Deger 2:')
		sonucd = (int(ddeger1) / int(ddeger2))
		print (sonucd)	
	else:
		print ('Hata!')
#