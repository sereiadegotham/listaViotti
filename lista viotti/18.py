idade = int(input("Informe a idade do nadador: "))

if 5<=idade<=7:
    print("Infantil A")
elif 8<=idade<=10:
    print("Infantil B")
elif 11<=idade<=13:
    print("Juvenil A")
elif 14<=idade<=17:
    print("Juvenil B")
elif 18<=idade<=60:
    print("Adulto")
elif idade>60:
    print("Senior")
