print("Dobrodosel v kalkulatorju")

t = raw_input("Zelis se nadaljevati? Da/Ne? ")
while t == "da":
    print(t)

    x = raw_input("Vpisi stevilko, katero zelis uporabiti: ")
    y = raw_input("Vpisi operacijo: ")
    z = raw_input("Vpisi drugo stevilko: ")

    if y == "-":
        print (int(x) - int(z))
    elif y == "+":
        print (int(x) + int(z))
    elif y == "/":
        print (int(x) / float(z))
    elif y == "*":
        print (int(x) * float(z))

