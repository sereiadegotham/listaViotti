t = int(input("Informe o tempo da viagem (em horas): "))
v = int(input("Informe a velocidade: "))

km = t*v

if km>50:
    print("Você já está na metade do caminho.")
else:
    print("Ainda tem chão pra rodar!!")
