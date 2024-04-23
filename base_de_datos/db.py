

#SI tuviera que ser en orden usaria lista
# def ver_datos(*word, **kword):
#     for key, subdiccionario in kword.items():
#         valores_subdiccionario = list(subdiccionario.values())

#         for nombre in word:
#             if nombre in valores_subdiccionario:
#                 id = key
#             else:
#                 return("no hay")
#         return id


def ver_datos(*word, **kword):
    count = 0
    for key, subdiccionario in kword.items():
        valores_subdiccionario = set(subdiccionario.values()) #El set es como una lista, pero no tiene orden especifico
        
        if set(word).issubset(valores_subdiccionario): #Me sirve si necesito que tome los valores de nombres aunque no esten en orden
            count += 1
            id = key
    
    if count == 0:
        return 'no hay'
    elif count == 1:
        return id
    else:
        return f"Hay {count} ID con el mismo nombre"
    






