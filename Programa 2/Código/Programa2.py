import math
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import det

def menuPrincipal():
    op=0
    while op != 3:
        print("\nProgramas\n1.-Solución de ecuaciones no lineales\n2.-Solución de sistemas de ecuaciones\n3.-Salir")
        op=int(input("Ingrese una opción: "))
        if op == 1:
            menup1()
        elif op == 2:
            programa2()
        elif op == 3:
            exit()
        else:
            print("Opción no válida")

def menup1():
    print("Programa 1")
    op=0
    while op != 3:
        print("\nMétodo\n1.-Bisección\n2.-Newton\n3.-Regresar")
        op=int(input("Ingrese una opción: "))
        if op == 1:
            biseccion()
        elif op == 2:
            newton()
        elif op == 3:
            menuPrincipal()
        else:
            print("Opción no válida")

def programa2():
    print("\nPrograma 2\nDeterminante por triangulación\n")
    n=int(input("Ingrese la dimensión n de la matriz: "))
    a=np.zeros((n,n))
    vecInd=np.zeros((n,1))
    ok=False

    def lecMatriz():
        print("\nIngrese los datos de la matriz\n")
        c=0
        d=0
        while d < n:
            c=0
            while c < n:
                a[d,c]=float(input("R"+str(d+1)+" x"+str(c+1)+": "))
                c+=1
            d += 1
    
    def lecVector():
        print("\nIngrese los datos del vector independiente\n")
        c=0
        while c < n:
            vecInd[c,0]=float(input("R"+str(c+1)+": "))
            c+=1


    def corregirM():
        print("\nIngrese los datos del coeficiente a corregir")
        w=int(input("Renglon: "))-1
        x=int(input("Columna: "))-1
        a[w,x]=float(input("Coeficiente correcto: "))
    
    def corregirV():
        print("\nIngrese los datos del valor a corregir")
        w=int(input("Renglon: "))-1
        vecInd[w,0]=float(input("Valor correcto: "))

    def imprimirMatriz():
       w=0
       x=0
       renglon=""
       print("\n\nMatriz\n")
       while w < n:
        x=0
        renglon=""
        while x < n:
            renglon+=str("{0:.2f}".format(a[w,x]))+"\t"
            x+=1
        print (renglon)
        print("\n")
        w+=1
    
    def imprimirVector():
        w=0
        print("\n\nVector Independiente\n")
        while w < n:
            print(str(vecInd[w,0]))
            w+=1

    def medd():
        aii=0.0
        aij=0.0
        b=0
        c=0
        while b<n:
            while c<n:
                if c==b:
                    aii+=abs(a[b,c])
                else:
                    aij+=abs(a[b,c])
                c+=1
            b+=1
        if aii>=aij:
            return True
        else:
            return False

    def triangular():
        facMult=0.0
        renglon=0
        columna=0
        ctn=0
        while ctn < n-1:
            renglon=ctn+1
            while renglon < n:
                columna=ctn
                facMult=-(a[renglon,columna])/(a[ctn,ctn])
                while columna < n:
                    a[renglon,columna]=(facMult*a[ctn,columna])+a[renglon,columna]
                    columna+=1
                renglon+=1
            ctn+=1
            imprimirMatriz()

    def determinante():
        determinante=1.0
        c=0
        while c < n:
            determinante*=a[c,c]
            c+=1
        determinante=math.ceil(determinante)
        print("El determinante es: "+str("{0:.0f}".format(determinante))) 
    
    while ok==False:
        op=0
        lecMatriz()
        
        while op!=1:
            imprimirMatriz()
            op=int(input("\n¿Los datos son correctos?\n1.-Si\n2.-No\nR: "))
            if op == 1:
                ok=True
            elif op == 2:
                corregirM()
            else:
                print("Opción no válida")
    
    ok=False
    while ok==False:
        op=0
        lecVector()

        while op!=1:
            imprimirVector()
            op=int(input("¿Los datos son correctos?\n1.-Si\n2.-No\nR: "))
            if op == 1:
                ok=True
            elif op == 2:
                corregirV()
            else:
                print("Opción no válida")
    
    ok=medd()
    if ok==True:
        print(str(det(a)))
        triangular()
        determinante()
        op=0
        while op != 1:
            op=int(input("\n¿Desea obtener la solución al sistema?\n1.-Si\n2.-No"))
            if op==1:
                programa3()
            
    else:
        imprimirMatriz()
        print("El determinante no se puede obtener por este método, ya que la Matriz no es Estrictamente Dominante Diagonalmente.")
        print(str(det(a)))

    exit()

def programa3():
    print("Programa aún no disponible")

def biseccion():
    funb=0
    
    while funb != 5:
        print("\nFunciones\n1.-f(x)=x^2 cos(x)-2x\n2.-f(x)=(6−2/x^2)e^(x+2)/4+1\n3.-f(x)=x^3-3sen(x^2)+1\n4.-f(x)=x^3+6x^2+9.4x+2.5\n5.-Regresar")
        funb=int(input("Ingrese una opción: "))
        if funb == 1:
            biseccion1()
        elif funb == 2:
            biseccion2()
        elif funb == 3:
            biseccion3()
        elif funb == 4:
            biseccion4()
        elif funb ==5:
            menup1()
        else:
            print("Opción no válida")

def newton():
    fun=0
    
    while fun != 5:
        print("\nFunciones\n1.-f(x)=x^2 cos(x)-2x\n2.-f(x)=(6−2/x^2)e^(x+2)/4+1\n3.-f(x)=x^3-3sen(x^2)+1\n4.-f(x)=x^3+6x^2+9.4x+2.5\n5.-Regresar")
        fun=int(input("Ingrese una opción: "))
        if fun == 1:
            newton1()
        elif fun == 2:
            newton2()
        elif fun == 3:
            newton3()
        elif fun == 4:
            newton4()
        elif fun == 5:
            menup1()
        else:
            print("Opción no válida")



def biseccion1():
    def f(x):
       return (x**2)* np.cos(x) -(2*x)
    
    a=1
    b=1

    print("\nf(x)=x^2 cos(x)-2x")
    while f(a)*f(b)>0 or a+b==0:
        print("\nIngrese el intervalo [a,b]")
        a=float(input("a= "))
        b=float(input("b= "))
        if f(a)*f(b)>=0:
            print("El intervalo no contiene la raíz")
        if a+b==0:
            print("No se puede dividir entre 0")

    tolerancia=float(input("\nIngrese la tolerancia del Er: "))
    maxit=int(input("\nIngrese el máximo de iteraciones: "))
    error=100

    i=0
    p0=0
    print("i\tRaíz\t\tEr")
    while error> tolerancia and i<=maxit:
        p1=(a+b)/2
        error=abs(p1-p0)/abs(p1)
        p0=p1
        if f(a)*f(p1)<0:
            b=p1
        else:
            a=p1
        print(i,"\t",p0,"\t",error)
        i=i+1

    print("\nLa raíz ",p0," se encontro en la iteración ",i-1," con un Er de ",error)

    x = np.linspace(-6,6,100)
    plt.plot(x,f(x))
    plt.plot(p0,f(p0),'or') #indica la raiz
    plt.grid()
    plt.show()

    otraR = int(input("\n¿Desea obtener otra raíz?\n1.-Si\n2.-No\nRespuesta: "))
    if otraR == 1:
        biseccion1()
    elif otraR == 2:
        biseccion()
    else:
        print("Opción no válida")

def biseccion2():
    def f(x):
      return (((6-2)/(x**2))*np.exp(x+2))/(4+1)

    a=0
    b=0
    print("\nf(x)=(6−2/x^2)e^(x+2)/4+1")
    while a==0 or b==0:
        print("\nIngrese el intervalo [a,b]")
        a=float(input("a= "))
        b=float(input("b= "))
        if a==0 or b==0:
            print("No se puede dividir entre 0")

    tolerancia=float(input("\nIngrese la tolerancia del Er: "))
    maxit=int(input("\nIngrese el máximo de iteraciones: "))
    error=100

    i=0
    p0=0
    print("i\tRaíz\t\tEr")
    while error> tolerancia and i<=maxit:
        p1=(a+b)/2
        error=abs(p1-p0)/abs(p1)
        p0=p1
        if f(a)*f(p1)<0:
            b=p1
        else:
            a=p1
        print(i,"\t",p0,"\t",error)
        i=i+1

    print("\nLa raíz ",p0," se encontro en la iteración ",i-1," con un Er de ",error)

    x = np.linspace(-6,6,50)
    plt.plot(x,f(x))
    plt.plot(p0,f(p0),'or') #indica la raiz
    plt.grid()
    plt.show()

    otraR = int(input("\n¿Desea obtener otra raíz?\n1.-Si\n2.-No\nRespuesta: "))
    if otraR == 1:
        biseccion1()
    elif otraR == 2:
        biseccion()
    else:
        print("Opción no válida")

def biseccion3():
    def f(x):
      return (x**3)-(3* np.sin (x**2))+1

    a=1
    b=1

    print("\nf(x)=x^3-3sen(x^2)+1")
    while f(a)*f(b)>0 or a+b==0:
        print("\nIngrese el intervalo [a,b]")
        a=float(input("a= "))
        b=float(input("b= "))
        if f(a)*f(b)>=0:
            print("El intervalo no contiene la raíz")
        if a+b==0:
            print("No se puede dividir entre 0")

    tolerancia=float(input("\nIngrese la tolerancia del Er: "))
    maxit=int(input("\nIngrese el máximo de iteraciones: "))
    error=100

    i=0
    p0=0
    print("i\tRaíz\t\tEr")
    while error> tolerancia and i<=maxit:
        p1=(a+b)/2
        error=abs(p1-p0)/abs(p1)
        p0=p1
        if f(a)*f(p1)<0:
            b=p1
        else:
            a=p1
        print(i,"\t",p0,"\t",error)
        i=i+1

    print("\nLa raíz ",p0," se encontro en la iteración ",i-1," con un Er de ",error)

    x = np.linspace(-6,6,20)
    plt.plot(x,f(x))
    plt.plot(p0,f(p0),'or') #indica la raiz
    plt.grid()
    plt.show()

    otraR = int(input("\n¿Desea obtener otra raíz?\n1.-Si\n2.-No\nRespuesta: "))
    if otraR == 1:
        biseccion1()
    elif otraR == 2:
        biseccion()
    else:
        print("Opción no válida")

def biseccion4():
    def f(x):
        return (x**3)+(6*(x**2))+(9.4*x)+ 2.5

    a=1
    b=1

    print("\nf(x)=x^3+6x^2+9.4x+2.5")
    while f(a)*f(b)>0 or a+b==0:
        print("\nIngrese el intervalo [a,b]")
        a=float(input("a= "))
        b=float(input("b= "))
        if f(a)*f(b)>=0:
            print("El intervalo no contiene la raíz")
        if a+b==0:
            print("No se puede dividir entre 0")

    tolerancia=float(input("\nIngrese la tolerancia del Er: "))
    maxit=int(input("\nIngrese el máximo de iteraciones: "))
    error=100

    i=0
    p0=0
    print("i\tRaíz\t\tEr")
    while error> tolerancia and i<=maxit:
        p1=(a+b)/2
        error=abs(p1-p0)/abs(p1)
        p0=p1
        if f(a)*f(p1)<0:
            b=p1
        else:
            a=p1
        print(i,"\t",p0,"\t",error)
        i=i+1

    print("\nLa raíz ",p0," se encontro en la iteración ",i-1," con un Er de ",error)

    x = np.linspace(-6,6,100)
    plt.plot(x,f(x))
    plt.plot(p0,f(p0),'or') #indica la raiz
    plt.grid()
    plt.show()

    otraR = int(input("\n¿Desea obtener otra raíz?\n1.-Si\n2.-No\nRespuesta: "))
    if otraR == 1:
        biseccion1()
    elif otraR == 2:
        biseccion()
    else:
        print("Opción no válida")


def newton1():
    def f(x):
       return (x**2)* np.cos(x) -(2*x)
    def Df(x): #derivada de la funcion
        return 2*x*np.cos(x)-((x**2)*np.sin(x))-2

    print("\nf(x)=x^2 cos(x)-2x")
    x0 = float(input("Ingrese el valor inicial: ")) #valor inicial
    i=1 
    tolerancia=float(input("\nIngrese la tolerancia del Er: ")) #tolerancia
    maxit=int(input("\nIngrese el máximo de iteraciones: "))
    error=100

    print("i\tRaíz\t\tEr")
    while error > tolerancia:

        x1= x0-f(x0)/Df(x0) #formula newton
        error= abs(x1-x0)/abs(x1)
        x0= x1
        print(i,"\t",x0,"\t",error)
        i=i+1
    
    print("\nLa raíz ",x0," se encontro en la iteración ",i-1," con un Er de ",error)

    x = np.linspace(-2,2,100)
    plt.plot(x,f(x))
    plt.plot(x0,f(x0),'or') #indica la raiz
    plt.grid()
    plt.show()

    otraR = int(input("\n¿Desea obtener otra raíz?\n1.-Si\n2.-No\nRespuesta: "))
    if otraR == 1:
        newton1()
    elif otraR == 2:
        newton()
    else:
        print("Opción no válida")

def newton2():
    def f(x):
      return (6-2/x*2) * np.exp(x+2) / 4+1
    
    def Df(x): #derivada de la funcion
        return (4*(np.exp(x+2))*(x-2))/(5*(x**3))

    print("\nf(x)=(6−2/x^2)e^(x+2)/4+1")
    x0 = float(input("\nIngrese el valor inicial: ")) #valor inicial
    i=1 
    tolerancia=float(input("Ingrese la tolerancia del Er: ")) #tolerancia
    maxit=int(input("\nIngrese el máximo de iteraciones: "))
    error=100

    print("i\tRaíz\t\tEr")
    while error > tolerancia and i<=maxit:

        x1= x0-f(x0)/Df(x0) #formula newton
        error= abs(x1-x0)/abs(x1)
        x0= x1
        print(i,"\t",x0,"\t",error)
        i=i+1
    
    print("\nLa raíz ",x0," se encontro en la iteración ",i-1," con un Er de ",error)

    x = np.linspace(-2,2,100)
    plt.plot(x,f(x))
    plt.plot(x0,f(x0),'or') #indica la raiz
    plt.grid()
    plt.show()

    otraR = int(input("\n¿Desea obtener otra raíz?\n1.-Si\n2.-No\nRespuesta: "))
    if otraR == 1:
        newton2()
    elif otraR == 2:
        newton()
    else:
        print("Opción no válida")

def newton3():
    def f(x):
      return (x**3)-(3* np.sin (x**2))+1
    
    def Df(x):
        return (3*(x**2))-(6*x*np.cos(x**2))

    print("\nf(x)=x^3-3sen(x^2)+1")
    x0 = float(input("Ingrese el valor inicial: ")) #valor inicial
    i=1 
    tolerancia=float(input("Ingrese la tolerancia del Er: ")) #tolerancia
    maxit=int(input("\nIngrese el máximo de iteraciones: "))
    error=100

    print("i\tRaíz\t\tEr")
    while error > tolerancia and i<=maxit:

        x1= x0-f(x0)/Df(x0) #formula newton
        error= abs(x1-x0)/abs(x1)
        x0= x1
        print(i,"\t",x0,"\t",error)
        i=i+1

    print("\nLa raíz ",x0," se encontro en la iteración ",i-1," con un Er de ",error)

    x = np.linspace(-2,2,100)
    plt.plot(x,f(x))
    plt.plot(x0,f(x0),'or') #indica la raiz
    plt.grid()
    plt.show()

    otraR = int(input("\n¿Desea obtener otra raíz?\n1.-Si\n2.-No\nRespuesta: "))
    if otraR == 1:
        newton3()
    elif otraR == 2:
        newton()
    else:
        print("Opción no válida")

def newton4():
    def f(x):
        return (x**3)+(6*(x**2))+(9.4*x)+ 2.5

    def Df(x):
        return (3*(x**2))+(12*x)+9.4

    print("\nf(x)=x^3+6x^2+9.4x+2.5")
    x0 = float(input("Ingrese el valor inicial: ")) #valor inicial
    i=1 
    tolerancia=float(input("Ingrese la tolerancia del Er: ")) #tolerancia
    maxit=int(input("\nIngrese el máximo de iteraciones: "))
    error=100

    print("i\tRaíz\t\tEr")
    while error > tolerancia and i<=maxit:

        x1= x0-f(x0)/Df(x0)
        error= abs(x1-x0)/abs(x1)
        x0= x1
        print(i,"\t",x0,"\t",error)
        i=i+1

    print("\nLa raíz ",x0," se encontro en la iteración ",i-1," con un Er de ",error)

    x = np.linspace(-2,2,100)
    plt.plot(x,f(x))
    plt.plot(x0,f(x0),'or') #indica la raiz
    plt.grid()
    plt.show()

    otraR = int(input("\n¿Desea obtener otra raíz?\n1.-Si\n2.-No\nRespuesta: "))
    if otraR == 1:
        newton4()
    elif otraR == 2:
        newton()
    else:
        print("Opción no válida")



menuPrincipal()
