# Meredith Aguirre NC = 0013

# Python Conditions
print("+-+-+-Condiciones-+-+-+")
a = 33
b = 200
if b > a:
  print("b es mayor que a")
  numero = 15
if numero > 0:
  print("El numero es positivo")

# Python Elif Statement
print("-3-3-3- Elif -3-3-3-")
edad = 25

if edad < 13:
  print("Eres un niño")
elif edad < 20:
  print("Eres un adolecente")
elif edad < 65:
  print("Eres un adulto")
elif edad >= 65:
  print("Eres un anciano")

# Python Else Statement
print("-1-1-1- Else -1-1-1-")
temperatura = 22

if temperatura > 30:
  print("Afuera hace calor!")
elif temperatura > 20:
  print("Aguera esta caliente")
elif temperatura > 10:
  print("Esta fresco afuera")
else:
  print("Afuera hace frio!")

# Python For Loops
print("-0-0-0- For -0-0-0-")
frutas = ["manzana", "durazno", "banana"]
for x in frutas:
  if x == "durazno":
    continue
  print(x)

# Python While Loops
print("-5-5-5- While -5-5-5-")
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

  print("Meredith Aguirre NC 0013")