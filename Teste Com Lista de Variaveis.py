grupo = ["Pedro", "Kaiki", "Vitor","Atila"]
print(grupo)
SN=(input("Deseja adicionar participante? "))

while SN == "sim":
    add_part=(input("Digite o nome de um novo participante: "))

    grupo.extend([f"{add_part}"])

    print(grupo)
   
    SN=(input("Deseja adicionar participante? "))

    if SN == "nao" or SN == "não":
        print('Seu Grupo é composto por:')
        for pessoa in grupo:
            print(pessoa)

        break
