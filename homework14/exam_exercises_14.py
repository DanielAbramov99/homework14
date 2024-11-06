stop: int = -99
while True:
    try:
        number: int = int(input("enter a number between 0-9999:"))
        if number == stop:
            break
        if not 0 <= number <= 9999:
            print("invalid number,try again")
        else:
            num_str = str(number)
            if len(set(num_str)) == 1:
                print(True)
            else:
                print(False)


    except ValueError:
        print("illegal parameter, try again")

num1: int = int(input("enter first number:"))
num2: int = int(input("enter second number:"))
num3: int = int(input("enter third number:"))

if num1 + num2 == num3 or num2 + num3 == num1 or num1 + num3 == num2:
    print(True)
else:
    print(False)

user_input_word: str = str(input("enter your word:"))
word: str = user_input_word.lower()
stop: str = "*"
letter_list: list[str] = []
while True:
    letter: str = str(input("enter a letter:"))
    if letter == stop:
        break
    else:
        letter_list.append(letter.lower())

if all(l in word for l in letter_list):
    print(True)
else:
    print(False)
