print("My to do list")
print("=============")

active = "y"

while active:
  todo = input("Apa yang ingin anda lakukan:")
  file = open('todolist.txt','a')
  file.write(todo+"\n")
  file.close()

  file = open("todolist.txt","r")
  print(file.read())

active = input("ingin lanjut?y/n")




