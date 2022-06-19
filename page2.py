
#Help-Bar
def leave():
  print("--You apologize, and say you're new to the area so you weren't aware of the laws. You then head back over to Asky to tell him that you need to go work at the tables.")
  print("--Asky says, 'Oops, sorry for getting you in trouble, friend. I'll have a chat with Pyth when I get home tonight and explain the situation. He just got his sheriff job so he's a little too excited to catch a criminal. Anyway, do ya want to wait tables in the front or the back?")
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
  print("--You walk to the front of the tavern where you see a friendly looking group of adenturers who wave you down and introduce themselves as Elwin, Calla, and the Hearthstone siblings. They order some mushroom soup and a couple root beers for the siblings. When you bring them their order, they tip you generously and compliment you for your service.")
  print("--After your day is done, you've earned enough tips, plus the pay Asky gave you, to cover your expenses for a few more days of adventuring until you find another tavern to work at. Maybe you'll run into Elwin, Calla, and the Hearthstones on your travels!")
  print("--The End--")
def back():
  print("--You go to the back of the tavern, where some shady-looking characters and a kind old woman sit. You ask for their orders and the old woman says, 'Let me get that bit of dirt off your nose, dearie.' She reaches out her hankerchief and you suddenly become drowsy and collapse.")
  print("--While you remain unconsious, the shady characters and the not so kind old lady take you to their camp in the Githube Woods. When you wake up you see a bag embroidered with the words 'To Asky, xoxo Pyth'. They must have stolen Asky's knapsack!")
  print("--You try to grab the knapsack but the bandits catch you escaping and corner you. You are forced into battle!")
  import random

  bandit_list = ["win", "lose"]
  bandit = random.choice(bandit_list)
  from page3 import win
  from page3 import lose
  if bandit == "win":
    win()  
  elif bandit == "lose":
    lose()


#Find-Fight
def onward():
  print("--You continue on foot after tying up the injured horse. You'll go back for him once you finish your quest.")
  print("--After a bit of walking, you see the bandit's camp, as well as Asky's bag, which is embroidered with the words 'To Asky, xoxo Pyth'. Unfortunately, the bandits see you, too. You are forced into battle!")
  import random
  bandit_list = ["win", "lose"]
  bandit = random.choice(bandit_list)
  from page3 import win
  from page3 import lose
  if bandit == "win":
    win()  
  elif bandit == "lose":
    lose()

def flee():
  print("--You go back to the tavern where the horse is bandaged up and given some apples for his good work. When you go inside the tavern, Asky seems glad to see you alive, but his face falls when he realizes that you don't have his bag.")
  print("--He says, 'Kid, not only did you fail to get my bag, you injured one of my best horses. I doubt that I can trust you with another quest. Please be on your way and do your best to avoid coming here again.'")
  print("--The End--")
  

