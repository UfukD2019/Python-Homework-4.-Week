print("**********Convertor from lowercase to uppercase or reverse**********\n\n\n")
print("""This is a conversion program from lowercase to uppercase or reverse.
Please choose a operation you would like to do;

For conversion from lowercase to uppercase, press    "1"
For conversion from uppercase to lowercase, press    "2"
For capitalization of first word of sentence, press  "3"
For capitalization of each words of sentence, press  "4"
""")
while True:
 operation=input("Please enter a operation code\n")
 if operation=="1":
    uppercase=input("Please enter word or sentence you would like to convert\n")
    print(uppercase.upper())
    q=input("""Would you like to quit? If yes please press "q", if no please press "n".
""")
    if q.lower()=="q":
        print("Program terminated.")
        break
    elif q.lower()=="n":
        continue
 elif operation=="2":
    lowercase=input("Please enter word or sentence you would like to convert\n")
    print(lowercase.lower())
    q=input("""Would you like to quit? If yes please press "q", if no please press "n".
""")
    if q.lower()=="q":
        print("Program terminated.")
        break
    elif q.lower()=="n":
        continue
 elif operation=="3":
    capital_letter=input("Please enter sentence you would like to capitalize first word\n")
    print(capital_letter.capitalize())
    q=input("""Would you like to quit? If yes please press "q", if no please press "n".
""")
    if q.lower()=="q":
        print("Program terminated.")
        break
    elif q.lower()=="n":
        continue
 elif operation=="4":
    capital_letter=input("Please enter sentence you would like to capitalize each words of sentence\n")
    print(capital_letter.title())
    q=input("""Would you like to quit? If yes please press "q", if no please press "n".
""")
    if q.lower()=="q":
        print("Program terminated.")
        break
    elif q.lower()=="n":
        continue
 else:
    print("You made a mistake. Please check your operation and follow the instructions.\n")

