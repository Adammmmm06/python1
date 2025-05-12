import random

hemligt_nummer = random.randint(0, 100)
försök_kvar = 10

print("Välkommen till gissa numret-spelet!")
print("Jag tänker på ett nummer mellan 0 och 100. Du har 10 försök.")

while försök_kvar > 0:
    gissning = input("Gissa ett nummer: ")

    if gissning.isdigit():
        gissning = int(gissning)