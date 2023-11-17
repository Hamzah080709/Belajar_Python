#open('file.pertama','x') x=membuat file baru
  #membaca file
file = open('file_pertama.txt','r') #r = membaca file(yang sudah ada)
  #mengambil konten dengan .read()
print(file.read())
#==============================================================
file = open('file.txt','w')

file.write("Selamat Datang")
file.write("\n")
file.write("Nama saya Hamzah")
 #setiap selesai manulis
 #harus .close
file.close()
#==========================================================
file = open('file.txt', 'a')
file.write("\n")
file.write("Saya lahir di Semarag")

file.close()
#open('file.pertama','x') x=membuat file baru
  #membaca file
file = open('file_pertama.txt','r') #r = membaca file(yang sudah ada)
  #mengambil konten dengan .read()
print(file.read())
#==============================================================
file = open('file.txt','w')

file.write("Selamat Datang")
file.write("\n")
file.write("Nama saya Hamzah")
 #setiap selesai manulis
 #harus .close
file.close()
#==========================================================
file = open('file.txt', 'a')
file.write("\n")
file.write("Saya lahir di Semarag")

file.close()
