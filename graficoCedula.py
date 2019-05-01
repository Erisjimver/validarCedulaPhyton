from tkinter import *
from tkinter import messagebox

root=Tk()
miFrame=Frame(root,width=200,height=100)
miFrame.pack()

#------Label Numero de cedula---------------
labelCedula=Label(miFrame,text="Ingrese numero de cedula:")
labelCedula.grid(row=0,column=0,sticky="w",padx=8,pady=2)

#------Cuadro de texto ingresar N Cedula----
cuadroCedula=Entry(miFrame)
cuadroCedula.grid(row=0,column=1,padx=8,pady=2)
cuadroCedula.config(fg="blue",justify="right")

#------Boton ejecutar-----
botonEjecutar=Button(miFrame, text="Consultar", command=lambda:verificar(cuadroCedula.get()))
botonEjecutar.grid(row=1, column=0, padx=10, pady=10,columnspan=2)
botonEjecutar.config(background="black", fg="#03f943", justify="left")


#------Etiqueta Resultado
etiqueta=Label(root)
etiqueta.pack()


def verificar(nro):
    l = len(nro)
    print(l)
    if l == 10 or l == 13: # verificar la longitud correcta
        cp = int(nro[0:2])
        if cp >= 1 and cp <= 24: # verificar codigo de provincia
            tercer_dig = int(nro[2])
            if tercer_dig >= 0 and tercer_dig < 6 : # numeros enter 0 y 6
                if l == 10:
                    return __validar_ced_ruc(nro,0)                       
                elif l == 13:
                    return __validar_ced_ruc(nro,0) and nro[10:13] != '000' # se verifica q los ultimos numeros no sean 000
            elif tercer_dig == 6:
                return __validar_ced_ruc(nro,1) # sociedades publicas
            elif tercer_dig == 9: # si es ruc
                return __validar_ced_ruc(nro,2) # sociedades privadas
            else:
               # raise Exception(u'Tercer digito invalido') 
                etiqueta.config(text="Tercer digito invalido")
        else:
            #raise Exception(u'Codigo de provincia incorrecto') 
            etiqueta.config(text="Codigo de provincia incorrecto")
    else:
        #raise Exception(u'Longitud incorrecta del numero ingresado')
        etiqueta.config(text="Longitud incorrecta del numero ingresado")



def __validar_ced_ruc(nro,tipo):
    total = 0
    if tipo == 0: # cedula y r.u.c persona natural
        base = 10
        d_ver = int(nro[9])# digito verificador
        multip = (2, 1, 2, 1, 2, 1, 2, 1, 2)
    elif tipo == 1: # r.u.c. publicos
        base = 11
        d_ver = int(nro[8])
        multip = (3, 2, 7, 6, 5, 4, 3, 2 )
    elif tipo == 2: # r.u.c. juridicos y extranjeros sin cedula
        base = 11
        d_ver = int(nro[9])
        multip = (4, 3, 2, 7, 6, 5, 4, 3, 2)
    for i in range(0,len(multip)):
        p = int(nro[i]) * multip[i]
        if tipo == 0:
            total+=p if p < 10 else int(str(p)[0])+int(str(p)[1])
        else:
            total+=p
    mod = total % base
    val = base - mod if mod != 0 else 0
    
    if val==d_ver:
        print("Cedula Valida")
        etiqueta.config(text="Cedula Validad")
    else:
        print("Cedula Invalida")
        etiqueta.config(text="Cedula Invalida")
    return val == d_ver

#print("Validar cedula o DNI Ecuador")
#verificar(input("Ingrese numero de cedula: "))

#Autor Israel


root.mainloop()