import random
import time


#Variáveis contadoras declaradas como globais 
global contComp, contTroca
contComp = 0 #contar o número de comparações
contTroc = 0 #contar o número de trocas


#Criação do Insert Sort
def insertionSort(v):
    i = 1
    global contComp  #variável contadora de comparação
    global contTroc  #variável contadora de troca

    #o i é igual a 1, pois no método insert sort, a análise dos elementos começa a partir do segundo elemento.

    while i < len(v):
        aux = v[i]
        trocar = False
        j = i - 1
        contComp += 1

        while (j >= 0 and v[j] > aux):
            contComp += 1
            v[j + 1] = v[j]
            trocar = True
            j = j - 1

        if trocar:
            v[j + 1] = aux
            contTroc += 1

        i = i + 1

#Criação do Quick Sort
def quickSort(arr):
  #Usado pra armazenar os valores para a função auxiliar
  quickSortAux(arr,0,len(arr)-1)

def quickSortAux(arr,prim,ultm):
  if prim<ultm:
    # Particionamento do arr 
    corte = particao(arr,prim,ultm)
    # Ordenação dos valores antes e depois do corte
    quickSortAux(arr,prim,corte-1)
    quickSortAux(arr,corte+1,ultm)


def particao(arr,prim,ultm):
  # Indice para o corte
  global contTroc
  pivo = arr[prim]
  # Indice dos elementos   
  esq = prim+1
  dire = ultm
  done = False
  # Loop infinito para a ordenação
  while not done:
      global contComp
      contComp += 1
      # Ordenação dos menores  
      while esq <= dire and arr[esq] <= pivo:
        esq = esq + 1
      # Ordenação dos maiores 
      while arr[dire] >= pivo and dire >= esq:
        dire = dire -1
      # verificação  
      if dire < esq:
        contTroc += 1
        done = True
      else:
        temp = arr[esq]
        arr[esq] = arr[dire]
        arr[dire] = temp
        contTroc += 1
  # Retorno no arr  
  temp = arr[prim]
  arr[prim] = arr[dire]
  arr[dire] = temp
  contTroc += 1
  # Retorno da Função
  return dire

#Criação do Radix Sort
def countingSort(arr, exp1):
    n = len(arr)
    # O array de saida com os elementos ordenados do array original
    saida = [0] * (n)
    # Inicializa o array com 0
    cont = [0] * (10)
    # Armazena as ocorrencias de cont[]
    for i in range(0, n):
        index = arr[i] // exp1
        cont[index % 10] += 1
    # Muda cont[i] para que cont[i] tenha a posição atual do digito no array de saída
    for i in range(1, 10):
        cont[i] += cont[i - 1]
    # Constroi o array de saída
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        saida[cont[index % 10] - 1] = arr[i]
        cont[index % 10] -= 1
        i -= 1
    # Copia o array de saída para arr[], para que o arr agora tenha os numeros ordenados.
    i = 0
    for i in range(0, len(arr)):
        arr[i] = saida[i]
 
# Função para fazer o Radix Sort
def radixSort(arr):
    # Encontra o maior numero para saber o número de digitos
    max1 = max(arr)
    # Faz o Counting Sort para cada digito.
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10

# Criação de Vetor aleatório e decrescente
def criarRanArr(x,a,b):
  arr = []
  num = 0
  if x > 999:
    num = 100
  ranArr = list(random.sample(range(a,b),x))
  while num != x:
    if num > 999:
      arr.append(sorted(ranArr[:num],reverse = True))
      num += 999
      if num > x:
        num = x
    else:
      arr.append(sorted(ranArr, reverse = True))
      return arr[0]
  return arr[0]

#Criação do menu de opções
#O usuário deverá escolher o método de ordenação

print("\---------Menu de opções--------/")
print("Escolha o método de ordenação:")
print("1 - Insert Sort")
print("2 - Quick Sort")
print("3 - Radix Sort")
opMet = int(input("opção -> "))

#Método de ordenação Insert Sort
if opMet == 1:

    #O usuário deverá escolher o tamanho do vetores
    print("\nTamanho do vetor:")
    print("1-10 elementos")
    print("2-100 elementos")
    print("3-1.000 elementos")
    print("4-10.000 elementos")
    print("5-100.000 elementos")
    op = int(input("opção-> "))

    #O intervalo dos valores do vetor
    print("Determine o intervalo de entrada\n")
    x = int(input("Primeiro intervalo -> "))
    n = int(input("Segundo intervalo -> "))

    print("1 - Gerar os vetores aleatoriamente")
    print("2 - Gerar vetores aleatórios decrescente")
    tipoVet = int(input("opção -> "))

    # Para criar vetores de forma aleatória, usamos o range;
    # o range((x,n),y) cria y elementos diferentes entre o intervalo de x e n
    # O usuário escolhe o intervalo desses valores
    # A criação de forma aleatória, foi feita nas demais condições

    if tipoVet == 1:
      if op == 1:
          #Para 10 elementos
          antes = time.time()
          vetor = list(random.sample(range(x, n), 10))
          print("\nNúmeros gerados aleatóriamente")
          insertionSort(vetor)
          print("\nNúmeros ordenados pelo Insert Sort")
          print(vetor)
          print(f'Comparações: {contComp}')
          print(f'Trocas: {contTroc}')
          
          #Para 100 elementos
      elif op == 2:
          antes = time.time()
          vetor = list(random.sample(range(x, n), 100))
          print("Números gerados aleatóriamente")
          print(vetor)
          insertionSort(vetor)
          print("\nNúmeros ordenados pelo Insert Sort")
          print(vetor)
        
        #Para 1000 elementos
      elif op == 3:
          antes = time.time()
          vetor = list(random.sample(range(x, n), 1000))
          print("Números gerados aleatóriamente")
          print(vetor)
          insertionSort(vetor)
          print("\nNúmeros ordenados pelo Insert Sort")
          print(vetor)

        #Para 10000 elementos
      elif op == 4:
          antes = time.time()
          vetor = list(random.sample(range(x, n), 10000))
          print("Números gerados aleatóriamente")
          print(vetor)
          insertionSort(vetor)
          print("\nNúmeros ordenados pelo Insert Sort")
          print(vetor)
    
        #Para 100000 elementos
      elif op == 5:
          antes = time.time()
          vetor = list(random.sample(range(x, n), 100000))
          print("Números gerados aleatóriamente")
          print(vetor)
          insertionSort(vetor)
          print("\nNúmeros ordenados pelo Insert Sort")
          print(vetor)
    
    
    
    elif tipoVet == 2:
    # Para criar vetores de forma aleatória, usamos o range;
    # o range((x,n),y) cria y elementos diferentes entre o intervalo de x e n
    # O usuário escolhe o intervalo desses valores
    # A criação de forma aleatória, foi feita nas demais condições

      if op == 1:
          #Para 10 elementos
          antes = time.time()
          vetor = criarRanArr(10,x,n)
          print("\nNúmeros gerados aleatóriamente")
          print(vetor)
          insertionSort(vetor)
          print("\nNúmeros ordenados pelo Insertion Sort")
          print(vetor)
          print(f'Comparações: {contComp}')
          print(f'Trocas: {contTroc}')
          
          #Para 100 elementos
      elif op == 2:
          antes = time.time()
          vetor = criarRanArr(100,x,n)
          print("Números gerados aleatóriamente")
          print(vetor)
          insertionSort(vetor)
          print("\nNúmeros ordenados pelo Insertion Sort")
          print(vetor)
        
        #Para 1000 elementos
      elif op == 3:
          antes = time.time()
          vetor = criarRanArr(1000,x,n)
          print("Números gerados aleatóriamente")
          print(vetor)
          insertionSort(vetor)
          print("\nNúmeros ordenados pelo Insertion Sort")
          print(vetor)

        #Para 10000 elementos
      elif op == 4:
          antes = time.time()
          vetor = criarRanArr(10000,x,n)
          print("Números gerados aleatóriamente")
          print(vetor)
          insertionSort(vetor)
          print("\nNúmeros ordenados pelo Insertion Sort")
          print(vetor)
    
        #Para 100000 elementos
      elif op == 5:
          antes = time.time()
          vetor = criarRanArr(100000,x,n)
          print("Números gerados aleatóriamente")
          print(vetor)
          insertionSort(vetor)
          print("\nNúmeros ordenados pelo Insetion Sort")
          print(vetor)

#Método de ordenação Quick Sort
elif opMet == 2:
  
  print("\nTamanho do vetor:")
  print("1-10 elementos")
  print("2-100 elementos")
  print("3-1.000 elementos")
  print("4-10.000 elementos")
  print("5-100.000 elementos\n")
  op = int(input("opção-> "))

  #O intervalo dos valores do vetor
  print("Determine o intervalo de entrada\n")
  x = int(input("Primeiro intervalo -> "))
  n = int(input("Segundo intervalo -> "))

  #O usuário vai escolher o tipo de entrada 
  print("1 - Gerar os vetores aleatoriamente")
  print("2 - Gerar vetores aleatórios decrescente")
  tipoVet = int(input("opção -> "))

  if tipoVet == 1:
    
    # Para criar vetores de forma aleatória, usamos o range;
    # o range((x,n),y) cria y elementos diferentes entre o intervalo de x e n
    # O usuário escolhe o intervalo desses valores
    # A criação de forma aleatória, foi feita nas demais condições

    if op == 1:
        #Para 10 elementos
        antes = time.time()
        vetor = list(random.sample(range(x, n), 10))
        print("\nNúmeros gerados aleatóriamente")
        print(vetor)
        quickSort(vetor)
        print("\nNúmeros ordenados pelo Quick Sort")
        print(vetor)
        print(f'Comparações: {contComp}')
        print(f'Trocas: {contTroc}')
        
        #Para 100 elementos
    elif op == 2:
        antes = time.time()
        vetor = list(random.sample(range(x, n), 100))
        print("Números gerados aleatóriamente")
        print(vetor)
        quickSort(vetor)
        print("\nNúmeros ordenados pelo Quick Sort")
        print(vetor)
       
       #Para 1000 elementos
    elif op == 3:
        antes = time.time()
        vetor = list(random.sample(range(x, n), 1000))
        print("Números gerados aleatóriamente")
        print(vetor)
        quickSort(vetor)
        print("\nNúmeros ordenados pelo Quick Sort")
        print(vetor)

       #Para 10000 elementos
    elif op == 4:
        antes = time.time()
        vetor = list(random.sample(range(x, n), 10000))
        print("Números gerados aleatóriamente")
        print(vetor)
        quickSort(vetor)
        print("\nNúmeros ordenados pelo Quick Sort")
        print(vetor)
  
       #Para 100000 elementos
    elif op == 5:
        antes = time.time()
        vetor = list(random.sample(range(x, n), 100000))
        print("Números gerados aleatóriamente")
        print(vetor)
        quickSort(vetor)
        print("\nNúmeros ordenados pelo Quick Sort")
        print(vetor)


  elif tipoVet == 2:
    if op == 1 :
      antes = time.time()
      arr = criarRanArr(10,x,n)
      #Print Array original
      print("\nNumeros gerados aleatoriamente: ")
      for i in arr: print(i,end='-')
      #Divisão do array para superar o erro de memoria
      if len(arr) < 997:
        quickSort(arr)
        arr2=arr
        aux=True
      else: 
        x = 0
        arr2 = []
        while x != len(arr):
          aux = []
          aux.append(arr[x:x+900])
          quickSort(aux[0])
          arr2.insert(0,aux[0])
          x += 900
          if x > len(arr):
            aux.append(arr[x-900:])
            quickSort(aux[0])
            arr2.insert(0, aux[0])
            x = len(arr)
            arr2.pop(0)
      #Print do Array ordenado
      print("\nNumeros ordenados pelo Quick Sort")
      if aux:
        for i in arr2: print(i, end='-')
      else:
        for i in arr2: 
          for j in i: 
            print(j,end='-')
      # Exibição das Comparações e Trocas      
      print(f'\nComparações: {contComp}')
      print(f'Trocas: {contTroc}')
    elif op == 2 :
      antes = time.time() 
      arr = criarRanArr(100,x,n)
      #Print Array original
      print("\nNumeros gerados aleatoriamente: ")
      for i in arr: print(i,end='-')
      #Divisão do array para superar o erro de memoria
      if len(arr) < 997:
        quickSort(arr)
        arr2=arr
        aux=True
      else: 
        x = 0
        arr2 = []
        while x != len(arr):
          aux = []
          aux.append(arr[x:x+900])
          quickSort(aux[0])
          arr2.insert(0,aux[0])
          x += 900
          if x > len(arr):
            aux.append(arr[x-900:])
            quickSort(aux[0])
            arr2.insert(0, aux[0])
            x = len(arr)
            arr2.pop(0)
      #Print do Array ordenado
      print("\nNumeros ordenados pelo Quick Sort")
      if aux:
        for i in arr2: print(i, end='-')
      else:
        for i in arr2: 
          for j in i: 
            print(j,end='-')
      # Exibição das Comparações e Trocas      
      print(f'\nComparações: {contComp}')
      print(f'Trocas: {contTroc}')
    elif op == 3 :
      antes = time.time()
      arr = criarRanArr(1000,x,n)
      #Print Array original
      print("\nNumeros gerados aleatoriamente: ")
      for i in arr: print(i,end='-')
      #Divisão do array para superar o erro de memoria
      if len(arr) < 997:
        quickSort(arr)
        arr2=arr
        aux=1
      else: 
        x = 0
        arr2 = []
        while x != len(arr):
          aux = []
          aux.append(arr[x:x+900])
          quickSort(aux[0])
          arr2.insert(0,aux[0])
          x += 900
          if x > len(arr):
            aux.append(arr[x-900:])
            quickSort(aux[0])
            arr2.insert(0, aux[0])
            x = len(arr)
            arr2.pop(0)
      #Print do Array ordenado
      print("\nNumeros ordenados pelo Quick Sort")
      if aux == 1:
        for i in arr2: print(i, end='-')
      else:
        for i in arr2: 
          for j in i: 
            print(j,end='-')
      # Exibição das Comparações e Trocas      
      print(f'\nComparações: {contComp}')
      print(f'Trocas: {contTroc}')

    elif op == 4 :
      antes = time.time()
      arr = criarRanArr(10000,x,n)
      #Print Array original
      print("\nNumeros gerados aleatoriamente: ")
      for i in arr: print(i,end='-')
      #Divisão do array para superar o erro de memoria
      if len(arr) < 997:
        quickSort(arr)
        arr2=arr
        aux=1
      else: 
        x = 0
        arr2 = []
        while x != len(arr):
          aux = []
          aux.append(arr[x:x+900])
          quickSort(aux[0])
          arr2.insert(0,aux[0])
          x += 900
          if x > len(arr):
            aux.append(arr[x-900:])
            quickSort(aux[0])
            arr2.insert(0, aux[0])
            x = len(arr)
            arr2.pop(0)
      #Print do Array ordenado
      print("\nNumeros ordenados pelo Quick Sort")
      if aux == 1:
        for i in arr2: print(i, end='-')
      else:
        for i in arr2: 
          for j in i: 
            print(j,end='-')
      # Exibição das Comparações e Trocas      
      print(f'\nComparações: {contComp}')
      print(f'Trocas: {contTroc}')

    elif op == 5 :
      antes = time.time()
      arr = criarRanArr(100000,x,n)
      #Print Array original
      print("\nNumeros gerados aleatoriamente: ")
      for i in arr: print(i,end='-')
      #Divisão do array para superar o erro de memoria
      if len(arr) < 997:
        quickSort(arr)
        arr2=arr
        aux=1
      else: 
        x = 0
        arr2 = []
        while x != len(arr):
          aux = []
          aux.append(arr[x:x+900])
          quickSort(aux[0])
          arr2.insert(0,aux[0])
          x += 900
          if x > len(arr):
            aux.append(arr[x-900:])
            quickSort(aux[0])
            arr2.insert(0, aux[0])
            x = len(arr)
            arr2.pop(0)
      #Print do Array ordenado
      print("\nNumeros ordenados pelo Quick Sort")
      if aux == 1:
        for i in arr2: print(i, end='-')
      else:
        for i in arr2: 
          for j in i: 
            print(j,end='-')
      # Exibição das Comparações e Trocas      
      print(f'\nComparações: {contComp}')
      print(f'Trocas: {contTroc}')

#Método Radix Sort
elif opMet == 3:
  
  #O usuário deverá escolher o tamanho do vetores
    print("\nTamanho do vetor:")
    print("1-10 elementos")
    print("2-100 elementos")
    print("3-1.000 elementos")
    print("4-10.000 elementos")
    print("5- 100.000 elementos")
    op = int(input("opção-> "))

    #O intervalo dos valores do vetor
    print("Determine o intervalo de entrada\n")
    x = int(input("Primeiro intervalo -> "))
    n = int(input("Segundo intervalo -> "))

    print("1 - Gerar os vetores aleatoriamente")
    print("2 - Gerar vetores aleatórios decrescente")
    tipoVet = int(input("opção -> "))

    # Para criar vetores de forma aleatória, usamos o range;
    # o range((x,n),y) cria y elementos diferentes entre o intervalo de x e n
    # O usuário escolhe o intervalo desses valores
    # A criação de forma aleatória, foi feita nas demais condições


    if tipoVet == 1:
      if op == 1:
          #Para 10 elementos
          antes = time.time()
          vetor = list(random.sample(range(x, n), 10))
          print("\nNúmeros gerados aleatóriamente")
          print(vetor)
          radixSort(vetor)
          print("\nNúmeros ordenados pelo Radix Sort")
          print(vetor)
          print(f'\nComparações: Radix não é baseado em comparações')
          print(f'\nTrocas: Radix não é baseado em trocas')
          
          #Para 100 elementos
      elif op == 2:
          antes = time.time()
          vetor = list(random.sample(range(x, n), 100))
          print("Números gerados aleatóriamente")
          print(vetor)
          radixSort(vetor)
          print("\nNúmeros ordenados pelo Radix Sort")
          print(vetor)
          print(f'\nComparações: Radix não é baseado em comparações')
          print(f'\nTrocas: Radix não é baseado em trocas')
        
        #Para 1000 elementos
      elif op == 3:
          antes = time.time()
          vetor = list(random.sample(range(x, n), 1000))
          print("Números gerados aleatóriamente")
          print(vetor)
          radixSort(vetor)
          print("\nNúmeros ordenados pelo Radix Sort")
          print(vetor)
          print(f'\nComparações: Radix não é baseado em comparações')
          print(f'\nTrocas: Radix não é baseado em trocas')        

        #Para 10000 elementos
      elif op == 4:
          antes = time.time()
          vetor = list(random.sample(range(x, n), 10000))
          print("Números gerados aleatóriamente")
          print(vetor)
          radixSort(vetor)
          print("\nNúmeros ordenados pelo Radix Sort")
          print(vetor)
          print(f'\nComparações: Radix não é baseado em comparações')
          print(f'\nTrocas: Radix não é baseado em trocas')
        #Para 100000 elementos
      elif op == 5:
          antes = time.time()
          vetor = list(random.sample(range(x, n), 100000))
          print("Números gerados aleatóriamente")
          print(vetor)
          radixSort(vetor)
          print("\nNúmeros ordenados pelo Radix Sort")
          print(vetor)
          print(f'\nComparações: Radix não é baseado em comparações')
          print(f'\nTrocas: Radix não é baseado em trocas')
    elif tipoVet == 2:
      if op == 1:
          #Para 10 elementos
          antes = time.time()
          vetor = criarRanArr(10,x,n)
          print("\nNúmeros gerados aleatóriamente")
          print(vetor)
          radixSort(vetor)
          print("\nNúmeros ordenados pelo Radix Sort")
          print(vetor)
          print(f'\nComparações: Radix não é baseado em comparações')
          print(f'\nTrocas: Radix não é baseado em trocas')
          
          #Para 100 elementos
      elif op == 2:
          antes = time.time()
          vetor = criarRanArr(100,x,n)
          print("Números gerados aleatóriamente")
          print(vetor)
          radixSort(vetor)
          print("\nNúmeros ordenados pelo Radix Sort")
          print(vetor)
          print(f'\nComparações: Radix não é baseado em comparações')
          print(f'\nTrocas: Radix não é baseado em trocas')
        
        #Para 1000 elementos
      elif op == 3:
          antes = time.time()
          vetor = criarRanArr(1000,x,n)
          print("Números gerados aleatóriamente")
          print(vetor)
          radixSort(vetor)
          print("\nNúmeros ordenados pelo Radix Sort")
          print(vetor)
          print(f'\nComparações: Radix não é baseado em comparações')
          print(f'\nTrocas: Radix não é baseado em trocas')        

        #Para 10000 elementos
      elif op == 4:
          antes = time.time()
          vetor = criarRanArr(10000,x,n)
          print("Números gerados aleatóriamente")
          print(vetor)
          radixSort(vetor)
          print("\nNúmeros ordenados pelo Radix Sort")
          print(vetor)
          print(f'\nComparações: Radix não é baseado em comparações')
          print(f'\nTrocas: Radix não é baseado em trocas')
        #Para 100000 elementos
      elif op == 5:
          antes = time.time()
          vetor = criarRanArr(100000,x,n)
          print("Números gerados aleatóriamente")
          print(vetor)
          radixSort(vetor)
          print("\nNúmeros ordenados pelo Radix Sort")
          print(vetor)
          print(f'\nComparações: Radix não é baseado em comparações')
          print(f'\nTrocas: Radix não é baseado em trocas')
          


# Para saber o tempo que o sistema levou para rodar o código
# utilizaremos a biblioteca time
depois = time.time()
tempoTotal = depois - antes
print(f'\nO tempo decorrido foi: {tempoTotal:.5f}s')