import os
import time
def hesappy():
    print("Hesap Makinesine Hoşgeldiniz İşlemler:+,-,*,/")
    islem=input("")
    if islem == "+":
        os.system('clear')
        plus_num1=int(input("One Numbers:"))
        plus_num2=int(input("Two Numbers:"))
        print(plus_num1+plus_num2)
        time.sleep(5)
        os.system('clear')
        exit(hesappy())
    if islem == "-":
        down_num1=int(input("One Numbers:"))
        down_num2=int(input("Two Numbers:"))
        print(down_num1-down_num2)
        time.sleep(5)
        os.system('clear')
        exit(hesappy())
    if islem == "*":
        ik1=int(input("One Numbers:"))
        ik2=int(input("Two Numbers:"))
        print(ik1*ik2)
        time.sleep(5)
        os.system('clear')
        exit(hesappy())
    if islem == "/":
        ert=int(input("One Numbers:"))
        if ert != 0:
            ert2=int(input("Two Numbers:"))
            if ert2 != 0:
                print(ert/ert2)
                time.sleep(5)
                os.system('clear')
                exit(hesappy())
            else:
                print("/:")
                os.system('clear')
                exit(hesappy())        
        else:
            print("/:")
            os.system('clear')
            exit(hesappy())
    
    
    
    
hesappy()
