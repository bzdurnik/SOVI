print ("---- TO JEST KALKULATOR ----")
print ("Menu działań")
print (" 1 -- Dodawanie")
print (" 2 -- Odejmowanie")
print (" 3 -- Mnożenie")
print (" 4 -- Dzielenie")

a = int (input("Podaj liczbę pierwszą a: "))
b = int (input("Podaj liczbę drugą b: "))

działanie = input("wybierz działanie (1-4): ")

if działanie  == "1":
    print(" Wynik a+b = ", a+b)
elif działanie  == "2":
    print(" Wynik a-b = ", a-b)
elif działanie  == "3":
    print(" Wynik a*b = ", a*b)
elif działanie  == "4":
    print(" Wynik a/b = ", a//b)
else:
    print("Błędny wybór")
    