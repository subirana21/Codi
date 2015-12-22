# -*- coding: utf-8 -*-
"""
Ejercicio 1
Crear un módulo para validación de nombres de usuarios. Dicho módulo, deberá cumplir con los siguientes criterios de aceptación:

    El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12.
    El nombre de usuario debe ser alfanumérico.
    Nombre de usuario con menos de 6 caracteres, retorna el mensaje "El nombre de usuario debe contener al menos 6 caracteres".
    Nombre de usuario con más de 12 caracteres, retorna el mensaje "El nombre de usuario no puede contener más de 12 caracteres".
    Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje "El nombre de usuario puede contener solo letras y números".
    Nombre de usuario válido, retorna True.

"""

def validar_usuario():
    print "\n"
    print "Introduzca su usuario:"
    s=raw_input('--> ')
    if s.isalnum():
        if len(s)>12:
            print "El nombre de usuario no puede contener más de 12 caracteres"
            validar_usuario()
        elif len(s)<6:
            print "El nombre de usuario debe contener al menos 6 caracteres"
            validar_usuario()
        else:
            return True
    else:
        print "El nombre de usuario puede contener solo letras y números"
        validar_usuario()

#validar_usuario()

"""
if __name__ == '__main__':
"""
