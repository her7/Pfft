import os
from time import sleep


a="\033[91m"
b="\033[92m"
c="\033[93m"
d="\033[0m"
                  
def main():
      try:
            os.system("clear")
            toilet (b+"+"*40)
            print(c+"\tHILIH KINTIL :v")
            print (a+"\t  Kusus Jomblo !!")
            toilet (b+"+"*40)
            print (d+"""program ini cuman iseng iseng cowg jangan dianggap serius.""")
            print (b+"+"*40)
            kata=input(a+"\Kata!?\n> "+d)
            while True:
                  sleep(0.5)
                  print (c+"Dasar KontooooLLL Anjing kau "+kata+" !!")
      except KeyboardInterrupt:
            ask=input(a+"\nlagi y/n ? "+d)
            if ask == "y":
                  main()
            
            elif ask == "n":
                  os.system("clear")
                  print(b+"MMMMUaaach !! :*"+d)
                  exit()
            
try:
      main()
            
except KeyboardInterrupt:
      ask=input(a+"\nlagi y/n ? "+d)
      if ask == "y":
            main()
            
      elif ask == "n":
            os.system("clear")
            print(b+"MMMMUaaach !! :*"+d)
            exit()
