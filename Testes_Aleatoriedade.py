from collections import Counter
from BitVector import BitVector
import pandas as pd

Caminho_Arquivo = 'Matrix2.txt'
Dados_Arquivo = pd.read_csv(Caminho_Arquivo, sep="'", header=None)
Dados_Arquivo = Dados_Arquivo.drop(columns=[0, 2])
Dados_Arquivo = pd.DataFrame([f"{BitVector(hexstring = linha)}" for linha in Dados_Arquivo[1]])

Contador_Poker = 1
Contador_Monobit = 1
Contador_Long_Run_Test = 1
Contador_Long_Test = 1

#######################################################################################################

def PokerTest(chave):
    
    global Contador_Poker
    Contador_Chave = []
    Contador = []
    Nibble = ''
    Nibble_Chave = {}          
    Total_Nibble_Chave = []
    i = 0
    
    for Valor in chave:
        if i == 4:
            Contador.append(Nibble)
            i = 0
            Nibble = ''
        Nibble = Nibble + Valor
        i = i + 1
        
    Contador_Chave.append(Contador)
    Contador = []
    Contador_Chave = pd.DataFrame(Contador_Chave)
    
    Nibbles = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111',]
    
    for chave in Contador_Chave.values:           
        for Nibble in Nibbles:
            c = Counter(chave)
            Nibble_Chave[Nibble] = c[Nibble]
        Total_Nibble_Chave.append(Nibble_Chave)
        Nibble_Chave = {}
        
    Total_Nibble_Chave = pd.DataFrame(Total_Nibble_Chave)
    Soma_Chaves = []
    Acumulado = 0
    Conta = 0

    for chave in Total_Nibble_Chave.values:
        for Valor in chave:
            Acumulado = Acumulado + Valor * Valor
        Conta = (16/5000) * Acumulado - 5000
        Soma_Chaves.append(Conta)
        Conta = 0
        Acumulado = 0
        
    Soma_Chaves = pd.DataFrame(Soma_Chaves)
    Verificacao = 0
    
    for chave in Soma_Chaves.values:
        if chave > 1.03 and chave < 57.4:
            Verificacao = Verificacao + 1
    
    if(Verificacao == 0):
        print('CHAVE >> {} << - NÃO - POKER'.format(Contador_Poker))
        Contador_Poker = Contador_Poker +1
    else:
        print('CHAVE >> {} << - SIM - POKER'.format(Contador_Poker))
        Contador_Poker = Contador_Poker +1

#######################################################################################################

def MonobitTest(chave):
    
    global Contador_Monobit
    Contador = []
    Verificacao = 0
    
    c = Counter(chave)
    Contador.append(c['1'])
        
    for item in Contador:
        if item > 9654 and item < 10346:
            Verificacao = Verificacao + 1
   
    if(Verificacao == 0):
        print('CHAVE >> {} << - NÃO - MONOBIT'.format(Contador_Monobit))
        Contador_Monobit = Contador_Monobit +1
    else:
        print('CHAVE >> {} << - SIM - MONOBIT'.format(Contador_Monobit))
        Contador_Monobit = Contador_Monobit +1
        
#######################################################################################################

def LongRunTest(chave):
    
    global Contador_Long_Run_Test
    Contador_Chave = []
    Contador = []
    Atual = ''
    i = 0

    for item in chave:
        if Atual == '':
            Atual = item
        else:  
            if item == Atual:
                i = i + 1
            else:
                Contador.append(i)
                i = 0
                Atual = item
                
    Contador_Chave.append(Contador)
    Contador = []
    Atual = ''
    Contador_Chave = pd.DataFrame(Contador_Chave)
    Verificacao = 0
    
    for Contador in Contador_Chave.values:
        if len(Contador[Contador > 33]) == 0:
            Verificacao = Verificacao + 1
   
    if(Verificacao == 0):
        print('CHAVE >> {} << - NÃO - LONG RUN'.format(Contador_Long_Run_Test))
        Contador_Long_Run_Test = Contador_Long_Run_Test +1
    else:
        print('CHAVE >> {} << - SIM - LONG RUN'.format(Contador_Long_Run_Test))
        Contador_Long_Run_Test = Contador_Long_Run_Test +1         

#######################################################################################################

def RunTest(chave):
    
    global Contador_Long_Test
    Contador_label = {'1': 0,'2': 0,'3': 0,'4': 0,'5': 0,'6': 0,}
    Contador_Chave = []
    Atual = ''
    i = 0
  
    for item in chave:
        if Atual == '':
            Atual = item
            i = i + 1
        else:  
            if item == Atual:
                i = i + 1
            else:
                if i >= 6:
                    Contador_label['6'] = Contador_label['6'] + 1
                if i == 5:
                    Contador_label['5'] = Contador_label['5'] + 1
                if i == 4:
                    Contador_label['4'] = Contador_label['4'] + 1
                if i == 3:
                    Contador_label['3'] = Contador_label['3'] + 1
                if i == 2:
                    Contador_label['2'] = Contador_label['2'] + 1
                if i == 1:
                    Contador_label['1'] = Contador_label['1'] + 1
                i = 0
                Atual = item

    Contador_Chave.append(Contador_label)
    Atual = ''
    Contador_Chave = pd.DataFrame(Contador_Chave)

    Cont = 0

    for Contador in Contador_Chave.values:
        if Contador[5] < 90 or Contador[5] > 223:
            Cont = Cont + 1
        elif Contador[4] < 90 or Contador[4] > 223:
            Cont = Cont + 1
        elif Contador[3] < 223 or Contador[3] > 402:
            Cont = Cont + 1
        elif Contador[2] < 502 or Contador[2] > 748:
            Cont = Cont + 1
        elif Contador[1] < 1079 or Contador[1] > 1421:
            Cont = Cont + 1
        elif Contador[0] < 2267 or Contador[0] > 2733:
            Cont = Cont + 1
    
    if(i == 0):
        print('CHAVE >> {} << - NÃO - RUN'.format(Contador_Long_Test))
        Contador_Long_Test = Contador_Long_Test +1
    else:
        print('CHAVE >> {} << - SIM - RUN'.format(Contador_Long_Test))
        Contador_Long_Test = Contador_Long_Test +1     

#######################################################################################################

def main():
    print("Os testes de aleatoriedade estão ordenados em cada chave da seguinte forma: 1 - The Poker Test, 2 - The Monobit Test, 3 - The Long Run Test, 4 - The Run Test\n")
    for x in range(len(Dados_Arquivo)):
        PokerTest(Dados_Arquivo[0][x])
        MonobitTest(Dados_Arquivo[0][x])
        LongRunTest(Dados_Arquivo[0][x])
        RunTest(Dados_Arquivo[0][x])
        print('\n')

#######################################################################################################
        
main()

