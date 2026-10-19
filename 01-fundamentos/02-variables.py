nombreh = "Hanz"
edadh = 25 
carrera = "Ingeníeria de software"
Mi_nota = 18.5
Aprendiendo_python = True
print("Tipo de dato:",type(nombreh))
print(type(edadh))
print(type(carrera))
print(type(Mi_nota))
print(type(Aprendiendo_python))

# CASO PRACTICO PARA APLICAR LO APRENDIDO
#Una institución educativa necesita desarrollar un pequeño programa en Python que almacene la información básica de un estudiante.
#Tu misión: crear variables para guardar el nombre, la edad, la carrera, el promedio final y si el estudiante está matriculado.
#El programa deberá mostrar de manera ordenada los valores y sus respectivos tipos de datos.
#Reglas del ejercicio:
#Utiliza str, int, float y bool.
#Aplica nombres de variables en snake_case.
#tiliza print() y type().

nombre = "Hanz" 
edad = 19
carrera = "Mecanica"
promedio_final = 18.7
matriculado = True

print(f"Nombre del estudiante: {nombre}",type(nombre))
print(f"La edad de {nombre} es: {edad}",type(edad))
print(f"La carrera de {nombre} es : {carrera} y el tipo de datos es:",type(carrera))
print(f"Su promedio  final de {nombre} es: {promedio_final} y el tipo de datos es:",type(promedio_final))
print(f"Pero el estudiate {nombre} esta matriculado?: {matriculado} y el tipo de dato es :",type(matriculado))

# =========================================
# LO QUE APRENDÍ - LECCIÓN 02
# =========================================

# 1. ¿Qué es una variable?
# Respuesta: Una variable es un nombre que hace referencia a un valor. Ese valor puede ser un texto, número, booleano u otro tipo de objeto.

# 2. ¿Qué diferencia existe entre str, int, float y bool?
# Respuesta: El tipo caracter que resive si es str solo texto es decir letras en cambio si es int solo recibe numeros enteros 20 30 pero no 32.0 porque es un float es el que almacena decimales y un bool son condiciones si es verdadero o si es falso 

# 3. ¿Para qué sirve la función type()?
# Respuesta: Sirve para mostrar el tipo de dato que esta dentro de nuestra variable si ponemos nombre = Hanz Y usamos type nos dira que la variable nombre tiende dentro un valor tipo str 

# 4. ¿Qué significa utilizar snake_case?
# Respuesta: significa que podemos entener mejor una variable in vez de poner minombre ponemos mi_nombre 

# 5. ¿Qué error cometí en el caso práctico?
# Respuesta: en la linea 30 en la parte que hace referencia a la variable que quiero sacar su tipo no puse promedio_final sino carreraun error por copear de la linea anterior

# 6. ¿Qué aprendí al desarrollar este programa?
# Respuesta: aprendi concepto de la variable como podemos organizar mejor una variable y los tipos de vriables 