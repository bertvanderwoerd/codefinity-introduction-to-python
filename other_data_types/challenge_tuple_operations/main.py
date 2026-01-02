# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")
# Tel aantal appels
apple_count = shelf.count("apples")
# Druk aantal appels af
print("Number of Apples:", apple_count)
# Stel eerste posities van "bananas" vast
banana_index = shelf.index("bananas")
# Druk de eerste positie van "bananas" af
print("First Banana Index:", banana_index)
# Als aantal apples kleiner is dan 5, druk af dat er moet weorden aangevuld, anders druk af dat aanvulling niet nodig is
if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")
# Tel aantal grapes
grapes_count = shelf.count("grapes")
# Als het aantal grapes 1 is, druk af dat moet worden aangevuld, anders druk af dat dit niet nodig is
if grapes_count == 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")
# Controleer of "oranges" in de lijst voorkomt
if "oranges" in shelf:
    orange_index = shelf.index("oranges")
# Als oranges voorkomt in shelf, druk af waar ze staan, anders druk af dat ze er niet zijn
    print("Oranges are at index:", orange_index)
else:
    print("Oranges are out of stock.")