print (" Nama	: Stefanus kevin alfandara")
print (" NIM  	: 311810200")
print (" Kelas	: TI.18.A1 ")

print ("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print ("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print ("MENENTUKAN BILANGAN TERBESAR DARI 3 BILANGAN YANG DI INPUTKAN !! ")
print ("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print ("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
	
def pengulangan():

	a=int(input("Bilangan 1 = "))
	b=int(input("Bilangan 2 = "))
	c=int(input("Bilangan 3 = "))

	if a>b and a>c:
		if b>c:
			print (a,"Adalah Bilangan Terbesar")
		else:
			print(a,"Adalah Bilangan Terbesar")
	elif b>a and b>c:
		if a>c:
			print(b,"Adalah Bilangan Terbesar")
		else:
			print(b,"Adalah Bilangan Terbesar")
	else:
		if a>b:
			print(c,"Adalah Bilangan Terbesar")
		else:
			print(c,"Adalah Bilangan Terbesar")

pengulangan()