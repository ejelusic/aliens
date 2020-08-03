import turtle

stranica = 100

def ispisi_oblik(stranica):
    for i in range(0,12):
        turtle.forward(stranica)
        turtle.right(30)

def pomakni_kursor():
    turtle.penup()
    turtle.right(90)
    turtle.forward(20)
    turtle.right(270)
    turtle.forward(4)
    turtle.pendown()

for i in range(0,12):
    ispisi_oblik(stranica)
    pomakni_kursor()
    stranica -= 10

turtle.exitonclick()