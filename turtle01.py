import turtle
import math

# 스크린 생성
s = turtle.getscreen()

# 거북이 변수 지정
t = turtle.Turtle()
t.shape("turtle")

t.penup()
t.goto(-100,0)

#장애물 설치
t.pendown()
for i in range(4):
    t.fd(100)
    t.rt(90)
    
#시작점 이동    
t.penup()    
t.goto(-350,-350)

#장애물 피하기
t.goto(-150,-150)
t.goto(-100,50)
t.goto(160,160)

#목표도착
t.goto(350,350)



