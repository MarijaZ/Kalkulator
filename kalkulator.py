print("Dobrodosel v kalkulatorju")

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

