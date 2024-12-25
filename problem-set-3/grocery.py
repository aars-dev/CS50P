grocery_list = {}

while True:
    try:
        item = input().upper().strip()
        if item not in grocery_list:
            grocery_list[item] = 1
        else:
            grocery_list[item] += 1
    except EOFError:
        sorted_dict = dict(sorted(list(grocery_list.items())))
        for item in sorted_dict:
            print(sorted_dict[item], item, sep=" ")
        break
    except KeyError:
        pass
