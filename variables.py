#Day 2: 30 days of python programming
import math


first_name = 'Alberto'
last_name = 'Zarzo'
full_name = 'Alberto Zarzo'
country = 'Spain'
city = 'Salamanca'
age = 27
year = 2022
is_married = False
is_true = False
is_light_on = True
first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True


print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name) == len(last_name))
print(len(first_name) <= len(last_name))
print(len(first_name) >= len(last_name))
print(len(first_name) != len(last_name))
print(len(first_name) < len(last_name))
print(len(first_name) > len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
divide = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two #Potencias en Python
floor_division = num_one // num_two

radio = float(input('Radio: '))

area_of_circle = float(math.pi * radio**2)

print(area_of_circle)

circum_of_circle = 2 * math.pi * radio

print(circum_of_circle)

nombre = input("Nombre: ")
apellido = input("Apellido: ")
pais = input("País: ")
edad = input("Edad: ")

print("Tu nombre es: "+nombre+ " y tu apellido "+apellido+ " eres de "+pais+ " y tienes" +edad+ "años")

help('keywords')