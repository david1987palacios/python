def es_constante_decimal(cadena):  

    if not cadena:  
        return False  #comprobamos si la cadena esta vacia
        
        cadena = cadena.strip() #eliminamos espacios en blanco  
    
    
    if cadena[0] == '-':  #lee si hay signos negativos
        cadena = cadena[1:]  # elimina signos negativos para operar  

        partes = cadena.split('.')  #separamos decimales
    
    
    if len(partes) > 2:#comprobamos el numero de partes debe 1 o 2  
        return False  

    parte_entera = partes[0]   # comprueba los numeros enteros
    if parte_entera == '':  
        
        if len(partes) == 2 and partes[1] == '':  # Si hay parte decimal, parte entera puede estar vacía  
            return False  
    elif not parte_entera.isdigit():  
        return False  

    if len(partes) == 2 and partes[1] != '':  #  comprueba la parte decimal si existe
        if not partes[1].isdigit():  
            return False  

    return True   #si todas las validacines cumplen  

pruebas = [  
    "123.456",    
    "-123.456",   
    "123",        
    "-123",      
    "123.",      
    ".456",       
    "abc",       
    "123.a",      
    " -0123.45 ",  
]  

for prueba in pruebas:  
    resultado = es_constante_decimal(prueba)  
    print(f"'{prueba}' es constante decimal: {resultado}") 