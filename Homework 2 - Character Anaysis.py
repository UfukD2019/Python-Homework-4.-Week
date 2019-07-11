print("********** Character Analysis **********")
uppercase=""
lowercase=""
number=""
special_character=""
space=""
info=input("Please enter the data you would like to analyze\n")
for i in info:
    if i.isupper():
        uppercase+=i
    elif i.islower():
        lowercase+=i
    elif i.isnumeric():
        number+=i
    elif i.isspace():
        space+=i
    else:
        special_character+=i
print("The data contains:\n {} uppercase letter(s),\n {} lowercase letter(s),\n {} number(s),\n {} special character(s),\n {} space(s)".format(len(uppercase),len(lowercase),len(number),len(special_character),len(space)))
print("""These are "{}", "{}", "{}", "{}".""".format(uppercase,lowercase,number,special_character))
