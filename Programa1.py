import math
import numpy as np
import matplotlib.pyplot as plt

def menu():
    op=0
    while op != 3:
        print("\nMétodo\n1.-Bisección\n2.-Newton\n3.-Salir")
        op=int(input("Ingrese una opción: "))
        if op == 1:
            biseccion()
        elif op == 2:
            newton()
        elif op == 3:
            exit()
        else:
            print("Opción no válida")

def biseccion():
    funb=0
    
    while funb != 5:
        print("\nFunciones\n1.-f(x)=x^2 cos(x)-2x\n2.-f(x)=(6-2/x^2)(e^2+x/4)+1\n3.-f(x)=x^3-3sen(x^2)+1\n4.-f(x)=x^3+6x^2+9.4x+2.5\n5.-Regresar")
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
            menu()
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
            menu()
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
      return (6-(2/x**2))*((np.exp(2+x))/4)+1
  
    a=1
    b=1
    print("\nf(x)=(6-(2/x^2)) ((e^(2+x))/4)+1")
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
        newton1()
    elif otraR == 2:
        newton()
    else:
        print("Opción no válida")

def newton2():
    def f(x):
      return (6-(2/x**2))*((np.exp(2+x))/4)+1
    
    def Df(x): #derivada de la funcion
        return (np.exp(2+x))*(x+1)*(3*(x**2)-(3*x)+2)

    print("\nf(x)=(6-(2/x^2)) ((e^(2+x))/4)+1")
    x0 = float(input("Ingrese el valor inicial: ")) #valor inicial
    i=1 
    tolerancia=float(input("\nIngrese la tolerancia del Er: ")) #tolerancia
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
        newton1()
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


print("Programa 1")
menu()
