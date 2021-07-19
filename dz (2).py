a = int(input("Перше число:"))
b = int(input("Друге число:"))
c = str(input("Дія:"))
f = int(0)

if c == "+":
    d = (a + b)
    print(f"Результат додавання {a} на {b} -> {d} ")

if c == "-":
    d = (a - b)
    print(f"Результат віднімання {a} на {b} -> {d} ")

if c == "*":
    d = (a * b)
    print(f"Результат множення {a} на {b} -> {d} ")

if c == "/":
    if a == f:
        print("Деления на 0 запрещено!")
    if b == f:
        print("Деления на 0 запрещено!")
    else:
        d = (a / b)
        print(f"Результат ділення {a} на {b} -> {d} ")
#git init
#git add *
#git commit -m "first commit"
#git branch -M main
#git remote add origin https://github.com/danchik/mydzpython.git
#git push -u origin main