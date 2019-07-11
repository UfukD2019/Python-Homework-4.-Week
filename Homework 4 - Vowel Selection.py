print("********** Vowel Selection **********")
vowel=("a","e","o","ö","u","ü","ı","i","A","E","I","İ","O","Ö","U","Ü")
with open("football player.txt","r+") as player:
 for data in player.readlines():
     if data.startswith(vowel):
         with open("Names with a vowel.txt","a") as name:
             name.write(data)
         
  


