a = int(input ("Введіть значення від 1 до 100 для а: "))

while (a < 1 or a > 100):

    a = int(input ("Введіть значення від 1 до 100 для а: "))

b = int(input ("Введіть значення від 1 до 100 для b: "))

while (b < 1 or b > 100):

    b = int(input ("Введіть значення від 1 до 100 для b: "))
else:
    if a > b:
        x = b * a + 1
    elif a == b:
        x = 3425
    else:
        x = (2 * a - 5) / b
    
print(f"Значення X: {x}")   
