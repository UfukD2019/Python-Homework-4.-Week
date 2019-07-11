print("********** Replacing Turkish Character with English Character **********\n\n\n")
source = "şçöğüıŞÇÖĞÜİ"
target = "scoguiSCOGUI"
replacing_table = str.maketrans(source,target)
with open("football player.txt","r") as player:
 data=player.read()
 with open("Replacing Character.txt","a") as name:
     name.write(data.translate(replacing_table))

