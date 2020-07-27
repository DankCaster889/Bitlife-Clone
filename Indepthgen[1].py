import random

firstw=["Martha","Agnes","Joan","Anne","Rebecca","Colleen","Jo","Katie","Marie","Skylar","Karen","Kate"]
firstm = ["Greg","Jean","Mark","George","Mike","Sean","Shaun","Tom","Steven","Chris","Jack","John"]
last = ["Stuart","Little","Wayne","Hanson","DeWitt","Olson","Steele","Thompson","Thomas","Marston","Matthews"]
gend = ["Male","Female"]

roles = {
   "Small Child":0,
   "Criminal":10,
   "Stoner":13,
   "Wageslave":15,
   "Mascot":15,
   "Homeless":18,
   "Soldier":18,
   "Scientist":25,
   "Average Person":25,
   "Judge":30,
   "Politician":40,
}

roles2 = list(roles)

alignments = {
   "Good":10,
   "Neutral":5,
   "Evil":0
}

align2 = list(alignments)

class Person:
   global people
   def __init__(self,age,cog,role,align,karma,gender,full,fname,lname):
      self.age=age
      self.cog=cog
      self.role=role
      self.align=align
      self.karma=karma
      self.gender=gender
      self.full=full
      self.fname=fname
      self.lname=lname
   
   def roleass(self,age_range):
      if age_range == "Adult":
         self.age=random.randint(18,45)
      elif age_range == "Child":
         self.age=random.randint(1,17)
      else:
         self.age=random.randint(1,45)
      age = self.age
      if age < 10:
         self.role = "Small Child"
      elif 10 < age <= 15:
         self.role = random.choice(roles2[0:4])
      elif 15 < age <= 20:
         self.role = random.choice(roles2[4:6])
      elif 20 < age <= 30:
         self.role = random.choice(roles2[6:8])
      else:
         self.role = random.choice(roles2[8:10])
   
   def basgen(self):
      self.gender= random.choice(gend)
      if self.gender == "Female":
         self.fname = random.choice(firstw)
         self.lname = random.choice(last)
      elif self.gender == "Male":
         self.fname=random.choice(firstm)
         self.lname=random.choice(last)
      self.align=random.choice(align2)
      self.karma=int(alignments[self.align])+0
      self.full = [str(self.fname)+" "+str(self.lname)]
      self.cog = [self.full,self.gender,self.age,self.role,self.align,self.karma]
   def desc(self):
       print(" ~~~~~~~~~~\n",
       	      "Name: "+str(self.full)[1:-1]+"\n",
       	      "Age: "+str(self.age)+"\n",
       	      "Gender: "+str(self.gender)+"\n",
       	      "Job: "+str(self.role)+"\n",
       	      "Moral: "+str(self.align)+"\n",
       	      "Karma: "+str(self.karma)+"\n",
       	      "~~~~~~~~~~")
def peeps(size,age_range,desc_print):
   for i in range(size):
      person.roleass(age_range)
      person.basgen()
      if desc_print == True:
         person.desc()
         continue
      elif desc_print == False:
         continue    

person=Person(None,None,None,None,None,None,None,None,None)

peeps(15,"Adult",True)