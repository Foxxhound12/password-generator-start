#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
chosen_letters = []
for letter in range(nr_letters):
    l = random.randint(0, len(letters)-1)
    chosen_letters.append(letters[l])
chosen_symbols = []
for symbol in range(nr_symbols):
    s = random.randint(0, len(symbols)-1)
    chosen_symbols.append(symbols[s])
    #chosen_symbols.insert(symbol, symbols[s])
chosen_numbers = []
for number in range(nr_numbers):
    n = random.randint(0, len(numbers)-1)
    chosen_numbers.append(numbers[n])

password = (chosen_letters+chosen_symbols+chosen_numbers) #letters = 0, symbols = 1, numbers = 2
#print(password)
random.shuffle(password)
#empty_string = ""   #kann auch jeglicher anderer string sein, muss nicht leer sein. der angegebene string verbindet die Listenobjekte. Wäre er zb. P oder ein Leerzeichen wäre es 0P1,...oder 0 1  (Index der Liste, das auf entsprechendes Objekt in der Liste verweist)
#final_password=empty_string.join(password)  #oder wie unten in einer Zeile: str() kreiert einen leeren String
#final_password = str().join(password)
#oder
final_password = str.join("", password) #wäre auch mit for loop möglich final_password="", for item in password: final_password += item (string concatenation)
print(final_password)
