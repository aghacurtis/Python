import turtle

wn = turtle.Screen()
wn.title("Cookie Clicker")
wn.bgcolor("white")

wn.register_shape("cookie.gif")

cookie = turtle.Turtle()
cookie.shape("cookie.gif")
cookie.speed(0)

clicks = 0


pen = turtle.Turtle()
pen.hideturtle()
pen.color("black")
pen.penup()
pen.goto(0, 200)

def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

cookie.onclick(clicked)

wn.mainloop()