print ("Olá me chamo Jéssica, sou assistente virtual da Vivo. \nGostaria de saber qual o seu consumo mensal de internet")

menu = """
================ Menu ================
[1] Consumo de até 10 GB
[2] Consumo entre 10 - 20 GB
[3] Consumo maior que 20 GB
[4] Lista de Plano
[0] Sair \n

=>"""

while True:

    opcao = input(menu)

    if opcao == "1":
        nome = str(input("Te indico o Plano Essencial Fibra - 50Mbps. \nPara saber mais volte para o menu - clink Enter"))

    elif opcao == "2":
        nome = str(input("Te indico o Plano Prata Fibra - 100Mbps. \nPara saber mais volte para o menu - clink Enter"))

    elif opcao == "3":
        nome = str(input("Te indico o Plano Premium Fibra - 300Mbps. \nPara saber mais volte para o menu - clink Enter"))

    elif opcao == "4":
        print("\n===================== Lista de Plano =====================")
        print("\n-Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB.")
        print("\n-Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB.")
        print("\n-Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB.")
        print("============================================================")

    elif opcao == "0":
        print("Espero que tenha te ajudado. Volte sempre!") 
        exit()

    else:
        print("Falha no sistema, por favor selecione novamente a operação desejada.") 
