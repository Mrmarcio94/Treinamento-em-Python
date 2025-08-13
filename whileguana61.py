print("Gerador de P.A")
print("-=" * 10)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da P.A: "))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('FIM!')

#Parei em 5:53 no vídeo do guanabara