

def fibonacci_no_recursivo(value):
    values = [0,1]

    for _ in range(value-1):
        values.append(values[-1]+values[-2])
  
    return values[value]



def fibonacci_recursivo(value):
    #condicion de corte
    if value == 0:
        return 0
    if value == 1:
        return 1
    #llamada recursiva
    return fibonacci_recursivo(value-1) + fibonacci_recursivo(value-2)