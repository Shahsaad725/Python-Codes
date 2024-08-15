import turtle as t
import time as ti

screen = t.Screen()
screen = t.screensize(500)
screen = t.bgcolor("Black")
count=1
t1=t.Turtle()
t2=t.Turtle()
t3=t.Turtle()
t4=t.Turtle()
t5=t.Turtle()
t6=t.Turtle()
t7=t.Turtle()
t8=t.Turtle()



pen1 = t.Turtle()
# for dot function
pen2 = t.Turtle()
# for outer design

pen2.goto(-67,-155)
# to put pen1 in side the pen2


pen2.hideturtle()

for i in range(30):
    pen2.speed(30)
    pen2.forward(133)
    # t.pendown()
    pen2.color("yellow")
    pen2.forward(135)
    pen2.right(255)
    pen2.forward(135)





pen1.color("black")

for i in range(200):
    
    if i % 2 == 0:
        x=0.1
    else:
        x=0.01
    # if count / 3 == 0:
        # x=0.01
    count=count+1
    
    pen1.color("Red")  
    # to hide the pointer by asigning the same color as that of dot
    
    t1.dot(306,"Red")
    ti.sleep(x)
    pen1.color("darkviolet")
    t2.dot(276,"darkviolet")
    ti.sleep(x)
    pen1.color("cyan")
    t3.dot(246,"cyan")
    ti.sleep(x)
    pen1.color("orange")
    t4.dot(216,"orange")
    ti.sleep(x)
    pen1.color("Chartreuse")
    t5.dot(186,"Chartreuse")
    ti.sleep(x)     
    pen1.color("magenta")
    t6.dot(156,"magenta")
    ti.sleep(x)    
    pen1.color("blue")
    t7.dot(126,"blue")
    ti.sleep(x)
    pen1.color("yellow")
    t8.dot(96,"yellow")
    
    if count % 5 == 0:
         # pen1.color("Red")  
         # to hide the pointer by asigning the same color as that of dot

         
        
         t1.clear()
         ti.sleep(x)
         # pen1.color("darkviolet")
         t2.clear()
         ti.sleep(x)
         # pen1.color("cyan")
         t3.clear()
         ti.sleep(x)
         # pen1.color("orange")
         t4.clear()
         ti.sleep(x)
         # pen1.color("Chartreuse")
         t5.clear()
         ti.sleep(x)     
         # pen1.color("magenta")
         t6.clear()
         ti.sleep(x)    
         # pen1.color("blue")
         t7.clear()
         ti.sleep(x)
         # pen1.color("yellow")
         t8.clear()  
    
    if count % 9 == 0:
         # pen1.color("Red")  
         # to hide the pointer by asigning the same color as that of dot

         y=0.3
        
         t8.clear()
         ti.sleep(y)
         # pen1.color("darkviolet")
         t7.clear()
         ti.sleep(y)
         # pen1.color("cyan")
         t6.clear()
         ti.sleep(y)
         # pen1.color("orange")
         t5.clear()
         ti.sleep(y)
         # pen1.color("Chartreuse")
         t4.clear()
         ti.sleep(y)     
         # pen1.color("magenta")
         t3.clear()
         ti.sleep(y)    
         # pen1.color("blue")
         t2.clear()
         ti.sleep(y)
         # pen1.color("yellow")
         t1.clear()      
    
    
    t.clear()

    



t.done()