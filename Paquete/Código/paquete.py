import math
import sys
import numpy as np

def Menu_principal():
  opcion_principal=-1

  while opcion_principal<=0 or opcion_principal>4:
    print("Menu de Calculos del programa\n")
    print("1. Calcular raices de funciones")
    print("2. Caldular el determinante y soluucion de una matriz mediante el metodo de Gauss")
    print("3. Calcular la solucion y determinante de una matriz por el metodo de Jacobi")
    print("4. Factorización de Cholesky y método de potencias")
    print("5. Salir del ejecutable")

    opcion_principal=input("\n¿Que deseas hacer?")
    opcion_principal=int(opcion_principal)
    print("")
    if opcion_principal==1:
      Menu()
    if opcion_principal==2:
      funcion_matricial()
    if opcion_principal==3:
      funcion_matricial_2()
    if opcion_principal==4:
      Submenu()
    if opcion_principal==5:
      print("¡Nos vemos usuario!")
      sys.exit()
def Funcion_1(x):
  y=x*x*math.cos(x)-2*x
  return y;

def Funcion_1_1(x):
  y=2*x*math.cos(x)-x*x*math.sin(x)-2
  return y;

def Funcion_2(x):
  if x==0:
    print("No es posible hacer la division entre 0, vuelve a intentarlo con otro punto.")
    sys.exit()
  y=((6-2/(x*x))*math.exp(2+x))/4+1
  return y;

def Funcion_2_2(x):
  if x==0:
    print("No es posible hacer la division entre 0, vuelve a intentarlo con otro punto.")
    sys.exit()
  y= (math.exp(x+2)*(3*x*x*x-x+2))/(2*x*x*x)
  return y;



def Funcion_3(x):
  y=x*x*x-3*math.sin(x*x)+1
  return y;

def Funcion_3_3(x):
  y=3*x*x-6*x*math.cos(x*x)
  return y;



def Funcion_4(x):
  y=x*x*x+6*x*x+9.4*x+2.5
  return y;

def Funcion_4_4(x):
  y=3*x*x+12*x+(47/5)
  return y;



def Menu():
  opcion=-1
  opcion_2=-1

  while opcion<=0 or opcion>4:

    print("Menu de los Metodos")
    print("1. Pocision Falsa")
    print("2. Newton-Raphson")
    print("3. La Secante")
    print("4.Regresar al Menu Principal")

    opcion=input("¿Cual metodo o accion deseas hacer? ")
    opcion= int(opcion)
    print(" ")
  if opcion==4:
    Menu_principal()


 
  while opcion_2<=0 or opcion_2>4:

    print("Menu de funciones")
    print("1. x*xcos(x)-2x")
    print("2. ((6-2/x^2)e^2+x)/4+1")
    print("3. x^3-3sen(x^2)+1")
    print("4. x^3+6x^2+9.4x+2.5")  
    print(" ")

    opcion_2= input("¿Cual funcion quieres calcular? ")
    opcion_2= int(opcion_2)


    print(" ")
  
  if opcion==1:
    posicion_falsa(opcion_2)
  if opcion==2:
    Newton_Raphson(opcion_2)
  if opcion==3:
    Secante(opcion_2)
def posicion_falsa(opcion_2):
  OPCION=1

  while OPCION==1:
    Absoluto =1
    Relativo =1
    Porcentual =1
    parametro_superior=1



    a = float(input("Introduce el primer numero del intervalo: "))
    b = float(input("Introduce el segundo numero del intervalo: "))

    print("1. Error Absoluto")
    print("2. Error Relativo")
    print("3. Error Relativo Porcentual")

    opcion=input("¿Cual quieres que sea tu condicion de parada? ")
    opcion=int(opcion)

    parametro_Inferior = float(input("¿Cual quieres que sea tu tolerancia: "))


    i=0 #Variable de control
    reserva_c=0


    while parametro_Inferior<parametro_superior and i<100:
      #Variables
      if opcion_2==1:
        f_a = Funcion_1(a)
        f_b = Funcion_1(b)
      if opcion_2==2:
        f_a = Funcion_2(a)
        f_b = Funcion_2(b)
      if opcion_2==3:
        f_a = Funcion_3(a)
        f_b = Funcion_3(b)
      if opcion_2==4:
        f_a = Funcion_4(a)
        f_b = Funcion_4(b)

      c = b-f_b*((a-b)/(f_a-f_b))

      #Calculo de Errores
      Absoluto = abs((c-reserva_c)) #Calculo del error
      Relativo= Absoluto/abs(c)
      Porcentual= Relativo*100


      reserva_c=c
      if opcion_2==1:
        f_c = Funcion_1(c)
      if opcion_2==2:
        f_c = Funcion_2(c)
      if opcion_2==3:
        f_c = Funcion_3(c)
      if opcion_2==4:
        f_c = Funcion_4(c)

      if f_c*f_a<0:
        b=c

      if f_c*f_a>0:
        a=c
      

      print("Iteracion numero : ",i)
      print("La aproximacion es: ",c)
      print("La evaluacion es: ",f_c)

      i=i+1
      if opcion==1:
        parametro_superior= Absoluto
        if i>0:
          print("El error es  ", Absoluto)
        print(" ")
      if opcion==2:
        parametro_superior= Relativo
        if i>0:
          print("El error es  ", Relativo)
          print(" ")
      if opcion==3:
        parametro_superior= Porcentual
        if i>0:
          print("El error es  %", Porcentual)
          print(" ")
    print("La raiz de la funcion buscada es: ",c)
 
    print(" ")
    print("Opciones")
    print("1. Calcular una nueva raiz de esta ecuacion")
    print("2. Salir al Menu de metodos")
    print("3. Salir del programa")
    print(" ")
    OPCION = int(input("¿Que deseas hacer? "))
    print(" ")
  if OPCION==2:
    Menu()
  if OPCION==3:
    print("¡¡Hasta luego!!")
    exit()
def Newton_Raphson(opcion_2):
  OPCION=1

  while OPCION==1:
    Absoluto =1
    Relativo =1
    Porcentual =1
    parametro_superior=1

    x = float(input("Introduce el numero: "))

    print("1. Error Absoluto")
    print("2. Error Relativo")
    print("3. Error Relativo Porcentual")

    opcion=input("¿Cual quieres que sea tu condicion de parada? ")
    opcion=int(opcion)

    parametro_Inferior = float(input("¿Cual quieres que sea tu tolerancia: "))


    i=0 #Variable de control


    while parametro_Inferior<parametro_superior and i<100:
      #Variables
      if opcion_2==1:
        f_x = Funcion_1(x)
        f_dx = Funcion_1_1(x)

        if f_dx==0:
          print("Lo siento, hay una divisón entre cero, debo de cerrar el programa, abrelo e intentalo con otro método ")
          sys.exit()


      if opcion_2==2:
        f_x = Funcion_2(x)
        f_dx = Funcion_2_2(x)

        if f_dx==0:
          print("Lo siento, hay una divisón entre cero, debo de cerrar el programa, abrelo e intentalo con otro método ")
          sys.exit()


      if opcion_2==3:
        f_x = Funcion_3(x)
        f_dx = Funcion_3_3(x)
        
        if f_dx==0:
          print("Lo siento, hay una divisón entre cero, debo de cerrar el programa, abrelo e intentalo con otro método ")
          sys.exit()


      if opcion_2==4:
        f_x = Funcion_4(x)
        f_dx = Funcion_4_4(x)

        if f_dx==0:
            print("Lo siento, hay una divisón entre cero, debo de cerrar el programa, abrelo e intentalo con otro método ")
            sys.exit()

      a=x

      x=x-f_x/f_dx

      if x==0 and opcion>1:      
       print("Hay una división entre cero, intenta con otro punto y/o con otro tipo de error: ")
       sys.exit()

      #Calculo de Errores
      Absoluto = abs((a-x)) #Calculo del error
      Relativo= Absoluto/abs(x)
      Porcentual= Relativo*100
   

      print("Iteracion numero : ",i)

      if 0<i:
        print("La aproximacion es: ",x)
      print("La evaluacion es: ",f_x)

      i=i+1

      if opcion==1:
        parametro_superior= Absoluto
        if i>0:
          print("El error es  ", Absoluto)
        print(" ")
      if opcion==2:
        parametro_superior= Relativo
        if i>0:
          print("El error es  ", Relativo)
          print(" ")
      if opcion==3:
        parametro_superior= Porcentual
        if i>0:
          print("El error es  %", Porcentual)
          print(" ")
    print("La raiz de la funcion buscada es: ",x)
    print(" ")
    print("Opciones")
    print("1. Calcular una nueva raiz de esta ecuacion")
    print("2. Salir al Menu de metodos")
    print("3. Salir del programa")
    print(" ")
    OPCION = int(input("¿Que deseas hacer? "))
    print(" ")
  if OPCION==2:
    Menu()
  if OPCION==3:
    print("¡¡Hasta luego!!")
    exit()
    
def Secante(opcion_2):
  OPCION=1

  while OPCION==1:
    Absoluto =1
    Relativo =1
    Porcentual =1
    parametro_superior=1

    x_0= float(input("Dame el valor inicial de x: "))
    x_1= float(input("Dame el valor final de x: "))

    print("1. Error Absoluto")
    print("2. Error Relativo")
    print("3. Error Relativo Porcentual")

    opcion=input("¿Cual quieres que sea tu condicion de parada? ")
    opcion=int(opcion)

    parametro_Inferior = float(input("¿Cual quieres que sea tu tolerancia: "))
    i=0 #Variable de control

    while parametro_Inferior<parametro_superior and i<100:
      if opcion_2==1:
        f_x0= Funcion_1(x_0)
        f_x1= Funcion_1(x_1)
      if opcion_2==2:
        f_x0= Funcion_2(x_0)
        f_x1= Funcion_2(x_1)
      if opcion_2==3:
        f_x0= Funcion_3(x_0)
        f_x1= Funcion_3(x_1)
      if opcion_2==4:
        f_x0= Funcion_4(x_0)
        f_x1= Funcion_4(x_1)

      if (f_x1-f_x0)==0 or f_x1==0 and f_x0==0:
        print("Hay una división entre cero, intenta con otro punto y/o con otro tipo de error: ")
        sys.exit()


      a=x_1 
      x_1= x_1- f_x1*(x_0-x_1)/(f_x0-f_x1)
      x_0=a

      if x_1==0 and opcion>1:
        print("Hay una división entre cero, intenta con otro punto y/o con otro tipo de error")
        sys.exit()

      Absoluto= abs((x_0-x_1))
      Relativo= Absoluto/abs(x_1)
      Porcentual= Relativo*100

      print("Iteracion numero : ",i)
      print("La aproximacion es: ",x_1)
      print("La evaluacion es: ",f_x1)

      i=i+1
      if opcion==1:
        parametro_superior= Absoluto
        print("El error es  ", Absoluto)
        print(" ")
      if opcion==2:
        parametro_superior= Relativo
        print("El error es  ", Relativo)
        print(" ")
      if opcion==3:
        parametro_superior= Porcentual
        print("El error es  %", Porcentual)
        print(" ")
    print("La raiz de la funcion buscada es: ",x_1)
    print(" ")
    print("Opciones")
    print("1. Calcular una nueva raiz de esta ecuacion")
    print("2. Salir al Menu de metodos")
    print("3. Salir del programa")
    print(" ")
    OPCION = int(input("¿Que deseas hacer? "))
    print(" ")
  if OPCION==2:
    Menu()
  if OPCION==3:
    print("¡¡Hasta luego!!")
    exit()





#COMIENZO DEL PROGRAMA 2
def funcion_matricial():
  columnas=0
  Bucle =1
  matriz=[]
  vector= []
  matriz_reserva=[]

  while columnas==0:
    columnas= int(input("¿De cuantas dimensiones quieres que sea tu matriz cuadrada? "))
    filas= columnas
    if columnas ==0:
      print("Oh no!, lo siento no puedo calcular una matriz tan grande.\nPor favor inserta un numero diferente\n")
 
  for i in range(filas):
    matriz.append([0]*columnas)
    
  for r in range(1):
    matriz_reserva.append([0]*columnas)

  #Llenar valores de la matriz y el vector
  print("\nDatos del Vector independiente")
  print("Indicaciones: Por favor, inserte los valores del vector.")
  for r in range(filas):
    variable_de_almacenamiento= float(input("Valor del vector z[%d]: " %(r)))
    vector.append(variable_de_almacenamiento)

  #Imprimir valores del vector
  print("Tu vector es: ")
  for z in range(filas):
    print("[%g]" %(vector[z]))

  print("\nDatos de la Matriz")
  print("Indicaciones: Por favor, inserta los valores de la matriz\n")
  for f in range(filas):
    for c in range(columnas):
      x=f
      y=c
      matriz[f][c]= float(input("Elemento a[%d][%d]: " %(x,y)))
  print("")
  print("\tTu matriz es: ")
  for fila in matriz:
      for valor in fila:
          print("\t", valor, end=" ")
      print()


  print("1. Si")
  print("2. No")
  correccion= int(input("¿Deseas hacer alguna correccion en tu matriz? "))
  while Bucle==1:

    if correccion == 1:
        x= int(input("Dame el numero de fila del elemento a corregir: "))
        y=int(input("Dame la columna: "))
        matriz[x][y]= float(input("Ahora introduce el numero: "))
        print("Tu matriz ahora es: ")
        for fila in matriz:
            for valor in fila:
                print("\t", valor, end=" ")
            print()
        print("1. Si")
        print("2. No")

        correccion=int(input("¿Deseas hacer alguna otra correccion? "))
    if correccion == 2:
        Bucle=0

    if correccion !=1 and correccion !=2:
        print("No has seleccionado ninguna opcion, ¡hasta luego!\n")
        sys.exit()

  f=0
  c=0
  reserva_c=c
  #Triangular

  for f in range(filas-1):

    almacenamiento_temporal=f

    if matriz[f][c] !=0:
      Elemen_p=matriz[f][c]
      Elemen_p=-(1/Elemen_p)
      doble_f=f
      f_vectorial=f #apunta a la fila en la que se encuentra la constante vectorial
      for c in range(columnas):
        #Almacenar el renglon
        matriz_reserva[0][c]=matriz[f][c]

      c=almacenamiento_temporal
      f=almacenamiento_temporal


      for f in range (filas):
        if ((matriz [f][c]!= 0) and (f !=doble_f)and (f>=almacenamiento_temporal)):
          k=matriz[f][c]
          for c in range(columnas):
            matriz[f][c]= k*Elemen_p*matriz_reserva[0][c]+matriz[f][c]
            if c+1==columnas:
              vector[f]= k*Elemen_p*vector[f_vectorial]+vector[f]

          c= almacenamiento_temporal
    
    f=almacenamiento_temporal
    c=almacenamiento_temporal +1
  f=0
  c=0
  Valores_del_determinante=[]
  anterior_filas=filas-1

  for c in range(columnas):
    Valores_del_determinante.append(matriz[f][c])
    f=f+1

  for i in range (anterior_filas):
    Valores_del_determinante[i+1]= Valores_del_determinante[i]*Valores_del_determinante[i+1]

  print("El determinante de la matriz es: %g" %(Valores_del_determinante[anterior_filas]))
  determinante= Valores_del_determinante[anterior_filas]

  #Casos finales

  if determinante ==0:
    print("Lo siento, tu sistema de ecuaciones no tiene solucion, intenta con nuevos coeficientes")
    sys.exit()

  if determinante != 0:
    #Aqui pondremos el algoritmo
    print("La solucion del sistema de ecuaciones es:")
    print("")
    f=filas-1
    Espacio_Solucion=[]
    while f>=0:
      i=0
      c=columnas-1
      if f==filas-1:
        variable_global= matriz[f][c]
        espacio_n= vector[f]/variable_global
        Espacio_Solucion.append(espacio_n)
        contador_i=0
        bandera=1

      while c>=0 and i<=contador_i and bandera==0:
        variable_global= matriz[f][c]
        vector[f]=vector[f]-variable_global*Espacio_Solucion[i]
        c=c-1
        i=i+1
        if i>contador_i:
          contador_i=contador_i+1
          variable_global=matriz[f][c]
          espacio_n= vector[f]/variable_global
          Espacio_Solucion.append(espacio_n)
          bandera=1 #forzar la detencion del while1

      bandera=0
      f=f-1  

    i=filas-1
    contador=1
    while i>=0:
      if Espacio_Solucion[i]==-0:
        print("x[%d]= 0" %(contador))
      if Espacio_Solucion[i] !=-0:
        print("x[%d]= %g" %(contador, Espacio_Solucion[i]))

      i=i-1
      contador= contador+1
    opcion_alternativa=0

    while opcion_alternativa<=1 or opcion_alternativa>2:
      print("\n\n1. Si")
      print("2. No")
      opcion_alternativa=input("¿Deseas regresar al menu principal?")
      opcion_alternativa=int(opcion_alternativa)

      if opcion_alternativa==1:
        Menu_principal()
      if opcion_alternativa==2: 
        print("Nos vemos usuario!\n")
        sys.exit()






#COMIENZO DEL PROGRAMA 3
def funcion_matricial_2():
  columnas =0
  determinante=0
  Bucle =1
  Error=0
  matriz =[]
  vector =[]
  while columnas==0:
    columnas= int(input("¿De cuantas dimensiones quieres que sea tu matriz cuadrada? "))
    filas= columnas
    if columnas ==0:
      print("Oh no!, lo siento no puedo calcular una matriz tan grande.\nPor favor inserta un numero diferente\n")
 
  for i in range(filas):
    matriz.append([0]*columnas)

  #Llenar valores de la matriz y el vector
  print("\nDatos del Vector independiente")
  print("Indicaciones: Por favor, inserte los valores del vector.")
  for r in range(filas):
    variable_de_almacenamiento= float(input("Valor del vector z[%d]: " %(r)))
    vector.append(variable_de_almacenamiento)

  #Imprimir valores del vector
  print("Tu vector es: ")
  for z in range(filas):
    print("[%g]" %(vector[z]))

  print("\nDatos de la Matriz")
  print("Indicaciones: Por favor, inserta los valores de la matriz\n")
  for f in range(filas):
    for c in range(columnas):
      x=f
      y=c
      matriz[f][c]= float(input("Elemento a[%d][%d]: " %(x,y)))
  print("")
  print("\tTu matriz es: ")
  for fila in matriz:
      for valor in fila:
          print("\t", valor, end=" ")
      print()

 #Correccion de datos   
  print("1. Si")
  print("2. No")
  correccion= int(input("¿Deseas hacer alguna correccion en tu matriz? "))
  while Bucle==1:

    if correccion == 1:
      while Error==0:
        x= int(input("Dame el numero de fila del elemento a corregir: "))
        y=int(input("Dame la columna: "))

        if (x>columnas-1 or y>filas-1):
          print("Lo siento, te estas saliendo del rango de la matriz, porfavor vuelve a introducir los valores")
        if x<=columnas-1 and y<=filas-1:
          Error=1
      matriz[x][y]= float(input("Ahora introduce el numero: "))
      print("Tu matriz ahora es: ")
      for fila in matriz:
          for valor in fila:
              print("\t", valor, end=" ")
          print()
      print("1. Si")
      print("2. No")

      correccion=int(input("¿Deseas hacer alguna otra correccion? "))
    if correccion == 2:
      Bucle=0
      Error=0

    if correccion !=1 and correccion !=2:
      print("No has seleccionado ninguna opcion, ¡hasta luego!\n")
      sys.exit()

  determinante =np.linalg.det(matriz) 

  if determinante ==0:
    print("Lo siento, tu matriz no tiene solucion")
    sys.exit()

  print("\nEl Determinante de tu matriz es: %g" %(determinante))

  lista_verificacion=[]
  Flor=0
  for i in range(filas):
    bandera=0
    nota=0
    sumatorio=0
    for a in range(columnas):
      #Recolectar los datos
      if i==a:
        x=matriz[i][a]
      if i !=a:
        variable_momentanea=matriz[i][a]
        variable_momentanea=abs(variable_momentanea)
        lista_verificacion.append(variable_momentanea) 
        bandera=bandera+1 
     #Hacer el sumatorio
    for nota in lista_verificacion:
      sumatorio +=nota
    #verificar EDD
    if sumatorio>=x:
      Flor=1
      
    #Si cumple la condicion, que borre los elementos anteriormente almacenados y repita con las siguientes filas
    sumatorio=0
    for a in range(filas):
      if i!=a:
        variable_momentanea=matriz[i][a]
        variable_momentanea=abs(variable_momentanea)
        lista_verificacion.remove(variable_momentanea)

  if Flor==1:
    print("La convergencia no se garantiza por tratarse de un sistema EDD")
    print("1. Si")
    print("2. No")
    Respuesta_2= int(input("¿Deseas continuar con la ejecucion de todos modos?"))
    if Respuesta_2==2:
      print("\nAdios")
      sys.exit()
    if Respuesta_2 !=2 and Respuesta_2!=1:
      print("Lo siento no has elegido ninguna opcion, por lo que terminare con la ejecucion del programa")
      sys.exit()

  #Solucion del sistema de ecuaciones
  iteracion=0

  #Reescribir el sistema de ecuaciones
  for f in range(filas):
    for c in range(columnas):
      if f==c:
        if matriz[f][c]!=0:
          reserva_c=c
          elemento_inverso=-1/matriz[f][c]
          for c in range (columnas):
            matriz[f][c]=elemento_inverso*matriz[f][c]
          vector[f]=-(vector[f]*elemento_inverso)
          c=reserva_c
          matriz[f][c]=0
  Iteraciones=[]
  for c in range(columnas):
    x=vector[c]
    Iteraciones.append(x)
  tolerancia=float(input("¿De cuanto quieres que sea tu tolerancia? "))
  iteracion=int(input("¿Cuantas quieres que sean tus iteraciones maximas? "))
  print("A continuacion, se mostraran los vectores y sus aproximaciones")
  print("")
  
  print("Iteracion: 0")
  print("", vector)
  sumatorio=0
  nota=0
  i=1
  Campo_De_Operaciones=[]
  Solucion=[]
  tempo=0
  salida=0
  while iteracion>=0 and salida==0:
    for f in range(filas):
      for c in range(columnas):
        k=(matriz[f][c]*Iteraciones[c])
        Campo_De_Operaciones.append(k)

      sumatorio=sum(Campo_De_Operaciones)
      sumatorio=sumatorio+vector[f]
      Solucion.append(sumatorio)
      for c in range(columnas):
        k=matriz[f][c]*Iteraciones[c]
        Campo_De_Operaciones.remove(k)
        
    variable_temporal=Iteraciones[tempo]
    for a in range(filas):
      #Guarda las soluciones 
      Iteraciones[a]=Solucion[a]
    print("Iteracion: %d" %(i))
    print("", Iteraciones)
    i=i+1
    iteracion=iteracion-1


    for nosequeletraponer in range(filas):
      x=Iteraciones[nosequeletraponer]
      Solucion.remove(x)
    
    if abs(variable_temporal-Iteraciones[tempo])<tolerancia:
      print("")
      print("La solucion dada la toleracia que solicitaste es: ")
      salida=1
      for p in range(filas):
        if Iteraciones[p]==0:
          print("x[%d]= 0" %(p))
        if Iteraciones[p]!=0:
          print("x[%d] =%g " %(p, Iteraciones[p]))

    if abs(variable_temporal-Iteraciones[tempo])>=tolerancia and iteracion==0:
      print("\nLo siento, no se alcanzo tu tolerancia, sin embargo la solucion dada el numero maximo de iteraciones que pusiste es: ")
      salida=1
      for p in range(filas):
        if Iteraciones[p]==0:
          print("x[%d]= 0" %(p))
        if Iteraciones[p]!=0:
          print("x[%d] =%g " %(p, Iteraciones[p]))

  opcion_alternativa=0

  while opcion_alternativa<=1 or opcion_alternativa>2:
    print("\n\n1. Si")
    print("2. No")
    opcion_alternativa=input("¿Deseas regresar al menu principal? ")
    opcion_alternativa=int(opcion_alternativa)

    if opcion_alternativa==1:
      Menu_principal()
    if opcion_alternativa==2: 
      print("Nos vemos usuario!\n")
      sys.exit()


#Aquí va lo de Cholesky y el metodo de Potencias

def Submenu():
  opcionxd=-1
  while opcionxd<=0 or opcionxd>2:
    print("Menu de Calculos del programa\n")
    print("1. Usar el metodo de Cholesky")
    print("2. Usar el metodo de potencias")

    opcionxd=input("\n¿Que deseas hacer?")
    opcionxd=int(opcionxd
                 )
    print("")
    if opcionxd==1:
      funcion_matricial_3()
    if opcionxd==2:
      funcion_matricial_4()
  print("")
def funcion_matricial_4():
  #Empezamos con la creacion de la matríz y del vector

  n=(int(input("Introduce la dimensión de tu matríz: ")))

  matriz= np.empty((n,n),float) #Creacion de la matríz

  #Llenado de la matríz
  for i in range(n):
    for j in range(n):
      matriz[i][j]=(float(input("Introduce el valor de [%d] [%d]: "%(i,j))))

  print(matriz)

  #Creación del primer vector solución
  vector=np.empty(n,float)

  for i in range(n):
    if i==0:
      vector[i]=1

    if 0<i:
      vector[i]=0

  print("Y tu vector es: ")
  print(vector)


  tolerancia_of=(float(input("Introduce la tolerancia que quieres: ")))
  tolerancia=1 #Para que se meta una vez al while

  #Creación del vector auxiliar
  vec_aux=np.dot(matriz,vector) #aquí hago la multiplicacion del vector con la matríz

  #Creación de un vector auxiliar para calcular correctamente la norma espectral
  z=np.empty(n,float)
  for i in range(n):
    if vec_aux[i]<0:
      z[i]=-vec_aux[i]

    if 0<vec_aux[i]:
      z[i]=vec_aux[i]

  #Creación de la norma espectral
  norm_espec=np.amax(z) #Aquí es para sacar el maximo
  #norm_espec=math.fabs(np.amax(z)) #Aquí es para que tenga ya valor numerico

  norm_espec_aux=norm_espec #Esto nos ayudará a calcular el error y la tolerancia

  print(norm_espec)

  #Ahora viene la normalizacíon del vector solución

  vector=(1/norm_espec)*vec_aux

  #fin de la creación


  #El minimo de una matriz se obtiene con np.amin(array) y el maximo con np.amax(array)



  #Empieza el ciclo



  k=2


  while tolerancia_of<tolerancia and k<100:

    #veamos los pasos:
    
    #1.-)Multiplicamos la matríz con el nuevo vector normalizado para obtener uno nuevo vector de aproximación

    vec_aux=np.dot(matriz,vector)


    #1.1-)#llenado de un vector auxiliar  z (es una copia del vector auxiliar, pero con cada entrada en valor absoluto) para calcular correctamente
    #la norma espectral

    for i in range(n):
      if vec_aux[i]<0:
        z[i]=-vec_aux[i]

      if 0<vec_aux[i]:
        z[i]=vec_aux[i]


    #2.-)Sacamos la norma espectral

    norm_espec=np.amax(z) 
    #norm_espec=math.fabs(z)


    #3.-)Normalizacíon del vector solución (actualización del vector solución)
    
    vector=(1/norm_espec)*vec_aux

    #4.-)Cálculo del error/tolerancia

    tolerancia=math.fabs(norm_espec-norm_espec_aux) #Esto para que la condición en el while se actualice

    norm_espec_aux=norm_espec


    #5.-)Aumento de la variable de iteración

    k=k+1




  print("El numero de iteraciones: ", k)
  print("")
  print("Tu vector propio es ",vector)

def funcion_matricial_3():
  columnas=0
  filas=0
  Error=0
  Bucle=1
  matriz=[]
  matriz_de_calculo=[]
  matriz_distinta=[]
  vector=[]

  while columnas==0:
    columnas= int(input("¿De cuantas dimensiones quieres que sea tu matriz cuadrada? "))
    filas= columnas

    if columnas <=0:
      print("Oh no!, lo siento no puedo calcular una matriz tan grande.")
      print("Por favor inserta un numero diferente\n")
      sys.exit()
  for i in range(filas):
    matriz.append([0]*columnas)
    matriz_distinta.append([0]*columnas)
    matriz_de_calculo.append([0]*columnas)

  #Llenar datos de la matriz
  print("\nDatos de la Matriz")
  print("Indicaciones: Por favor, inserta los valores de la matriz\n")
  for f in range(filas):
    for c in range(columnas):
      x=f
      y=c
      matriz[f][c]= float(input("Elemento a[%d][%d]: " %(x,y)))
  print("")
  print("\tTu matriz es: ")
  for fila in matriz:
      for valor in fila:
          print("\t", valor, end=" ")
      print()

  #Correccion de datos   
  print("1. Si")
  print("2. No")
  correccion= int(input("¿Deseas hacer alguna correccion en tu matriz? "))
  while Bucle==1:

    if correccion == 1:
      while Error==0:
        x= int(input("Dame el numero de fila del elemento a corregir: "))
        y=int(input("Dame la columna: "))

        if (x>columnas-1 or y>filas-1):
          print("Lo siento, te estas saliendo del rango de la matriz, porfavor vuelve a introducir los valores\n")
        if x<=columnas-1 and y<=filas-1:
          Error=1
      matriz[x][y]= float(input("Ahora introduce el numero: "))
      print("Tu matriz ahora es: ")
      for fila in matriz:
          for valor in fila:
              print("\t", valor, end=" ")
          print()
      print("\n")
      Bucle=0
    if correccion == 2:
      Bucle=0
      Error=0

    if correccion !=1 and correccion !=2:
      print("No has seleccionado ninguna opcion, ¡hasta luego!\n")
      sys.exit()
  
  matriz_transpuesta=[]
  matriz_transpuesta=np.transpose(matriz)

  #Verificar si la matriz es simetrica
  if(np.array_equal(matriz_transpuesta,matriz)==False):
    print("Lo siento, tu matriz no es simetrica")
    sys.exit()

  #Factorizar
  campo_operaciones=[]

  for f in range(filas):
    for c in range(columnas):
      llave=0
      if c>f:
        llave=1
      if f==c and llave==0:
        reserva_c=c
        while c>=0:
          if f==c:
            k=matriz[f][c]
          if f!=c:
            k=-matriz_de_calculo[f][c]*matriz_de_calculo[f][c]
          campo_operaciones.append(k)
          c=c-1
        c=reserva_c
        variable_final=math.sqrt(sum(campo_operaciones))       
        matriz_de_calculo[f][c]=variable_final

        while c>=0:
          if f==c:
            k=matriz[f][c]
          if f!=c:
            k=-matriz_de_calculo[f][c]*matriz_de_calculo[f][c]
          campo_operaciones.remove(k)
          c=c-1
        c=reserva_c
        llave=1

      if c==0 and f!=c and llave==0:
        if matriz_de_calculo[0][0]==0:
          print("Lo siento, en tu matriz se da una division entre 0 y no puedo continuar")
          print("Por favor, vuelve a intentarlo\n")
          sys.exit()
        matriz_de_calculo[f][c]=matriz[f][c]/matriz_de_calculo[0][0]
        llave=1

      if f==3 and c==1:
        reserva_f=f
        reserv_c=c
        matriz_de_calculo[3][1]=(matriz[3][1]-matriz_de_calculo[3][0]*matriz_de_calculo[1][0])/matriz_de_calculo[1][1]
        llave=1

      if f!=c and c!=0 and llave==0:
        reserva_f=f
        reserva_c=c
        c=0
        f=f-1

        for x in range(reserva_c):
          k=matriz_de_calculo[f][c]
          campo_operaciones.append(k)
          c=c+1

        f=reserva_f
        for c in range(reserva_c):
          k=matriz_de_calculo[f][c]*campo_operaciones[c]
          campo_operaciones[c]=k

        c=reserva_c
        f=reserva_f
        sumatorio_negativo=-sum(campo_operaciones)
        if matriz_de_calculo[c][c]==0:
            
          print("Lo siento, en tu matriz se da una division entre 0 y no puedo continuar")
          print("Por favor, vuelve a intentarlo\n")
          print("", matriz_de_calculo)
          sys.exit()

        matriz_de_calculo[f][c]=(matriz[f][c]+sumatorio_negativo)/matriz_de_calculo[c][c]
        llave=1

        for x in range(reserva_c):
          z=campo_operaciones[0]
          campo_operaciones.remove(z)

  print("\nPor favor dame tu vector: ")
  for x in range(columnas):
    k= float(input("Dame el elemento [%d]: " %(x)))
    vector.append(k)
  print("Tu vector es: ")
  for x in range(columnas):
    print("[%g]" %(vector[x]))
  
  Espacio_Solucion=[]
  maniobra=[]
  Espacio_Solucion_2=[]
  for f in range(filas):
    for c in range(columnas):
      matriz_distinta[filas-f-1][columnas-c-1]=matriz_de_calculo[f][c]
  print("", matriz_distinta)
  while f>=0:
    i=0
    c=columnas-1
    if f==filas-1:
      variable_global= matriz_distinta[f][c]
      espacio_n= vector[f]/variable_global
      Espacio_Solucion.append(espacio_n)
      contador_i=0
      bandera=1

    while c>=0 and i<=contador_i and bandera==0:
      variable_global= matriz_distinta[f][c]
      vector[f]=vector[f]-variable_global*Espacio_Solucion[i]
      c=c-1
      i=i+1
      if i>contador_i:
        contador_i=contador_i+1
        variable_global=matriz_distinta[f][c]
        espacio_n= vector[f]/variable_global
        Espacio_Solucion.append(espacio_n)
        bandera=1 #forzar la detencion del while1

    bandera=0
    f=f-1 
  f=filas-1
 # print("El vector despejado es: ", Espacio_Solucion)
  for f in range(filas):
    k=Espacio_Solucion[f]
    maniobra.append(k)

 # for f in range(filas):
  #  Espacio_Solucion[filas-1-f]=maniobra[f]
  #print("Espacio solucion volteado: ",Espacio_Solucion)

  while f>=0:
    i=0
    c=columnas-1
    if f==filas-1:
      variable_global= matriz_distinta[f][c]
      espacio_n= Espacio_Solucion[f]/variable_global
      Espacio_Solucion_2.append(espacio_n)
      contador_i=0
      bandera=1

    while c>=0 and i<=contador_i and bandera==0:
      variable_global= matriz_distinta[f][c]
      Espacio_Solucion[f]=Espacio_Solucion[f]-variable_global*Espacio_Solucion_2[i]
      c=c-1
      i=i+1
      if i>contador_i:
        contador_i=contador_i+1
        variable_global=matriz_distinta[f][c]
        espacio_n= Espacio_Solucion[f]/variable_global
        Espacio_Solucion_2.append(espacio_n)
        bandera=1 #forzar la detencion del while1

    bandera=0
    f=f-1 
  print("La solucion es: ", Espacio_Solucion_2)


Menu_principal()