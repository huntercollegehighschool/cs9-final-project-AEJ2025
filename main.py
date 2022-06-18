"""
Name(s): Amelia Edgecliffe-Johnson
Name of Project: Asky's Tavern
Note: Ascii art pulled from https://www.asciiart.eu/. When possible the artist's initials were included. 
""" 

#Write the main part of your program here. Use of the other pages is optional.




def start():
  print("You begin in the famous Asky's Tavern, where many adventurers   from far and wide have traveled to meet people and recieve quests in the hopes of earning some gold.")
  print(r"""                          (    )
                           (    )
                          (    )
                            )  )
                           (  (                  /\
                            (_)                 /  \  /\
                    ________[_]________      /\/    \/  \
           /\      /\        ______    \    /   /\/\  /\/
          /  \    //_\       \    /\    \  /\/\/    \/    
   /\    / /\/\  //___\       \__/  \    \/
  /  \  /\/    \//---- \       \ |[]|     \
 /\/\/\/       //Asky's \       \|__|      \
/      \      /X-Tavern-X\                  \
        \    /_I_II  I__I_\__________________\
               I_I|  I__I_____[]_|_[]_____I
               I_II  I__I_____[]_|_[]_____I
               I II__I  I     XXXXXXX     I
            ~~~~~   ~~~~~~~~~~~~~~~~~~~~~~~~""")
  print("The bartender, Asky, comes up to you and says, 'Pardon me, you look like the adventuring type. I have a job for you. Ya see, I seem to have lost my napsack (or maybe it was stolen) and it would be great if you could find it. Or you can help me out here! I  can always use an extra pair of hands in this place. Um... assuming you do have hands?'")
  help_or_find = input("--So what'll it be? Type 'help' to help Asky in the tavern or 'find' to find the bag: ")
  if help_or_find == "help":
    help()
  if help_or_find == "find":
    find()
#start____________________________________________________ 
def help():
  print("--Asky says,'Thank you so much. Want to help out at the bar or wait tables?'")
  bar_or_tables = input("--Type 'bar' to help at the bar or 'tables' to wait tables: ")
  from page1 import bar
  from page1 import tables
  if bar_or_tables == "bar":
    bar()
  if bar_or_tables == "tables":
    tables()
def find():
  print("Give directions, bye")#add text
  print("wolves, insert ascii")#add text
  fight_or_avoid = input("type fight or avoid")#add text
  from page1 import fight
  from page1 import avoid
  if fight_or_avoid == "fight":
    fight()
  if fight_or_avoid == "avoid":
    avoid()
  
  #need code
  




start()
  

#
#import page2 
#import page3  
#import page4   
