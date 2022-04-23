"""
projekt_1.py: Prvni projekt do Engeto Online Python Akademie

author: Radek Zeman
email: ze.ra@seznam.cz
discord: Radek Zeman
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

separator = 60 * "-"
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
username = input("Please, insert your login: ")
password = input("Please, insert your password: ")

if users.get(username) == password:
    print(
    f"username: {username} \n"
    f"password: {password} \n"
    f"{separator} \n"
    f"Welcome to the app, {username} \n"
    f"We have 3 texts to be analyzed.\n"
    f"{separator}")
else:
    print("unregistered user, terminating the program..")
    quit()
text_number = input("Enter a number between 1 and 3 to select: ")
print(f"{separator}")
if text_number.isnumeric is False:
    print(f"Invalid input. Must be number between 1 and {len(TEXTS)}.")
    quit()
if int(text_number) < 1 or int(text_number) > 3:
    print(f"Invalid input. Must be number between 1 and {len(TEXTS)}.")
    quit()
text = TEXTS[int(text_number) - 1]
text = text.replace("\n"," ")
text = text.split(" ")

clean_text = list()
for slovo in text:
    clean_text.append(slovo.strip(" ,!.?"))
for slovo in clean_text:
    if slovo == "":
        clean_text.remove(slovo)
word_count = clean_text.index(clean_text[-1]) + 1

title_case_count = 0
upper_case_count = 0
number_count = 0
lower_case_count = 0
number_sum = 0

for slovo in clean_text:
    if slovo.istitle():
        title_case_count = title_case_count + 1
    elif slovo.isupper():
        upper_case_count = upper_case_count + 1
    elif slovo.islower():
        lower_case_count = lower_case_count + 1
    elif slovo.isnumeric():
        number_count = number_count + 1
        number_sum = number_sum + int(slovo)

word_len = list()
for slovo in clean_text:
    word_len.append(len(slovo))

word_lenght = word_len.copy()
counted_numbers = dict()

for slovo in word_lenght:
    if slovo in counted_numbers:
        continue
    else:
        counted_numbers.update({str(slovo): word_lenght.count(slovo)})
print(f"There are {word_count} words in text.")
print(f"There are {title_case_count} titlecase words.")
print(f"There are {upper_case_count} uppercase words.")
print(f"There are {lower_case_count} lowercase words.")
print(f"There are {number_count} numeric strings.")
print(f"The sum of all the numbers is {number_sum}.")
print(f"{separator}")
print(f"{'LEN|':>3}{'OCCURENCES':^21}{'|NR.':<4}")
print(f"{separator}")
[print(f"{key:>3}|{int(value)*'*':<20} |{value:<3}")
for (key, value) in sorted(counted_numbers.items(), key=lambda x: int(x[0]))]
