def my_function():
  print("Hello world")

my_function()

name = "Lucas";
print(name)

name = 0;

print(name);

arr = [0,1,2];

print(arr); 


# %%
print('Hello World')

# %%
name = "Anthony"
name = "Nate" 

print("name 1:", name)

# this is how variables are declared
# constant variables do not exist 
# %%

a = b = c = 20

print("this is a", a)
print("this is a", b)
print("this is a", c)

# %%
# you can assign multiple variables at once
a,b,c = 1,2,"Joe"

#This is multiple assignment 
# %%
string = "Hello World!"

print(string[2:])
print(string[6:10])

# %%
# created a list and printed it a few differnt ways
crazyList = ['Lucas', 'Elephant', 125, 'PizzaRolls', 23 ]
list2 = [ 2, 54, 15 ]
list3 = [ 2, 44, 15 ]
print(crazyList)
print(crazyList * 2)


class OurClass: 
  name = "Anthony"

test = OurClass()

print(test.name)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Anthony", 31)

print(p1.name)
print(p1.age)

# dice roll
import random 
def dice_roll():
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  print("roll:", dice1 + dice2)

dice_roll()

# basic really easy sum function that lucas did 
# super easy nbd - took zero talent
def maths(num1, num2):
  print( num1 ** num2)

maths(2, 4)

if p1.age > 30:
  print("you're old")

noun = [ "Dennis Rodman", "Japan", "Gel Pen", "tuna flavored cupcake", "tennis ball scented cologne", "short shorts" ]
verbs = ["lived", "laughed", "loved"]
# our scenario function
def randomScenario():
  # randIndex1 = random.randint(1,3)
  # randIndex2 = random.randit(1,3)
  print(noun[random.randint(0,len(noun) -1)] + " " + verbs[random.randint(0,len(verbs) - 1)] + ' ' + noun[random.randint(0,len(noun) -1)]) 

randomScenario()

def reverseString(): 