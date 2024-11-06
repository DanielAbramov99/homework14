import statistics


def my_ascending(num1: int = 0, num2: int = 0):
    if num2 > num1:
        print(num2, num1)
    else:
        print(num1, num2)


my_ascending(-12, 7)


def my_details(sentence: str = None):
    middle: int = len(sentence) // 2
    print(sentence[0], end=" ")
    print(sentence[middle], end=" ")
    print(sentence[-1])


my_details("AI is the best")


def say_bool(boolean: bool = None):
    if boolean:
        print("yes")
    else:
        print("no")


say_bool(True)
say_bool(False)


def print_even_or_odd(even_or_odd_list: list[int]):
    for num in even_or_odd_list:
        if num % 2 == 0:
            print("even", end=" ")
        else:
            print("odd", end=" ")


print_even_or_odd([5, 3, 2, 10, 15, 14, 14])
print()


def my_statistics(school: list[int]):
    print(f"the best score for the test is:{max(school)}")
    print(f"the worst score for the test is:{min(school)}")
    print(f"the average score of all students is:{statistics.mean(school)}")
    print(f"the amount of scores is:{len(school)}")


scores: list[int] = []
stop: int = -99
while True:
    score: int = int(input("enter your score:"))
    if score == stop:
        break
    elif 0 <= score <= 100:
        scores.append(score)
    else:
        print("invalid score try again")
my_statistics(scores)
