def conversor(tipo_pesos, valor_dolar):   
    pesos = input("Ingresar cantidad de pesos " + tipo_pesos + ": ")
    pesos = int(pesos)
     
    valor_dolar = 183 
    dolares = pesos / valor_dolar  
    dolares = round(dolares, 2)
    dolares = str(dolares) 
    print("Tienes un total de $" + dolares + " dolares") 
    
   while True:
     valor1=int(raw_input("ingrese un numero entero: "))
     if type(valor1)==int:
      break
   


menu = """
💰 Bienvenido al conversor de monedas 💰 

1- Pesos argentinos 
2- Pesos colombianos 
3- Pesos mexicanos 

Elige una opcion: """ 

opcion = input(menu) 

if opcion == "1": 
    conversor("argentinos", 182)

elif opcion == "2": 
    conversor("colombianos", 3875)  

elif opcion == "3": 
    conversor("mexicanos", 24)  
else: 
    print("Ingresa una opcion correcta") 





