import turtle as t
import time as ti
import tkinter as tk
from tkinter import simpledialog
import winsound as wi


replay = 1

while replay ==1:       # for retrying
    screen = t.Screen()
    screen = t.setup(width=600, height=800)
    screen = t.bgpic("Bg_pic/Gif Format/view-illuminated-neon-gaming-keyboard-setup-controller.gif")



    pen1 = t.Turtle()
    pen1 = t.pencolor("white")

    pen_2 = t.Turtle()

    pen1 = t.width(5)
    pen1 = t.speed(10)
    pen1 = t.hideturtle()

    pen1 = t.backward(200)
    pen1 = t.forward(400)
    pen1 = t.backward(150)
    pen1 = t.left(90)
    pen1 = t.forward(150)
    pen1 = t.backward(400)
    pen1 = t.forward(250)
    pen1 = t.left(90)
    pen1 = t.forward(100)
    pen1 = t.right(90)
    pen1 = t.forward(150)
    pen1 = t.backward(400)
    pen1 = t.forward(150)
    pen1 = t.right(90)
    pen1 = t.backward(150)
    pen1 = t.forward(400)



    #_______________________________Box drawning is ended________________________________________


    # ______________________________Naming the Quadrants_________________________________________





    # ______________________________Quadrant 1________________________________________________________
    pen1 = t.penup()
    pen1 = t.goto(-110,60)
    pen1 = t.pendown()
    q1   = t.write("Q : 1", align="center", font=("Arial",24,"italic"))
    pen1 = t.hideturtle()

    # ______________________________Quadrant 2________________________________________________________
    pen1 = t.penup()
    pen1 = t.goto(0,60)
    pen1 = t.pendown()
    q2   = t.write("Q : 2", align="center", font=("Arial",24,"italic"))
    pen1 = t.hideturtle()


    # ______________________________Quadrant 3________________________________________________________
    pen1 = t.penup()
    pen1 = t.goto(110,60)
    pen1 = t.pendown()
    q3   = t.write("Q : 3", align="center", font=("Arial",24,"italic"))
    pen1 = t.hideturtle()


    # ______________________________Quadrant 4________________________________________________________
    pen1 = t.penup()
    pen1 = t.goto(-110,-60)
    pen1 = t.pendown()
    q4   = t.write("Q : 4", align="center", font=("Arial",24,"italic"))
    pen1 = t.hideturtle()


    # ______________________________Quadrant 5________________________________________________________

    pen1 = t.penup()
    pen1 = t.goto(0,-60)
    pen1 = t.pendown()
    q5   = t.write("Q : 5", align="center", font=("Arial",24,"italic"))
    pen1 = t.hideturtle()


    # ______________________________Quadrant 6________________________________________________________
    pen1 = t.penup()
    pen1 = t.goto(110,-60)
    pen1 = t.pendown()
    q6   = t.write("Q : 6", align="center", font=("Arial",24,"italic"))
    pen1 = t.hideturtle()


    # ______________________________Quadrant 7________________________________________________________

    pen1 = t.penup()
    pen1 = t.goto(-110,-180)
    pen1 = t.pendown()
    q7   = t.write("Q : 7", align="center", font=("Arial",24,"italic"))
    pen1 = t.hideturtle()


    # ______________________________Quadrant 8________________________________________________________
    pen1 = t.penup()
    pen1 = t.goto(0,-180)
    pen1 = t.pendown()
    q8   = t.write("Q : 8", align="center", font=("Arial",24,"italic"))
    pen1 = t.hideturtle()


    # ______________________________Quadrant 9________________________________________________________
    pen1 = t.penup()
    pen1 = t.goto(110,-180)
    pen1 = t.pendown()
    q9   = t.write("Q : 9", align="center", font=("Arial",24,"italic"))
    pen1 = t.hideturtle()



    # _________________________________Alert the user to use the quadrant name for play____________________

    # Hey! Note The Quadrant No And Use Them For Playing

    pen = t.Turtle()
    pen.pensize(5)
    pen.speed(1)
    pen.hideturtle()
    pen.color("white")
    x_axis = -630
    y_axis = 350
    pen.penup()
    pen.goto(x_axis,y_axis)
    pen.down()

    def typing_sound(duration=0.01,frequency=1500):
        #  duration is the period of sounding
        # frequency is of the sound
        wi.Beep(frequency,int(duration*1000))


    def alert(i):
        
            match i:
                case 1:
                    return 'H'
                case 2:
                    return 'e'
                case 3:
                    return 'y'
                case 4:
                    return '!'
                case 5:
                    return ' '
                case 6:
                    return 'N'
                case 7:
                    return 'o'
                case 8:
                    return 't'
                case 9:
                    return 'e'
                case 10:
                    return ' '
                case 11:
                    return 'T'
                case 12:
                    return 'h'
                case 13:
                    return 'e'
                case 14:
                    return ' '
                case 15:
                    return 'Q'
                case 16:
                    return 'u'
                case 17:
                    return 'a'
                case 18:
                    return 'd'
                case 19:
                    return 'r'
                case 20:
                    return 'a'
                case 21:
                    return 'n'
                case 22:
                    return 't'
                case 23:
                    return ' '
                case 24:
                    return 'N'
                case 25:
                    return 'o'
                case 26:
                    return ' '
                case 27:
                    return 'A'
                case 28:
                    return 'n'
                case 29:
                    return 'd'
                case 30:
                    return ' '            
                case 31:
                    return 'U'
                case 32:
                    return 's'
                case 33:
                    return 'e'
                case 34:
                    return ' '
                case 35:
                    return 'T'
                case 36:
                    return 'h'
                case 37:
                    return 'e'
                case 38:
                    return 'm'
                case 39:
                    return ' '
                case 40:
                    return 'F'
                case 41:
                    return 'o'
                case 42:
                    return 'r'
                case 43:
                    return ' '
                case 44:
                    return 'P'
                case 45:
                    return 'l'
                case 46:
                    return 'a'
                case 47:
                    return 'y'
                case 48:
                    return 'i'
                case 49:
                    return 'n'
                case 50:
                    return 'g'
                case 51:
                    return '.'
    

    
    for i in range(51):
        
        masg = alert(i+1)                   
        pen.penup()
        pen.goto(x_axis,y_axis)
        pen.down()
        pen.write(masg, font=("Arial", 24 ,"italic")) 
        if masg!=' ':
            typing_sound(duration=0.1,frequency=1500)
        x_axis = x_axis+25




    # ______________________________Clearing the Quadrants Names______________________________________



    ti.sleep(4)
    t.clear()

    # __________________________________Redrawing the boxes after clearing the quadrants name__________________

    pen1 = t.width(5)
    pen1 = t.penup()
    pen1 = t.goto(0,0)
    pen1 = t.pendown()
    pen1 = t.speed(10)

    pen1 = t.backward(200)
    pen1 = t.forward(400)
    pen1 = t.backward(150)
    pen1 = t.left(90)
    pen1 = t.forward(150)
    pen1 = t.backward(400)
    pen1 = t.forward(250)
    pen1 = t.left(90)
    pen1 = t.forward(100)
    pen1 = t.right(90)
    pen1 = t.forward(150)
    pen1 = t.backward(400)
    pen1 = t.forward(150)
    pen1 = t.right(90)
    pen1 = t.backward(150)
    pen1 = t.forward(400)

    


    # ___________________________________________Getting Quadrant No___________________________________________
    # j=1
    # Initialize the screen
    screen = t.Screen()
    screen.bgcolor("white")

    winner_1 = []
    winner_2 = []
    winner = []
    position = 0


    # Initialize the turtles
    pen1 = t.Turtle()
    pen1.pensize(5)
    pen1.speed(10)
    pen1.hideturtle()

    def get_quadrant_no(k):
        window = tk.Tk()
        window.withdraw()  # Hide the root window
        q_no = simpledialog.askinteger("Input", f"Player {k % 2 +1}, Enter an integer (1-9):")
        window.destroy()  # Destroy the root window
        return q_no

    # Draw the grid and labels (assuming draw_grid and draw_labels are defined elsewhere)
    # draw_grid()
    # draw_labels()

    for k in range(9):

        Q_No = get_quadrant_no(k)
        
        if Q_No not in range(1, 10):
            print("Invalid quadrant number, skipping...")
            continue
        
        labels = {
            1: (-110, 60),
            2: (0, 60),
            3: (110, 60),
            4: (-110, -60),
            5: (0, -60),
            6: (110,-60),
            7: (-110, -160),
            8: (0, -160),
            9: (110, -160)
        }
        
        x, y = labels.get(Q_No, (0, 0))
        
        pen1.penup()
        pen1.goto(x, y)
        pen1.pendown()
        pen1.pencolor("magenta" if k % 2 == 0 else "cyan")
        pen1.circle(10)
        pen1.hideturtle()

        if k % 2 == 0:
            if k >= len(winner_1): #_______IF the indices are lesser, then create more indices____________
                winner_1.extend([None]*(k+1- len(winner_1)))
                
            winner_1[k] = Q_No
        else:
            if k >= len(winner_2): #_______IF the indices are lesser, then create more indices____________
                winner_2.extend([None]*(k+1- len(winner_2)))        
            winner_2[k] = Q_No

    # __________________________________________Decleraing The Winner____________________________________
        
        def alert(i):
        
            match i:
                case 1:
                    return 'C'
                case 2:
                    return 'o'
                case 3:
                    return 'n'
                case 4:
                    return 'g'
                case 5:
                    return 'r'
                case 6:
                    return 'a'
                case 7:
                    return 't'
                case 8:
                    return 'u'
                case 9:
                    return 'l'
                case 10:
                    return 'a'
                case 11:
                    return 't'
                case 12:
                    return 'i'
                case 13:
                    return 'o'
                case 14:
                    return 'n'
                case 15:
                    return 's'
                case 16:
                    return '!'
                case 17:
                    return ' '
                case 18:
                    return 'T'
                case 19:
                    return 'h'
                case 20:
                    return 'e'
                case 21:
                    return ' '
                case 22:
                    return 'P'
                case 23:
                    return 'L'
                case 24:
                    return 'A'
                case 25:
                    return 'Y'
                case 26:
                    return 'E'
                case 27:
                    return 'R'
                case 28:
                    return '_'
                case 29:
                    return  w    #_____________w is defined below in winner condition 
                case 30:
                    return ' '
                case 31:
                    return 'I'            
                case 32:
                    return 's'
                case 33:
                    return ' '
                case 34:
                    return 'T'
                case 35:
                    return 'h'
                case 36:
                    return 'e'
                case 37:
                    return ' '
                case 38:
                    return 'W'
                case 39:
                    return 'i'
                case 40:
                    return 'n'
                case 41:
                    return 'n'
                case 42:
                    return 'e'
                case 43:
                    return 'r'
                case 44:
                    return '.'
        
        def alert_2(i):
            match i:
                case 1:
                    return 'O'
                case 2:
                    return 'H'
                case 3:
                    return '!'
                case 4:
                    return ' '
                case 5:
                    return 'Y'
                case 6:
                    return 'o'
                case 7:
                    return 'u'
                case 8:
                    return ' '
                case 9:
                    return 'B'
                case 10:
                    return 'o'
                case 11:
                    return 't'
                case 12:
                    return 'h'
                case 13:
                    return ' '
                case 14:
                    return 'C'
                case 15:
                    return 'o'
                case 16:
                    return 'n'
                case 17:
                    return 't'
                case 18:
                    return 'r'
                case 19:
                    return 'o'
                case 20:
                    return 'l'
                case 21:
                    return 'l'
                case 22:
                    return 'e'
                case 23:
                    return 'd'
                case 24:
                    return ' '
                case 25:
                    return 'E'
                case 26:
                    return 'a'
                case 27:
                    return 'c'
                case 28:
                    return  'h'    #_____________w is defined below in winner condition 
                case 29:
                    return ' '
                case 30:
                    return 'O'            
                case 31:
                    return 't'
                case 32:
                    return 'h'
                case 33:
                    return 'e'
                case 34:
                    return 'r'
                case 35:
                    return '.'
                case 36:
                    return ' '
                case 37:
                    return 'D'
                case 38:
                    return '0'
                case 39:
                    return ' '
                case 40:
                    return 'Y'
                case 41:
                    return 'o'
                case 42:
                    return 'u'
                case 43:
                    return ' '       
                case 44:
                    return 'W'
                case 45:
                    return 'a'
                case 46:
                    return 'n'
                case 47:
                    return 't'
                case 48:
                    return ' '
                case 49:
                    return 'T'
                case 50:
                    return 'o'
                case 51:
                    return ' '
                case 52:
                    return 'P'
                case 53: 
                    return 'l'      
                case 54:
                    return 'a'
                case 55:
                    return 'y'
                case 56:
                    return ' '
                case 57:
                    return 'A'
                case 58:
                    return 'g'
                case 59:
                    return 'a'
                case 60:
                    return 'i'
                case 61:
                    return 'n'
                case 62:
                    return '.'


        def winning_line(winner):
            pen1.up()
            for i in winner:
                position = labels.get(i)
                    
                if position is not None:
                    x,y = position    
                    pen1.down()
                    pen1.goto(x,y)
    
                


        
        def winner (player_tik):
            winning_combination = [                           #_________Array Type________________________ 
                                {1,2,3},{4,5,6},{7,8,9},   #_________Row
                                {1,4,7},{2,5,8},{3,6,9},   #_________Column
                                {1,5,9},{3,5,7}            #_________Diagonal
                                ]
            
            player_set = set(player_tik)      #_____A set(math) of Player_tik is made and then assigned to player_set
            for comb in winning_combination:
                if comb.issubset(player_set):
                    return True
            return False     
                
                
        if winner(winner_1): #____The value of winner_1 passes to player_moves and the functions(winner) is run
                    
                    pen1.up()
                    winner = set(winner_1)
                    winning_line(winner)
                    # for i in winner_1:
                    #     x,y = labels.get(Q_No)
                    #     pen1.down()
                    #     pen1.goto(x,y)
                    
                    
                    pen.penup()
                    x_axis = -600
                    y_axis = -350
                    
                    pen.goto(-200,-350)
                    pen.pendown()
                    pen.hideturtle()
                    # pen.write("Congratulations! The Player 1 Is The Winner", align="center", font=("Arial", 24 , "italic"))
                    
                  
                    w=1    #_______To print the player no
                    
                    for i in range(43):
        
                        masg = alert(i+1)                   
                        pen.penup()
                        
                        # if i == 38:
                        #     x_axis = x_axis+20   #____For proper printing of i
                        # if i == 39:
                        #     x_axis = x_axis-30   #____For proper printing of other than i                    
                        
                        pen.goto(x_axis,y_axis)
                        pen.down()
                        pen.write(masg, font=("Arial", 24 ,"italic"))
                        if masg!=' ': 
                            typing_sound(duration=0.05,frequency=1500)

                        
                        x_axis = x_axis+25
                    

                    break

        elif winner(winner_2):
            
                    winner = set(winner_2)
                    winning_line(winner)
            
            
                    pen.penup()
                    x_axis = -600
                    y_axis = -350                
                    
                    pen.goto(x_axis,y_axis)
                    pen.pendown()
                    pen.hideturtle()
                    # pen.write("Congratulations! The Player 1 Is The Winner", align="center", font=("Arial", 24 , "italic")) 
                    
                    w=2  #_______To print the player no
                    
                    for i in range(43):
        
                        masg = alert(i+1)                   
                        pen.penup()
                   
                        
                        pen.goto(x_axis,y_axis)
                        pen.down()
                        pen.write(masg, font=("Arial", 24 ,"italic")) 
                        if masg!=' ':   
                            typing_sound(duration=0.05,frequency=1500)
                        x_axis = x_axis+25                
                    

                    
                    break




  
# ________________________________________________Button for replay________________________________________
    replay = 0
    
    def assigning_true():
        replay = 1
    def assigning_false():
        replay = 0
    
    main_window = tk.Tk()   # main_window = tk.Tk(): Creates the main application window. tk.Tk() initializes the Tkinter framework and creates the root window, which serves as the main container for all other GUI elements.
    frame = tk.Frame(main_window)  # frame = tk.Frame(parent): Creates a Frame widget, which is a container used to organize other widgets. parent is the root window, so the Frame is a child of the main application window.
    frame.pack()     # frame.pack(): Packs the Frame widget into the window using the pack geometry manager. This makes the Frame visible and positions it within the parent window.

    replay_button = tk.Button(frame,
                              text="Replay",
                              foreground="green",
                              command = assigning_true)
    replay_button.pack(side= tk.LEFT)
    
    quit_button = tk.Button(frame,
                            text="Quit",
                            foreground="red",
                            command = assigning_false )
    quit_button.pack(side=tk.RIGHT)
    
    if replay == 1:
       t.clear()


t.done()