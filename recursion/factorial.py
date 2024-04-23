


def factorial_no_recursivo(value): 
    resultado = 1 
    while value > 1: 
        resultado *= value
        value -= 1
    return resultado


def factorial_recursivo(value): #Es recursivo porque llama a la funcion otra vez, dentro de la funcion
    if value in (0,1): #Si esta entre 0 y 1, devuelve 1
        return 1
    #Si no, hace el factorial OTRA VEZ pero con value -1
    return value * factorial_recursivo(value-1)



