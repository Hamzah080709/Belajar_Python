def add(n1,n2):
  result = n1 + n2
  print(num1,"+",num2,"=",result)

def substitute(n1,n2):
  result = n1 - n2
  print(num1,"-",num2,"=",result)

def multiply(n1,n2):
  result = n1*n2
  print(num1,"x",num2,"=",result)

def divide(n1,n2):
  result = n1 / n2
  print(num1,":",num2,"=",result)

print("Kalkulator Sederhana")
print("====================")
print("Mode kalkulator")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

mode = input("Pilih 1/2/3/4:")
num1 = int(input("Masukkan angka pertama:"))
num2 = int(input("Masukkan angka kedua:"))

if mode == "1":
    add(num1,num2)
elif mode == "2":
     substitute(num1,num2)
elif mode == "3":
    multiply (num1,num2)
elif mode == "4":
    divide(num1,num2)