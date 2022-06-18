#Use of this page is optional. If you use code here, make sure either import page1 or from page1 import * appear on your main.py page.

                    
#Help
def bar():
  print("--You put on an apron and go to the bar. A man comes up to you, asking for a drink. He then takes a closer look at you and says 'Hey, you look pretty young to be selling alcohol. Do you have an ID?'")
  leave_or_lie = input("--You're underage. Type 'leave' to appologise to the man and leave to help wait tables, or type 'lie' to pull out your fake ID: ")
  from page2 import leave
  from page2 import lie
  if leave_or_lie == "leave":
    leave()
  if leave_or_lie == "lie":
    lie()

def tables (): 
  print("--Asky hands you a notepad and a pencil. He says, 'Ok, do you want to work in the front or the back? There's about the same number of people. And if you're lucky you might get a few tips!'")
  front_or_back = input("--Type 'front' to work in the front of the tavern or 'back' to work at the back. There's a couple shady characters lurking back there, so be on your guard: ")
  from page2 import front
  from page2 import back
  if front_or_back == "front":
     front()
  if front_or_back == "back":
     back()


#Find 
def fight():
  print("fight wolves, injured")#need text
  onward_or_flee =input("type onward or flee")#need text
  from page2 import onward
  from page2 import flee
  if onward_or_flee == "onward":
     onward()
  if onward_or_flee == "flee":
     flee()

def avoid():
  import random
  coinflip = [1,2]
  random.choice(coinflip) 
  if coinflip == 1:
    print("successfully avoid but your horse is hurt in the briars you hid in, continue")#need text
    from page2 import onward
    onward()
  if coinflip == 2:
    print("u die")#need text
    print("grim reaper")#need text
    print("--The End--")