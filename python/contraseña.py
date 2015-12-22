# -*- coding: utf-8 -*-
"""Crear un módulo para validación de contraseñas. Dicho módulo, deberá cumplir con los siguientes criterios de aceptación
a contraseña debe contener un mínimo de 8 caracteres.
Una contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico.
La contraseña no puede contener espacios en blanco.
Contraseña válida, retorna True.
Contraseña no válida, retorna el mensaje La contraseña elegida no es segura."""

import getpass
import string
import re

def validar_pass():
    a,b,c,d = 0,0,0,0
    print "\n"
    print "Introduzca su contraseña:"
    #r=getpass.getpass() #Esconde la contraseña
    r=raw_input()
    if len(r)>8:
        if ' ' in r:
            print "La contraseña no puede contener espacios en blanco"
        else:
            for letra in r:
                if letra.isalnum()==False:
                    
                    d+=1
                elif letra.isdigit():
                    
                    c+=1
                elif letra.islower():
                    
                    a+=1
                elif letra.isupper():
                    
                    b+=1
                else:
                    pass
            if a>=1 and b>=1 and c>=1 and d>0:
                return True
            else:
                print "La contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico"

    else:
        print "La contraseña debe contener un mínimo de 8 caracteres"


