x=int(input('choose:100,200,300'))
      
sum=0
while (x==100):
      w=int(input('player 1 choose a square number:'))
      if w==1 or w==4 or w==9 or w==16 or w==25 or w==36 or w==49 or w==64 or w==81 :
                         sum =sum+w
      else :
          print ("error")
      if sum==100 :
               print('you win')
               break
      if sum>100:
          print ("you lose")
          break
      y=int(input('player 2 choose a square number:'))
              
      if y==1 or y==4 or y==9 or y==16 or y==25 or y==36 or y==49 or y==64 or y==81:
                           sum=sum+y
      else :
          print ("error")
      if sum==100 :
                    print('you win')
                    x=0
      if sum>100:
         print ("you lose")
         break
while (x==200):
  
    w=int(input('player 1 choose a square number:'))
    if w==1 or w==4 or w==9 or w==16 or w==25 or w==36 or w==49 or w==64 or w==81 or w==100 or w==121 or w==144 or w==169 or w==196:
                         sum=sum+w
    else :
          print ("error")
    if sum==200 :
               print('you win')
               break
    if sum>200:
         print ("you lose")
         break   
    y=int(input('player 2 choose a square number:'))
    if y==1 or y==4 or y==9 or y==16 or y==25 or y==36 or y==49 or y==64 or y==81 or y==100 or y==121 or y==144 or y==169 or y==196:
                         sum=sum+y
    else :
          print ("error") 
    if sum==200:
          print('you win')
          x=0
    if sum>200:
         print ("you lose")
         break
while (x==300):
  
    w=int(input('player 1 choose a square number:'))
    if w==1 or w==4 or w==9 or w==16 or w==25 or w==36 or w==49 or w==64 or w==81 or w==100 or w==121 or w==144 or w==169 or w==196 or w==225 or w==256 or w==289:
                         sum=sum+w
    else :
          print ("error")
    if sum==300 :
               print('you win')
               break
    if sum>300:
         print ("you lose")
         break   
    y=int(input('player 2 choose a square number:'))
    if y==1 or y==4 or y==9 or y==16 or y==25 or y==36 or y==49 or y==64 or y==81 or y==100 or y==121 or y==144 or y==169 or y==196 or w==225 or w==256 or w==289:
                         sum=sum+y
    else :
          print ("error") 
    if sum==300:
          print('you win')
          x=0
    if sum>300:
         print ("you lose")
         break      
print('error,try again')
