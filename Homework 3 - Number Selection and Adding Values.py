print("********** Number Selection and Adding Values **********")
while True:
 add=0   
 info=input("Please enter the data you would like to add the values of the numbers it contains\n")
 for i in info:
    if i.isdigit():
        add+=int(i)
 if add==0:
  print("The data does not include any number.")
  q=input("""Would you like to quit? If yes please press "q", if no please press "n".
""")
  if q.lower()=="q":
        print("Program terminated.")
        break
  elif q.lower()=="n":
        continue
 else:
  print("The sum of the numbers in the data is: ", add)
  q=input("""Would you like to quit? If yes please press "q", if no please press "n".
""")
  if q.lower()=="q":
        print("Program terminated.")
        break
  elif q.lower()=="n":
        continue  

