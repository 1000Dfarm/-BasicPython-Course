import turtle
tao = turtle.Pen()# ดึงความสามารถการใช้ปากกา
tao.shape('turtle')# กำหนดปากกาให้เป็นรูปเต่า
def Draw ():
    '''ฟังชั่นการวาดรูป'''
    for i in range (36):
        tao.forward(22)
        tao.circle(10)
        tao.left(10)
def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

Go(20,20)
Draw()
 
