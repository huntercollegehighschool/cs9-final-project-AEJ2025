                    
#Help
def bar():
  print("--You put on an apron and go to the bar. A man comes up to you, asking for a drink. He then takes a closer look at you and says 'Hey, you look pretty young to be selling alcohol. Do you have an ID?'")
  leave_or_lie = input("--You're underage. Type 'leave' to apologize to the man and leave to help wait tables, or type 'lie' to pull out your fake ID: ")
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
  print("--You fight the wolves from your horse, bravely attacking with your sword. Unfortunately your horse is pretty badly injured in the process. Do you cut your losses and flee the woods empty handed or do you continue onward on foot?")
  onward_or_flee =input("--Type 'onward' to keep going on foot or 'flee' to return to the tavern: ")
  from page2 import onward
  from page2 import flee
  if onward_or_flee == "onward":
     onward()
  if onward_or_flee == "flee":
     flee()

def avoid():
  import random
  wolf_list = ["success", "caught"]
  wolf = random.choice(wolf_list)
  from page3 import success
  from page3 import caught
  if wolf == "success":
    success()  
  elif wolf == "caught":
    caught()
  