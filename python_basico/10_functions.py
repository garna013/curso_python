### Funtions ###

def my_function ():
    print("Esto es una funcion")

my_function ()
my_function ()
my_function ()

def sum_two_values (first_value, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("Hola", " Mundo")
sum_two_values(1.4, 5.2)

def sum_two_values_with_return (first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values_with_return(10, 5)

print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name("Moure", "Brais")
print_name(surname = "Moure", name = "Brais")

def print_name_whit_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_whit_default("Brais", "Moure, MoureDev")
print_name_whit_default("Brais", "Moure")
print_name_whit_default(surname = "Moure", name = "Brais")

def print_texts(*texts):
    for text in texts:
        print(text)

print_texts("Hola", "Python", "MoureDev")
print_texts("Hola")