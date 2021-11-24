                                    #10 hands-on exercises related to Cycles
#¤1
#p=0

#for i in range(15):
# a=0
# while type(a)!=float:
 # try:
 #  a=float(input(f"Sisesta {i+1} arv"))
 # except ValueError:
 #  print("oi")

 #if a==round(a):
 # p+=1
 # print(f"{a} on täisarvud")
# else:
  #print(f"{a} ei ole täisarvud")

#print(f"{p} Täisarvud")


#¤4
#for i in range(10,21):
# print(i**2)

#¤7
#from random import *
#A<B
#a=randint(10,100)
#b=randint(10,1000)
#k=int(input("K: "))
#for i in range(a,b+1) :
 #if i%k==0: print(i)

#¤8
#for i in range(10,21):
 #print(i*2.5)

#¤6
#p=0
#n=0 
#N=int(input())
#for i in range(N):
 #a=int(input("arv: "))
 #if a<0:
 # n+=1
 #elif a>0:
 #3 p+=1
#print("Neg:",n)
#3print("Pos:",p)
#print("Null: ",N-n-p)




    

#¤3
#b=1
#for i in range(8):
  #  n=int(input("arv: "))
   # if n>0:
      #  b*=n
#print("Arv:",b)


#¤9
#p=1.03
#S=int(input("Sisesta summa"))
#N=int(input("Mitu aastat"))
#for aasta in range(1,N+1):
    #S*=p
    #print(aasta,round(S,2))



#¤13
#K=0
#S=0
#for i in range(100,1001):
    #if i %7==0:#кратные 7
        #print(i)
        #K+=1#колличество
        #S+=i#суммa

#print()
#print("kogus",K)
#print()
#print("summa",S)



#¤15
#for r in range(2):
   # for s in range(10):
        #print(s,end=" ")
    #print()



#¤16
#for r in range(1,10):
    #for s in range(1,10):
        #if r==s:
            #print(s,end=" ")
        #else:
           # print(0,end=" ")
    #print()
        
#¤29
#for r in range(1,10):
    #for s in range(1,10):
        #if r==s:
            #print("X",end=" ")
        #elif s==1:
            #print("X",end=" ")
        #else:
            #print(0,end=" ")
    #print()

#¤kupi clona
#loom=input("Kupi clona. ")
#while loom.title()!="Clona":
    #loom=input("Bce govorjat"+loom+"a ti kypi!!! ")
#print("Molodets")

#¤28 DZ
#from random import *
#print("vidite ceslo s 1 do 9")
#a=randint(1,9)
#print(a)

#a1="0"
#b=0
#k=1
#while type(a1)!=int or int(a1)>0 or int(a1)<9 :
   # try:
       # if int(a)==int(a1):
            #break
        #else:    
            #a1=(input(f"{k}arv "))
            #b+=1
            #k+=1
   # except TypeError:
        #print("ei ole")
#print("pravelnoe cislo",a1)
#print("kolicestvo popitok",b)



                                    #Testing knowledge in mathematics


#from random import*
#from math import*
#from keyboard import*
#print("Teadmiste kontroll")
#T=("Tase (1, 2, 3) ")
#while T not in [1,2,3]:
  #  try:
       # T=int(input("Tase (1, 2, 3) "))
  #  except ValueError:
       # print("Ainult 1,2 või 3")
    #else:
        #print("No.Ainult 1,2 või 3")
#if T==1:
    #min=0
    #max=15
    #tehed=["+","-"]
#elif T==2:
    #min=0
    #max=15
    #tehed=["+","-","*",]
#elif T==3:
   # min=0
   # max=20
    #tehed=["+","-","*","//",]
#kokku=0
#p=0

#while True:
   #     V=""
   #     d=input("kas jatkama E-break or S-continue: ")
      #  if d=='E':
       #     break
     #   elif d=='S':
          #  kokku+=1
          #  a=randint(min,max)
          #  b=randint(min,max)
          #  tehe=choice(tehed)# Robotaet tolko s random

          #  if tehe=="//" :
              #  while b==0:
               #     try:
               #         b=randint(min,max)
                #    except:
                    #    ValueError   
            #print(f"{a}{tehe}{b}=",end=" ")
            #A=round(eval(str(a)+tehe+str(b)),2)
            #print(A)
            #while type(V)!=int:
                #try:
                    #V=int(input("="))
                #except:
                    #ValueError
            #if V==A:
              #print("Õige vastlus!")
              # p+=1
            #else:
               # print("Motli veel!")
#print("Kokku ülesndeid: ",kokku)
#print("Õigev vastused:",p)
#K=(p/kokku)*100
#if K<60:
   # print("Hinne 2")
#elif 60<=K<75:
    #print("Hinne 3")
#elif 75<=K<90:
    #print("Hinne 4")
#elif 90<=K:
  #  print("Hinne 5")


                    

                                            #VigadeOtsing



print("*** ИГРЫ С ЧИСЛАМИ/Mäng ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
a=0
while type(a)!=float:
    try:
        a = abs(int(input("Введите целое число => ")))
        break
    except ValueError:
         print("Это не целое число")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Нет смысла ничего делать с нулём")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Определяем, сколько в числе чётных и сколько нечётных цифр")
    print()
    c=b=a
    paaris=0
    paaritu=0
    while b > 0:
        if b % 2==0:
            paaris += 1
        else:
            paaritu += 1
        b = b // 10
    
    print("Чётных цифр:",paaris)
    print("Нечётных цифр:",paaritu)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Переворачиваем* введённое число")
    print()
    b=0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10
        b = b + number
    print("*Перевёрнутое* число", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
   
