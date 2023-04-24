Lugares_vagos= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while True:
    sala = int(input("digite quantos assento você quer!(0 sai):"))
    if sala == 0:
        print("fim")
        break
    if sala > len(Lugares_vagos) or sala < 1:
        print("sala inválida")
    elif Lugares_vagos [sala - 1 ] == 0:
        print("desculpe, sala lotada!")
    else:
        lugares= int(input(f"confirme quantos lugares! ({Lugares_vagos[sala - 1]}vagos:)"))
    if lugares > Lugares_vagos [sala - 1]:
        print ("esse numero de lugares não está disponivel.")
    elif lugares < 0:
        print("numero invalido")
    else:
        Lugares_vagos[sala - 1] -= lugares
        print(f"{lugares} lugares vendidos")
print("utilização das salas")
for x, l in enumerate(Lugares_vagos):
    print(f"sala {x + 1 } - {l} lugar(es) vazio(s)")