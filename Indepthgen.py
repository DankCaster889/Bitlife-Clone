import random, os, platform
   
firstw=["Martha","Agnes","Joan","Anne","Rebecca","Colleen","Jo","Katie","Marie","Skylar","Karen","Kate"]
firstm = ["Greg","Jean","Mark","George","Mike","Sean","Shaun","Tom","Steven","Chris","Jack","John"]
last = ["Stuart","Little","Wayne","Hanson","DeWitt","Olson","Steele","Thompson","Thomas","Marston","Matthews"]
gend = ["Male","Female"]

roles = {
   "Child":10,
   "Wageslave":15,
   "Mascot":15,
   "Homeless":18,
   "Soldier":18,
   "Scientist":25,
   "Average Person":25,
   "Judge":30,
   "Politician":40,
}

bigj = {
   "Unemployed":[0],
   "Fast Food Employee":random.randint(20000,24000),
   "Clerk":random.randint(29000,45000),
   "Cook":random.randint(44000,92000),
   "Chef":random.randint(19000,38000),
   "Baker":random.randint(20000,28000),
   "Musician":random.randint(26000,75000)
}

bigj2 = list(bigj)

smallj = {
   "Lawncare":[random.randint(20,50)],
   "Tutor":[random.randint(15,50)],
   "Dog Walker":[random.randint(10,40)],
   "Busking":[random.randint(1,100)]
}

smallj2 = list(smallj)

stats = { 
   "Mood":0,
   "Intellect":0,
   "Appearance":0,
   "Money":0
}

stats2 = list(stats)

roles2 = list(roles)

folks = {
   "Parent1":None,
   "Parent2":None,
   "Boss":None,
   "Partner":None
}

folks2 = list(folks)

alignments = {
   "Good":10,
   "Neutral":5,
   "Evil":0
}

align2 = list(alignments)

ages = [10,15,20,30]

class Job:
   def __init__(self,title=None,pay=None,exp=None,hire=None,full=None,avail=None):
      self.title = title
      self.pay = pay
      self.exp = exp
      self.hire = hire
      self.full = full
      self.avail = avail
          
   def onetime(self):
      self.title = random.choice(smallj2)
      self.pay = smallj[self.title]
   
   def bigjob(self):
      self.title = random.choice(bigj2[1:5])
      self.pay = bigj[self.title]
   
   def hiring(self):
      opening = []
      for i in range(3):
          self.bigjob()
          self.full = [self.title, str(self.pay)]
          opening.append(self.full)
      if len(opening) == 0:
          print("You fail to find a place that is hiring.")
      else:
         clear()
         for x in range(3):
            print(str(x+1)+": "+str(opening[x]))
         choice=input("These are the available jobs. Choose one.\n")
         if choice == "0":
            print("You gave up on finding a job.")
         else:    
            event.coinflip()
            if flip == "heads":
               self.hire = True
               clear()
               print("You got the job!")
               player.job = opening[(int(choice)-1)]
               folks["Boss"] = peeps(1,"Adult",False)
            else:
               self.hire = False
               print("You failed to get the job...")
      opening.clear()
        
class Person:
   global people
   def __init__(self,age=None,cog=None,role=None,job="Unemployed",align=None,karma=None,gender=None,full=None,fname=None,lname=None):
      self.age=age
      self.cog=cog
      self.role=role
      self.job=job
      self.align=align
      self.karma=karma
      self.gender=gender
      self.full=full
      self.fname=fname
      self.lname=lname

   def ageroll(self,age_range):
      if age_range == "Adult":
         self.age=random.randint(18,45)
      elif age_range == "Child":
         self.age=random.randint(1,17)
      elif age_range == "Any":
         self.age == (1,45)
      elif 0 <= age_range <= 45:
         self.age = age_range
   
   def roleass(self):
      age = int(self.age)
      if age < 10:
         self.role = "Small Child"
      elif 10 < age <= 15:
         self.role = random.choice(roles2[1:4])
      elif 15 <= age < 20:
         self.role = random.choice(roles2[4:6])
      elif 20 <= age < 30:
         self.role = random.choice(roles2[6:8])
      else:
         self.role = random.choice(roles2[8:10])         
   
   def basgen(self,age):
      self.ageroll(age)
      self.roleass()
      self.gender= random.choice(gend)
      if self.gender == "Female":
         self.fname = random.choice(firstw)
         self.lname = random.choice(last)
      elif self.gender == "Male":
         self.fname=random.choice(firstm)
         self.lname=random.choice(last)
      self.align=random.choice(align2)
      self.karma=int(alignments[self.align])
      self.full = [self.fname+" "+self.lname]
      self.cog = [self.fname,self.lname,self.gender,self.age,self.role,self.align,self.karma]
   
   def desc(self):
      print(" ~~~~~~~~~~\n",
       	     "Name: "+str(self.full)[1:-1]+"\n",
       	     "Age: "+str(self.age)+"\n",
       	     "Gender: "+str(self.gender)+"\n",
       	     "Job: "+str(self.job)+"\n",
       	     "Moral: "+str(self.align)+"\n",
       	     "Karma: "+str(self.karma)+"\n",
       	     "~~~~~~~~~~")

class Event:
   def __init__(self,type):
      self.type=type

#flips a coin, useful ig
   def coinflip(self):
      global flip
      flip = random.randint(1,2)
      if flip == 1:
         flip = "heads"
      elif flip == 2:
         flip = "tails"
      
#generates events that happen
   def eventgen(self):
      self.coinflip()
      if flip == "heads":
         self.type = "good"
         player.karmaroll(self.type)
         if bonus > 0:
            x = random.randint(bonus,20)
            y = random.choice(stats2)
            stats[y]+=x
         else:
            x = random.randint(1,10)
            y = random.choice(stats2)
            stats[y]+=x
      elif flip == "tails":
         self.type == "bad"
         player.karmaroll(self.type)
         if bonus > 0:
            x = random.randint(bonus,20)
            y = random.choice(stats2)
            stats[y]-=x
         else:
            x = random.randint(1,20)
            y = random.choice(stats2)
            stats[y]-=x
      statcap()
      if y == stats2[0]:
         if self.type == "good":
            print("You have become happy and gained "+str(x)+" mood.")
         else:
            print("You had a rough day and lost "+str(x)+" mood.")
      elif y == stats2[1]:
          if self.type == "good":
             print("You gained "+str(x)+" dollars.")
          else:
             print("You lost "+str(x)+" dollars.")
      elif y == stats2[2]:
         if self.type == "good":
            print("You read a good book and gained "+str(x)+"\nintellect.")
         else:
            print("You consumed some fake media and lost "+str(x)+"\nintellect.")
      elif y == stats2[3]:
         if self.type == "good":
            print("You got some nice clothes "+str(x)+"\nappearance.")
         else:
            print("You tore your shirt and lost "+str(x)+"\nappearance.")
      print("---------------------------")
   
   def inpevent(self):
      if 0 < player.age < 5:
         x=input("You feel a sudden strength in your legs.\nA. Crawl, even still?\nB. Rise from the floor and stand tall.\nChoose: ")
         if x == "a":
            print("You crawl forward, despite your strong legs, and go to your toys.")
         elif x == "b":
            print("You stand up, your parents missing your first steps, before promptly falling onto your tush.")

event=Event(None)

class Player(Person):

#contains all the generation for the player and parents
   def prestart(self):
      self.basgen(0)
      self.align="Neutral"
      peeps(1,"Adult",False)
      person.lname=self.lname
      person.full=[str(person.fname)+" "+str(person.lname)]
      folks["Parent1"]=person.cog
      peeps(1,"Adult",False)
      person.lname=self.lname
      person.full=[str(person.fname)+" "+str(person.lname)]
      folks["Parent2"]=person.cog
      if self.fname == folks["Parent1"][0] or self.fname == folks["Parent2"][0]:
         self.full = [self.fname+" "+self.lname+", Jr."]

#generates parents and the default player    
   def startup(self):
      self.prestart()
      print(" ---------------------------\n",
      	     "You are "+str(self.full)[1:-1]+".\n",
      	     "Your parents are "+str(folks["Parent1"][0])+" and "+str(folks["Parent2"][0])+" "+str(self.lname)+"\n",
      	     "---------------------------")      

#does a karma roll to possibly modify event outcomes
   def karmaroll(self,type):
      global bonus
      event.coinflip()
      x = random.randint(1,5)
      y = self.karma
      total = 0      
      if type == "good":
         total = x+y
      elif type == "bad":
         total = x+y
      opproll = random.randint(1,10)
      if 0 < opproll < total:
         bonus = random.randint(1,25)
      else:
         bonus = 1
      
#main bit, ages the player up and holds most of the game's content
   def life(self):
      self.startup()
      death = random.randint(75,115)
      self.job = bigj2[0]
      while self.age < death:
         money = stats["Money"]
         if len(self.job) != 10:
            jtitle = self.job[0]
         else:
            jtitle = self.job
         print(" Name: %s\n" % str(self.full)[1:-1],
         	     "Age: %s\n" % self.age,
         	     "Money: %s\n" % f"{money:,}",
         	     "Current job: %s\n" % jtitle,
               "---------------------------")
         print(" Choices:\n",
         	      "1. Age\n",
         	      "2. Work\n",
         	      "3. Stats\n",
         	      "4. Relationships\n",
         	      "5. Misc. Option\n")
         x = input(" Choose: ")
         if x == "1":
            clear()
            print(" ---------------------------")
            self.age+=1
            if self.job != bigj2[0]:
               stats["Money"]+=int((self.job)[1])
            if folks["Boss"] == None:
               for x in range(2):
                  folks[folks2[x]][3]+=1
            elif folks["Boss"] != None:
               for x in range(folks):
                  folks[folks2[x]][3]+=1     
            if self.age > 12:
              event.eventgen()
         elif x == "2":
            age = self.age
            if 10 <= age < 15:
               job.onetime()
               print("You found work: "+str(job.title)+"\n")
               x = input("Take it?\n")
               if x == "y":
                  stats["Money"]+=int(str(job.pay)[1:-1])
                  print("You earned $%s " % str(job.pay)[1:-1])
               if x == "n":
                  print("Oh well, no money this time...\n")
            elif age < 10:
               print(" ---------------------------")
               print("Nobody will hire you because you're too\nyoung.")
               print(" ---------------------------")
            elif 15 <= age:
               print("What job would you like to do?\n",
               	      "1. Small Job\n 2. Regular Job")
               x=input("Choose: ")
               if x == "1":
                  job.onetime()
                  print("You found work: "+str(job.title)+"\n")
                  x = input("Take it?\n")
                  if x == "y":
                     stats["Money"]+=int(str(job.pay)[1:-1])
                     print("You earned $%s " % str(job.pay)[1:-1])
                  if x == "n":
                     print("Oh well, no money this time...\n")
               elif x == "2":
                  if self.job != "Unemployed":
                     print("You already have a job: "+str(self.job))
                     x=input("Quit?\n")
                     if x == "y":
                        self.job ="Unemployed"
                        clear()
                        print("You quit your job.")
                  else:
                     job.hiring()
         elif x == "3":
            clear()
            print(" ---------------------------")
            for x in range(3):
                print(str(stats2[x])+": "+str(stats[stats2[x]]))
            print(" ---------------------------")
         elif x == "4":
               if folks["Parent1"][0] in firstm:
                  for key, value in folks.items():
                     if value == None:
                        continue
                     else:
                        print("Dad: "+str(folks["Parent1"][0]))
               else:
                  print("Mom: "+str(folks["Parent1"][0]))
               if folks["Parent2"][0] in firstw:
                  for key, value in folks.items():
                     if value == None:
                        continue
                     else:
                        print("Mom: "+str(folks["Parent2"][0]))
                  else:
                     print("Dad: "+str(folks["Parent2"][0]))
      print("You are dead!")

#generates NPCs based on parameters
def peeps(size,age_range,desc_print):
   for i in range(size):
      person.basgen(age_range)
      if desc_print == True:
         person.desc()
         continue
      elif desc_print == False:
         continue    

#sets and maintains a cap for all stats
def statcap():
   if stats[stats2[3]] < 0:
      stats[stats2[3]] = 0
   for x in range(3):
      if stats[stats2[x]] <= 0:
         stats[stats2[x]] = 0
      if stats[stats2[x]] >= 100:
         stats[stats2[x]] = 100
      else:
         continue

#clears the screen
def clear():
   if platform.system == "Windows":
      os.system('cls')
   else:
      os.system('clear')

#main menu
def menu():
   clear()
   print("-------------------")
   print("BITLIFE 2: ORIGINS")
   print("-------------------")
   print("A Game Made By: Bela Olson")
   print("-------------------")
   print(" 1. Play\n",
         "2. Settings\n",
         "3. FAQ")
   x=input("Choose: ")
   if x == "1":
      clear()
      player.life()
   elif x == "2":
      clear()
      print("UNDER CONSTRUCTION!")
      input("Press any button to return...\n")
      menu()
   elif x == "3":
      print(" ---------------------------")
      print(" Hi, I'm the developer.\n",
      	     "This is a game I made. Hope you enjoy!\n",
      	     "---------------------------")
      input("Press any button to return...\n")
      menu()
   
person=Person()
job=Job()
player=Player()
menu()