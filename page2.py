#Use of this page is optional. If you use code here, make sure either import page2 or from page2 import * appear on your main.py page.
''' __
                            .d$$b
                          .' TO$;\
                         /  : TP._;
                        / _.;  :Tb|
                       /   /   ;j$j
                   _.-"       d$$$$
                 .' ..       d$$$$;
                /  /P'      d$$$$P. |\
               /   "      .d$$$P' |\^"l
             .'           `T$P^"""""  :
         ._.'      _.'                ;
      `-.-".-'-' ._.       _.-"    .-"
    `.-" _____  ._              .-"
   -(.g$$$$$$$b.              .'
     ""^^T$$$P^)            .(:
       _/  -"  /.'         /:/;
    ._.'-'`-'  ")/         /;/;
 `-.-"..--""   " /         /  ;
.-" ..--""        -'          :
..--""--.-"         (\      .-(\
  ..--""              `-\(\/;`
    _.                      :
                            ;`-
                           :\
                           ;  bug'''                            
                             

#Help-Bar
def leave():
  print("--You appoligise, and say you're new to the area so you weren't aware of the laws. You then head back over to Asky to tell him that you need to go work at the tables.")
  print("--Asky says, 'Oops, sorry for getting you in trouble, friend. I'll have a chat with Pyth when I get home tonight and explain the situation. He just got his sherrif job so he's a little too excited to catch a criminal. Anyway, do ya want to wait tables in the front or the back?")
  front_or_back = input("--Ah, so that's the man's name. Good to know. Anyway, type 'front' to work in the front of the tavern or 'back' to work at the back. There's a couple shady characters lurking back there, so be on your guard: ")
  if front_or_back == "front":
     front()
  if front_or_back == "back":
     back() 

      
  
  

def lie():
  print("--You hand over the fake ID you bought for a few copper pieces from a friend's cousin. The man looks at you and says, 'Kid, this is Joan of Arc fanart. My son's friend sells them to idiotic teens for a couple copper pieces. I'd better not see your lying butt in here again, got it?'") 
  print("--Your valiant attempt to use a dodgy fake ID failed. Maybe you'll make smarter choices in the future? Although you've been kicked out, so you won't be able to come back here again. Better get back on the road.")
  print("--The End--")


#Help-Tables
def front():
  print("--You walk to the front of the tavern where you see a friendly looking group of adenturers who wave you down and introduce themselves as Elwin, Calla, and the Hearthstone siblings. They order some mushroom soup and a couple root beers for the siblings. When you bring them their order, they tip you generously and compement you for your service.")
  print("--After your day is done, you've earned enough tips, plus the pay Asky gave you, to cover your expences for a few more days of adventuring until you find another tavern to work at. Maybe you'll run into Elwin, Calla, and the Hearthstones on your travels!")
  print("--The End--")
def back():
  print("shady lads, ask what they want, kidnapped")
  print("take you away as bait, you escape, they see you")
  import random
  coinflip = [1,2]
  random.choice(coinflip)
  if coinflip == 1:
    print("win, crown")#need text
    print("congrats+gifts")#need text
    print("--The End--")
  elif coinflip == 2:
    print("u die")#need text
    print("grim reaper")#need text
    print("--The End--")


#Find-Fight
def onward():
  print("continue, tie up horse")#need text
  print("meet bandits")#need text
  import random
  coinflip = [1,2]
  random.choice(coinflip) 
  if coinflip == 1:
    print("win, crown")#need text
    print("congrats+gifts")#need text
    print("--The End--")
  elif coinflip == 2:
    print("u die")#need text
    print("grim reaper")#need text
    print("--The End--")

def flee():
  print("return, help horse")#need text
  print("dissapointment, hurt horse, don't come back")#need text
  

