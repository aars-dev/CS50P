def main():
    user_input = input("Input: ")
    vowels = ["a","e","i","o","u"]
    vowels_omitted_str = ""

    for char in user_input:
        if char.lower() not in vowels:
           vowels_omitted_str += char

    print("Output: ",vowels_omitted_str)


main()










# output = ""

# for char in user_input:
#     if char.lower() not in vowels:
#         output += char
