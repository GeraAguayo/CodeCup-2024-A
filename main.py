print('\nEncriptación de cadenas Driver Academy')
print('\n')
print('Digite 1 para ejecutar una demo')
print('Digite 2 para introducir los valores de la clave de encriptación y el texto a encriptar')
opcion = int(input('Digite su opción:'))

if opcion == 1:
    clave_enc = 'zyxwvutsrqponmlkjihgfedcba'
    cadena_og = 'Hola, Mundo!'
elif opcion == 2:
    clave_enc = input('Ingrese la clave de encriptacion: ')
    cadena_og = input('Ingrese el mensaje a encriptar: ')

cadena = cadena_og.lower()
encriptado = ''
dict = {}
n = 97
for c in clave_enc:
    dict[n] = c
    n+=1

for s in cadena:    
    if ord(s) in dict:
        if cadena_og[cadena.index(s)].isupper():
            encriptado = encriptado + dict[ord(s)].upper()
        else:
            encriptado = encriptado + dict[ord(s)]
    elif ord(s) not in dict:
        print(f'Caracter especial introducido {s} -> se añadirá sin encriptar!')
        encriptado = encriptado + s

print(f'Cadena original {cadena_og}')
print(f'ENCRIPTADO : {encriptado}') 