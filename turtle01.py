import turtle

# 스크린 생성
s = turtle.getscreen()

# 거북이 변수 지정
t = turtle.Turtle()
t.shape("turtle")
for i in range(4):
    t.fd(100)
    t.rt(90)
    
    
t.penup()    
t.goto(-350,-350)
t.goto(350,350)



