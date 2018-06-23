import turtle
import random

turtle.penup()
turtle.goto(-40,180)
turtle.pendown()
turtle.write("Turtle Race")


# step 1 : Making Track
turtle.speed(6)
turtle.penup()
turtle.goto(-140,140)
for step in range(14):
  if step < 13 :
    turtle.write(step + 1 , align = 'center')
  else:
    turtle.write("Finish Line")
  turtle.right(90)
  turtle.forward(10)
  turtle.pendown()
  turtle.forward(150)
  turtle.penup()
  turtle.backward(160)
  turtle.left(90)
  turtle.forward(20)
turtle.goto(-190,-50)

# step 2 : Making Turtle

# for red turtle
red = turtle.Turtle()        # turtle.red.color('red') wrong
red.color('red')
red.shape('turtle')

red.penup()
red.goto(-190,100)
red.pendown()
red.write("Raju")

red.speed(2)
red.penup()
red.goto(-160,100)
red.pendown()
red.right(360)



# for blue turtle
blue = turtle.Turtle()
blue.color('blue')
blue.shape('turtle')

blue.penup()
blue.goto(-190,70)
blue.pendown()
blue.write("Giri")

blue.speed(2)
blue.penup()
blue.goto(-160,70)
blue.pendown()
blue.left(360)




# for green turtle
green = turtle.Turtle()
green.color('green')
green.shape('turtle')

green.penup()
green.goto(-190,40)
green.pendown()
green.write("JP")

green.speed(2)
green.penup()
green.goto(-160,40)
green.pendown()
green.right(360)




# for yellow turtle
yellow = turtle.Turtle()
yellow.color('yellow')
yellow.shape('turtle')

yellow.penup()
yellow.goto(-190,10)
yellow.pendown()
yellow.write("DV")

yellow.speed(2)
yellow.penup()
yellow.goto(-160,10)
yellow.pendown()
yellow.left(360)




# Racing Turtle
winners = []
r_flag = 0
b_flag = 0
g_flag = 0
y_flag = 0

for turn in range(300):
  if red.xcor() < 160:
    red.forward(random.randint(1,5))
    if(red.xcor() >= 120 and r_flag == 0):
      winners.append("Raju")
      r_flag = 1

  if blue.xcor() < 160:
    blue.forward(random.randint(1,5))
    if(blue.xcor() >= 120 and b_flag == 0):
      winners.append("Giri")
      b_flag = 1

  if green.xcor() < 160:
    green.forward(random.randint(1,5))
    if(green.xcor() >= 120 and g_flag == 0):
      winners.append("JP")
      g_flag = 1

  if yellow.xcor() < 160:
    yellow.forward(random.randint(1,5))
    if(yellow.xcor() >= 120 and y_flag == 0):
      winners.append("DV")
      y_flag = 1

  if r_flag == 1 and b_flag == 1 and g_flag == 1 and y_flag == 1:
    break


# Printing Winners
turtle.goto(-190,-50)
turtle.write("1st Position : " + winners[0])

turtle.goto(-190,-70)
turtle.write("2nd Position : " + winners[1])

turtle.goto(-190,-90)
turtle.write("3rd Position : " + winners[2])

turtle.goto(-190,-110)
turtle.write("4th Position : " + winners[3])
# turtle.done()
# turtle.Screen().bye()
# exitonclick not defined. need win=turtle.Screen(); win.exitonclick()
turtle.goto(-190,-140)
turtle.write("Clck here to Exit...")
turtle.exitonclick()
