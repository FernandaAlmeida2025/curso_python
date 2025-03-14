executar = True 
while executar : 
    escolhas = '''
        [1] ou [+] para somar
        [2] ou [-] para subtrair
        [3] ou [\] para dividir
        [4] ou [*] para multiplicar
        [5] para sair
        '''
    print(escolhas)   
    operador = input("Qual sua opção?: ")
    valor_01 = input("Qual o 1° valor?: ")
    valor_02 = input("Qual o 2° valor?: ")
    valor_01 = int(valor_01)
    valor_02 = int(valor_02)

    texto_sair = ''' 
        [1] Não, desejo sair
        [2] Sim, desejo sair e realizar outro calculo
    '''

    #Soma
    if operador == "1" or operador == "+" or operador == "Somar":
        resultado = valor_01 + valor_02
        print("Resultado da soma é:" + str(resultado))
        print(texto_sair)
        operador = input("Deseja realizar outro calculo? ")
        if operador == "1":
            executar = False
        


    #Subtração
    if operador == "2" or operador == "-" or operador == "Subtração":
        resultado = valor_01 - valor_02
        print("Resultado da subtração é: " + str(resultado))
        print(texto_sair)
        operador = input("Deseja realizar outro calculo? ")
        if operador == "2":
            executar = False
     #Dividir
    if operador == "3" or operador == "/" or operador == "Divisão":
        resultado = valor_01 / valor_02
        print("Resultado da Divisão é: " + str(resultado))
        print(texto_sair)
        operador = input("Deseja realizar outro calculo? ")
        if operador == "3":
             executar = False

    #Multiplicação
    if operador == "4" or operador == "*" or operador == "Multiplicação":
        resultado = valor_01 * valor_02
        print("Resultado da multiplicação é: " + str(resultado))
        print(texto_sair)
        operador = input("Deseja realizar outro calculo? ")
        if operador == "4":
          executar = False
    #Sair 
    if operador == "5" or operador == "Sair":
         print("Obrigado")
         executar = False
    
   