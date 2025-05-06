from random import randint
random_number = randint(1, 3)

print("Jag tänker på ett tal mellan 1 och 3")

guess = int(input("Gissa vilket tal jag tänker på!"))

if guess == random_number:
  print("Snyggt jobbat! Det var rätt!")
else:
  print("Tyvärr, det var fel.")

