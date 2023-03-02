#   a123_apple_1.py
import turtle as trtl
import random
#list for what button to click later
thewholealphabet = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r","s", "t", "v", "w", "x", "z"]

thewholealphabetpears = ["a", "e", "i", "o", "u", "y"]
#-----setup-----
rand1ap = random.choice(thewholealphabet)
xposwosloz = random.randint(-250, 250)

deifucult = input("Type something in order to procede: ")
print("initiating the test apple")

wonumber = 0
scorelore = wonumber

#these are all my different apple images that generate, go to their positions and write the letter needed to be presse
apple_image = "apple.gif" # Store the file name of your shape
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
apple = trtl.Turtle()
apple.penup()
apple.setpos(xposwosloz,200)
apple.speed(1)
faltre = False
wondernbonder = "yes"

#-----functions-----
def lettlewhwelfoal():
  global faltre, wondernbonder
  wondernbonder = "no"
  if faltre == False:
    apple.hideturtle()
    apple.color("blue")
    apple.write(rand1ap, font=("Arial", 50, "bold"))
    wondernbonder = "donezezo"
    
def blnk():
  gordinofornino = 0
def appole_fall_lol():
  global faltre, lettlewhwelfoal, rand1ap, wondernbonder, scorelore
  apple.right(90)
  wn.onkeypress(lettlewhwelfoal, rand1ap)
  wn.listen()
  apple.forward(400)
  wn.onkeypress(blnk, rand1ap)
  if wondernbonder == "yes":
    faltre = True
    if faltre == True:
      apple.hideturtle()
      apple.color("red")
      apple.write(rand1ap, font=("Arial", 50, "bold"))
      scorelore = scorelore - 1

lettrl = trtl.Turtle()
lettrl.hideturtle()
lettrl.penup()
lettrl.setpos(0,200)
lettrl.color("black")
lettrl.write(rand1ap, font=("Arial", 50, "bold"))

# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

#-----function calls-----
#draws the apples textures and makes sure to make the apple fall when the certain key is pressed
draw_apple(apple)
appole_fall_lol()
lettrl.clear()
wn.listen()
donez = "y"
while donez == "y":
  deifucult = input("What do you want the difficulty to be? (E ,M ,H): ")
  wonumber = 0
  if deifucult == "E":
    wonumber = 5
  if deifucult == "M":
    wonumber = 10
  if deifucult == "H":
    wonumber = 15
  scorelore = wonumber
  for i in range(wonumber):
    choiceloice = random.randint(0,1)
    if choiceloice == 1:
      rand1ap = random.choice(thewholealphabet)
      apple_image = "pear.gif"
    if choiceloice == 0:
      rand1ap = random.choice(thewholealphabetpears)
      apple_image = "apple.gif"
    
    xposwosloz = random.randint(-250, 250)
    wn.addshape(apple_image)
    apple = trtl.Turtle()
    apple.speed(1)
    apple.penup()
    apple.setpos(xposwosloz,200)
    faltre = False
    wondernbonder = "yes"
    lettrl = trtl.Turtle()
    lettrl.hideturtle()
    lettrl.penup()
    lettrl.setpos(0,200)
    lettrl.color("black")
    lettrl.write(rand1ap, font=("Arial", 50, "bold"))
    draw_apple(apple)
    appole_fall_lol()
    lettrl.clear()
    wn.listen()
  print("Your final score for the ammount of apples you catched is", scorelore)
  donez = input("Do you want to keep playing (y/n): ")
exit()
wn.mainloop()