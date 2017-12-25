# If the user enters anything other than a whole number, it throws the error. 

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again.")
