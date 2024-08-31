import turtle as t
import time as ti
import tkinter as tk
from tkinter import simpledialog
import winsound as wi


global replay  #______taken globally so that can be used in each function and can be updated correctly in button 
replay = True

while replay == True:       # for retrying
    screen = t.Screen()
    screen = t.setup(width=600, height=800)
    screen = t.bgpic("Bg_pic/Gif Format/view-illuminated-neon-gaming-keyboard-setup-controller.gif")



    pen1 = t.Turtle()
    
    def draw_Boxes():
        pen1 = t.pencolor("white")

        pen_2 = t.Turtle()

        pen1 = t.width(5)
        pen1 = t.penup()
        pen1 = t.goto(0,0)
        pen1 = t.pendown()        
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

    draw_Boxes()

    # ______________________________Naming the Quadrants_________________________________________

    def typing_sound(duration,frequency):
        #  duration is the period of sounding
        # frequency is of the sound
        wi.Beep(frequency,int(duration*1000))


    # ______________________________Naming_Quadrant________________________________________________________
    def Name_Quadrants():
        x = -110
        y = 60
        for i in range(1,10,1):
            pen1 = t.speed(10)
                       
            pen1 = t.penup()
            pen1 = t.goto(x,y)
            pen1 = t.pendown()
            q1   = t.write(f"Q :{i}", align="center", font=("Arial",24,"italic"))
            typing_sound(duration=0.3,frequency=2000)
            pen1 = t.hideturtle()
            x += 110
            
            if i % 3 == 0:
                y -= 120
                x -= 3*110
    
    
    Name_Quadrants()        

    # _________________________________Alert the user to use the quadrant name for play____________________

    # Hey! Note The Quadrant No And Use Them For Playing

    pen = t.Turtle()
    pen.pensize(5)
    pen.speed(7)
    pen.hideturtle()
    pen.color("white")
    x_axis = -630
    y_axis = 350
    pen.penup()
    pen.goto(x_axis,y_axis)
    pen.down()




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
            typing_sound(duration=0.06,frequency=1500)
        x_axis = x_axis+25




    # ______________________________Clearing the Quadrants Names______________________________________



    ti.sleep(4)
    t.clear()

    # __________________________________Redrawing the boxes after clearing the quadrants name__________________

    draw_Boxes()

    


    # ___________________________________________Getting Quadrant No___________________________________________
    # j=1
    # Initialize the screen
    screen = t.Screen()
    screen.bgcolor("white")

    winner_1 = []
    winner_2 = []
    winner = []
    position = 0
    check_overwrite = []
    win_line = []



    # Initialize the turtles
    pen1 = t.Turtle()
    pen1.pensize(5)
    pen1.speed(10)
    pen1.hideturtle()

    def get_quadrant_no(k):
        window = tk.Tk()
        window.withdraw()  # Hide the root window
        q_no = simpledialog.askinteger("Input", f"Player {k % 2 +1}, Enter an integer (1-9):\nTry NO # {k+1}")
        window.destroy()  # Destroy the root window
        return q_no

    # Draw the grid and labels (assuming draw_grid and draw_labels are defined elsewhere)
    # draw_grid()
    # draw_labels()

    for k in range(9):

        Q_No = get_quadrant_no(k)
        
        
        if Q_No not in check_overwrite:

            
            check_overwrite.append(Q_No)
            
            if Q_No not in range(1, 10):
                print("Invalid quadrant number, skipping...")
                k = k - 1               #___It makes the loop to iterate thruogh 9 times even when the continue statement is run
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
            typing_sound(duration=0.1,frequency=4000)
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

        else:
            print("The Quadrant is already used:")
            k = k - 1            #___It makes the loop to iterate thruogh 9 times even when the continue statement is run
            continue
            
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
                    typing_sound(duration=0.1,frequency=37)
                    pen1.goto(x,y)
    
                


        
        def winner (player_tik):
            winning_combination = [                        #_________Array Type________________________ 
                                {1,2,3},{4,5,6},{7,8,9},   #_________Row
                                {1,4,7},{2,5,8},{3,6,9},   #_________Column
                                {1,5,9},{3,5,7}            #_________Diagonal
                                ]
            
            player_set = set(player_tik)      #_____A set(math) of Player_tik is made and then assigned to player_set
            for comb in winning_combination:
                if comb.issubset(player_set):
                    win_line = comb
                    return True
            return False     
                
                
        if winner(winner_1): #____The value of winner_1 passes to player_moves and the functions(winner) is run
                    
                    pen1.up()
                    winner = set(winner_1)
                    winning_line(winner)
                    # winning_line(win_line)
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
                    # winning_line(win_line)
            
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
        global replay
        replay = True
    def assigning_false():
        global replay
        replay = False
    
    def button():
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
                                command = quit )
        quit_button.pack(side=tk.RIGHT)
        return replay
        
        
    button = button()
    
    if replay == True:
       t.clear()


t.done()