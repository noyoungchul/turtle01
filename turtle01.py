import turtle
import math

#거리계산 함수 구현
def distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) **2 + (y2 - y1) **2)
    return distance

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

#도착 알림
if distance(*t.pos(), 350, 350) < 10:
    print("목표 지점에 도착했습니다!")

