def main():
    user_input = input("Greeting: " ).strip().lower()
    if "hello" in user_input:
        print("$0")
    elif user_input[0]=="h" and len(user_input)!="hello":
        print("$20")
    else:
        print("$100")
main()


