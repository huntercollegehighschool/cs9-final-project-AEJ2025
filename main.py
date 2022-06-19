"""
Name(s): Amelia Edgecliffe-Johnson
Name of Project: Asky's Tavern
Note: Ascii art pulled from https://www.asciiart.eu/. When possible the artist's initials were included. 
""" 

#Write the main part of your program here. Use of the other pages is optional.




def start():
  print("You begin in the famous Asky's Tavern, where many adventurers from far and wide have traveled to meet people and receive quests in the hopes of earning some gold.")
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
  print("The bartender, Asky, comes up to you and says, 'Pardon me, you look like the adventuring type. I have a job for you. Ya see, I seem to have lost my knapsack (or maybe it was stolen) and it would be great if you could find it. Or you can help me out here! I  can always use an extra pair of hands in this place. Um... assuming you do have hands?'")
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
  print("--Asky says, 'Thanks, friend! You're a great help. It was probably taken by a group of bandits who usually hang around the northeastern part of the Githube Forest. Once you get past Replait Lake, it goes pretty straight. Grab a horse from the stables. Good luck!'")
  print("--You go on your way and find Replait Lake without much trouble. However, once you get there you see a pack of wolves blocking your path.")
  print(r"""                  ~~
                             d$$b
                          .' TO$;\
                         /  : TP._;
                        / _.;  :Tb|
                       /   /   ;j$j
                   _.-'       d$$$$
                 .' ..       d$$$$;
                /  /P'      d$$$$P. |\
               /   '      .d$$$P' |\^'l
             .'           `T$P^''''  :
         _.'      _.'                ;
      `-.-''.-'-' ._.       _.-'    .-'
    `.-'' _____  ._              .-'
   -(.g$$$$$$$b.              .'
     ''^^T$$$P^)            .(:
       _/  -'  /.'         /:/;
    ._.'-'`-'  ')/         /;/;
 `-.-'..--''   ' /         /  ;
.-'' ..--''        -'          :
..--''--.-'         (\      .-(\
  ..--''              `-\(\/;`
    _.                      :
                            ;`-
                           :\
                           ;  bug""") 
  fight_or_avoid = input("--They look angry and hungry, which is never a good combination. You can either type 'fight' to try your luck at fighting them off or type 'avoid' to attempt to take evasive action and avoid the wolves altogether. So?: ")
  from page1 import fight
  from page1 import avoid
  if fight_or_avoid == "fight":
    fight()
  if fight_or_avoid == "avoid":
    avoid()
  




start()
  

#
#import page2 
#import page3  
#import page4   
