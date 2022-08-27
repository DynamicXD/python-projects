def remove_match_char(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                c = list1[i]
                list1.remove(c)
                list2.remove(c)
                list3 = list1 + ["*"] + list2
                return [list3, True]

    list3 = list1 + ["*"] + list2
    return [list3, False]


one = input("Enter First Person's name: ")
one = one.lower()
one.replace(" ", "")
one_list = list(one)
two = input("Enter Second Person's name: ")
two = two.lower()
two.replace(" ", "")
two_list = list(two)
proceed = True

while proceed:
    ret_list = remove_match_char(one_list, two_list)
    con_list = ret_list[0]
    proceed = ret_list[1]
    star_index = con_list.index("*")
    one_list = con_list[: star_index]
    two_list = con_list[star_index + 1:]
count = len(one_list) + len(two_list)
result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
while len(result) > 1:
    split_index = (count % len(result) - 1)
    if split_index >= 0:
        right = result[split_index + 1:]
        left = result[: split_index]
        result = right + left
    else:
        result = result[: len(result) - 1]

print("Relationship status: ", result[0])
