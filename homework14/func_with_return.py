def my_avg(num1: int = 0, num2: int = 0):
    """Function that takes two numbers and takes their average in a float value"""
    average: float = (num1 + num2) / 2
    return average


avg: float = my_avg(99, 90)
print(avg)


def my_headline(sentence: str = ""):
    title_head: str = sentence.upper() + "!"
    return title_head


head1: str = my_headline("python has concurred the world")
print(head1)
print(head1)


def concat_list(list1: list[int] = [None], list2: list[int] = [None], list3: list[int] = [None]):
    list_comp: list[int] = list1 + list2 + list3
    return list_comp


res_con: list[int] = concat_list([1, 2], [3, 4, 5, 6], [7, 8, 9])
print(f"the list {res_con} length is {len(res_con)}")
