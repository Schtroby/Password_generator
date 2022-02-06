#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Worker version :)))
# pass_ch = []
# final_pass = ""
# for n in range(1, nr_letters + 1):
#   let_len = int(len(letters))
#   ran_lett = random.randint(0, let_len -1 )
#   letters[n] = letters[ran_lett]
#   pass_ch.append(letters[n])

# for j in range(1, nr_numbers + 1):
#   num_len = int(len(numbers))
#   ran_num = random.randint(0, num_len -1 )
#   numbers[j] = numbers[ran_num]
#   pass_ch.append(numbers[j])

# for i in range(1, nr_symbols + 1):
#   sym_len = int(len(symbols))
#   ran_sym = random.randint(0, sym_len -1 )
#   symbols[i] = symbols[ran_sym]
#   pass_ch.append(symbols[i])
# #print(pass_ch)

# for k in range(len(pass_ch)):
#   final_pass += pass_ch[k]
#   str_final = list(final_pass)
#   random.shuffle(str_final)
# print(f"Here is your password: " + ''.join(str_final))

# Smart version
pass_list = []
password = ""
for char in range(1, nr_letters + 1):
  pass_list.append(random.choice(letters))

for num in range(1, nr_numbers + 1):
  pass_list.append(random.choice(numbers))

for sym in range(1, nr_symbols + 1):
  pass_list.append(random.choice(symbols))
random.shuffle(pass_list)
for p in pass_list:
  password += p
print(f"Here is your password: {password}")


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
