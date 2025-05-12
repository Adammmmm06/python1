import random

hemligt_nummer = random.randint(0, 500)
försök_kvar = 10

print("Välkommen till gissa numret-spelet!")
print("Jag tänker på ett nummer mellan 0 och 500. Du har 10 försök.")

while försök_kvar > 0:
    gissning = input("Gissa ett nummer: ")

    if gissning.isdigit():
        gissning = int(gissning)

        if gissning == hemligt_nummer:
            print(f"Rätt! Du gissade rätt nummer med {försök_kvar} försök kvar.")
            break
        elif gissning < hemligt_nummer:
            print("mindre!")
        else:
            print("mer!")

        försök_kvar -= 1
        print(f"Du har {försök_kvar} försök kvar.\n")
    else:
        print("Skriv ett giltigt heltal.")

if försök_kvar == 0:
    print(f"Tyvärr, du har slut på försök. Det rätta numret var {hemligt_nummer}.")
