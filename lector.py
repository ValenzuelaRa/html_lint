import re
from tokens import dicc_html

def token_isopen(token): #token_isopen es el nombre de la funcion, token es el argumento
#El argumento obtiene un token y devuelve verdadero si es una etiqueta de abertura
    for key,value in dicc_html.items(): #dicc_html.items() toma los tokens y las asigna a value y las etiquetas se guardan en key
        if value == token: #Si los tokens (value) de dicc_html son iguales a los tokens del documento html, entonces:
            if token in [0,20]: #Entra a este if, y valida si la lista con los valores 0, 20 estan en los token del documento html
                pass #Si estan, el marcador pass evita que mande un error
                return 2 #regresa un 2
            if token == 34: #si token es igual a el token 34 del documento html, entonces regresa el token 1
                return 1
            if '/' in key: #si la etiqueta hay un '/' entonces regresa un 1
                return 1
        else:
            return 0 # si no regresa 0
        return value #Regresa el token de dicc_html la verificado sin errores

with open("index.html", "r", encoding='utf-8-sig') as f: #Habre el documento 'index.html', codificado en utf-8
    html_doc = f.read() #lee el index.html y lo guarda en la variable html_doc

tokens = [] #tokens, es una lista vacia

tags = re.findall(r'<[^>]+>', html_doc) #De la variable html_doc verifica el patron de los strings que esten dentro de <>

for t in tags: #las etiquetas dentro de <> se guardan en t para su recorrido
    s = t.split() #Divide las etiquetas y se guarda la divicion en la variable s
    bandera = 1
    for key,value in dicc_html.items(): #dicc_html.items() toma los tokens y las asigna a value y las etiquetas se guardan en key
        if key in s[0]: #s[0] toma las etiquetas que estan dentro del documento html y valida si estan en el diccionario de etiquetas
            print(f" \n {s[0]}  => {value}") #{s[0]} Imprime las etiquetas validadadas => {value} asigna los tokens de las etiquetas
            bandera = 0
            tokens.append(value) #el metodo append agrega los valores de las etiquetas a la lista tokens
            break #Sale del segundo ciclo for 
    if bandera:
        print(f'\n {s[0]} \t => -1') # Asigna un -1 a las etiquetas que no estan completas con su abertura o cierre

html_close = [0,31]
print(f"\n{tokens}") #Imprime la lista de tokens encontrados