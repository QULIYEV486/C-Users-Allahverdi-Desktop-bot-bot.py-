import sys
from datetime import datetime   

if sys.argv[1] == "tarixi" and sys.argv[2] == "de":
    print(datetime.now(). strftime('%S-%Y-%M-%H'))
   
elif sys.argv[1] == "ili" and sys.argv[2] == "de":
    print(datetime.now(). strftime('%Y'))

elif sys.argv[1] == "ayi" and sys.argv[2] == "de":
    print(datetime.now(). strftime('%m'))

elif sys.argv[1] == "saati" and sys.argv[2] == "de":
    print(datetime.now(). strftime('%H'))


# folder

import os 

if sys.argv[1] == "folder" and sys.argv[2] == "yarat":  
    directory = input('Folder adi yain: ')

    parent_dir = r"C:\Users\Allahverdi\Desktop\bot"

    path = os.path.join(parent_dir,directory)

    os.mkdir(path)

    print('folder yarandi')

elif sys.argv[1] == "folderi" and sys.argv[2] == "sil":
    directory = input()

    parent_dir = r"C:\Users\Allahverdi\Desktop\bot"

    path = os.path.join(parent_dir,directory)

    os.rmdir(path)

    print('Folder Silindi')

# kalkulyator
op = sys.argv[1]

if op  == "topla":
    a = int(input())
    b = int(input())
    print( a + b)

elif op == "cix":
    a = int(input())
    b = int(input())
    print( a - b) 

elif op == "vur":
    a = int(input())
    b = int(input())
    print( a * b)

elif op == "bol":
    a = int(input())
    b = int(input())
    print( a // b)      











 


