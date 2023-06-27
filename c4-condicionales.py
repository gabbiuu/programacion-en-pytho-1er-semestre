#CONDICIONALES
# IF ELSE ELIF

edad = 19

if edad >= 18:
    print("PASAS")
else:
    print("NO PASAS")
    
contraseña_almacenada = "WAJAJA"
contraseña_escrita = 'WAJAJA'

if contraseña_almacenada == contraseña_escrita:
    print("INICIANDO SESIÓN...")
else:
    print("CONTRASEÑA EQUIVOCADA")

#LOS ELSE IF SE ESCRIBEN COMO ELIF
ingreso_mensual = 100000


if ingreso_mensual > 10000:
    print ( "estás bien economicamentes en cualquier parte del mundo ")

elif ingreso_mensual < 1000:
    print("Estás bien económicamente en latinoamérica")
    
else: 
    print("No estás bien económicamente")
    
#IF ANIDADOS Y ELSE IF (ELIF)

ingreso_mensual = 81000 
gasto_mensual = 80000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estás en déficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Estás bien")
    else:
        print("Estás gastando mucho")
elif ingreso_mensual > 1000:
    print("Estás bien en latinoamérica")
elif ingreso_mensual > 500:
    print("Estás bien en Argentina")
elif ingreso_mensual > 200:
    print("Estás bien en Venezuela")
           