def convert(time):
    # Split the time string into hours and minutes
    hours, minutes = map(int, time.split(':'))

    # Convert the time to hours as a float
    return hours + minutes / 60

def main():
    # Prompt the user for a time
    time_str = input("What time is it? ")

    # Convert the input time to hours
    time = convert(time_str)

    # Check if it's breakfast time
    if 7 <= time < 8:
        print("breakfast time")

    # Check if it's lunch time
    elif 12 <= time <= 13:
         print("lunch time")

    # Check if it's dinner time
    elif 18 <= time < 19:
        print("dinner time")

if __name__ == "__main__":
    main()










# def main():
#     time = input("What time is it? ")
#     get_time = convert(time)

#     if 7.0<=get_time<=8.0 :
#         print("breakfast time")
#     elif 12.0<=get_time<=13.0 :
#         print("lunch time")
#     elif 18.0<=get_time<=19.0:
#         print("dinner time")
#     else :
#         print("")


# def convert(time):
#     # hours, minutes = time.split(":")
#     time_value = time.strftime("%H.%M")
#     print("time value",time_value)
#     return time_value


# if __name__ == "__main__":
#     main()
