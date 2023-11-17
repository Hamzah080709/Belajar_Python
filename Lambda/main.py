sayHello = lambda name : print("Selamat Datang",name)

sayHello("Jaka")
#================================================================
    #def addition(num1,num2):
     # result = num1 + num2
     # print(result)

addition = lambda num1,num2: print(num1 + num2)
addition(10,12)
#==============================================================
(lambda : print("Selamat Datang"))()
(lambda fruit : print("Saya suka",fruit))("Nanas")
(lambda name="" : print("Selamat Datang",name))()
