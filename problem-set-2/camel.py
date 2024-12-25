import re

def get_name(input_name):
    s1 =  re.sub('(.)([A-Z][a-z]+)', r'\1_\2', input_name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def main():
    user_input = input("camelCase: ")
    get_camel_case = get_name(user_input)
    print("snake_case: ",get_camel_case,)


main()

