#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#compute random letters, symbols and numbers
# create pre random list empty, will insert first letters, then symbols and finally numbers.
pre_random_list = []
rand_num = 0

#compute random letters and insert into list. 
for random_letters in range(1,nr_letters +1):
  random_letters = letters[random.randint(0,25)]
  rand_num = random.randint(0,len(pre_random_list))
  pre_random_list.insert(rand_num ,random_letters)

#compute random symbols and insert into list.
for random_symbols in range(1,nr_symbols + 1):
  random_symbols = symbols[random.randint(0,8)]
  rand_num = random.randint(0,len(pre_random_list))
  pre_random_list.insert(rand_num ,random_symbols)

#compute random numbers and insert into list.
for random_numbers in range(1, nr_numbers +1):
  random_numbers = numbers[random.randint(0,9)]
  rand_num = random.randint(0,len(pre_random_list))
  pre_random_list.insert(rand_num ,random_numbers)

#for randomization of letters, numbers and symbols in list position
  
num = 0
final_output = ""

for num in range(1,len(pre_random_list)):
  final_output = final_output + pre_random_list[num]
  num += 1

#final Output
print(final_output)
