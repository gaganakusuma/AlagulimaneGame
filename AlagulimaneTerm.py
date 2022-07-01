# from this import s
import pygame
import time
import sys
import os
from pygame.locals import *
#import turtle

# GUI variables and functions
pygame.init()
width = 800  # wIDTH OF THE Display
height = 600  # HEIGHT OF THE SCREEEN
Display = pygame.display.set_mode((width, height))  # DISPLAY SURFACE OBJECT
pygame.display.set_caption("Alagulimane")  # CAPTION
clock = pygame.time.Clock()  # TIME OBJECT

white = (255, 255, 255)
l_red = (255, 0, 0)
red = (150, 0, 0)
l_green = (0, 255, 0)
green = (0, 150, 0)
yellow = (255, 229, 10)
l_yellow = (212, 255, 10)
black = (0, 0, 0)
orange = (255, 165, 0)
BlurryWood = (222, 184, 135)
BrownGrey = (222,214,211)
Plum = (255,205,116)


# Functions for BOARD COMPONENTS
def ReturnStoneImage(value):
    if value == 0:
        return he
    elif value == 1:
        return h1
    elif value == 2:
        return h2
    elif value == 3:
        return h3
    elif value == 4:
        return h4
    elif value == 5:
        return h5  
    elif value == 6:
        return h6
    elif value == 7:
        return h7
    elif value ==8:
        return h8
    elif value ==9:
        return h9
    elif value ==10:
        return h10
    elif value ==11:
        return h11
    elif value>=12:
        return h12

def ReturnStoreImage(value):
    if value == 0:
        return se 
    elif value == 1:
        return s1
    elif value == 2:
        return s2
    elif value == 3:
        return s3
    elif value == 4:
        return s4
    elif value == 5:
        return s5
    elif value > 5:
        return sm

def UpdateDisplay(state):
    # Stones on the board
    hole14=ReturnStoneImage(state[14])
    hole13=ReturnStoneImage(state[13])
    hole12 = ReturnStoneImage(state[12])
    hole11 = ReturnStoneImage(state[11])
    hole10 = ReturnStoneImage(state[10])
    hole9 = ReturnStoneImage(state[9])
    hole8 = ReturnStoneImage(state[8])
    hole7 = ReturnStoneImage(state[6])
    hole6 = ReturnStoneImage(state[5])
    hole5 = ReturnStoneImage(state[4])
    hole4 = ReturnStoneImage(state[3])
    hole3 = ReturnStoneImage(state[2])
    hole2 = ReturnStoneImage(state[1])
    hole1 = ReturnStoneImage(state[0])
    
    
    Display.blit(WoodBackground,(0,0))
    display_message("Alagulimane",30,400,50,Plum)
    Display.blit(board,(27,150))
    Display.blit(hole14, (61,183)) # 237x167
    Display.blit(hole13, (157,183)) # 237x167
    Display.blit(hole12, (263,183)) # 294x167
    Display.blit(hole11, (359,183)) # 351x167
    Display.blit(hole10, (455,183)) # 455x167
    Display.blit(hole9, (556,183)) # 512x167
    Display.blit(hole8, (652,183)) # 569x167
    # bottom row 1-6
    Display.blit(hole1, (61,307)) #237x234
    Display.blit(hole2, (157,307)) #294x234
    Display.blit(hole3, (263,307)) #351x234
    Display.blit(hole4, (359,307)) #455x234
    Display.blit(hole5, (455,307)) #521x234
    Display.blit(hole6, (556,307)) #569x234
    Display.blit(hole7, (652,307)) #569x234

    #stores
    Display.blit(s, (687,50)) #569x234
    Display.blit(s, (51,430)) #569x234
    
    store1 = ReturnStoneImage(state[7])
    store2 = ReturnStoneImage(state[15])
    Display.blit(store2, (692,70)) #173x232
    Display.blit(store1, (66,450)) #629x232

    #displaying the no. of beans in each pit for ease of playing
    display_message(str(state[14]),30,109,160,BrownGrey)
    display_message(str(state[13]),30,203,160,BrownGrey)
    display_message(str(state[12]),30,309,160,BrownGrey)
    display_message(str(state[11]),30,405,160,BrownGrey)
    display_message(str(state[10]),30,501,160,BrownGrey)
    display_message(str(state[9]),30,605,160,BrownGrey)
    display_message(str(state[8]),30,698,160,BrownGrey)
    display_message(str(state[0]),30,109,420,BrownGrey)
    display_message(str(state[1]),30,203,420,BrownGrey)
    display_message(str(state[2]),30,309,420,BrownGrey)
    display_message(str(state[3]),30,405,420,BrownGrey)
    display_message(str(state[4]),30,501,420,BrownGrey)
    display_message(str(state[5]),30,605,420,BrownGrey)
    display_message(str(state[6]),30,698,420,BrownGrey)


    display_message(str(state[7]),30,105,550,BrownGrey)
    display_message(str(state[15]),30,742,50,BrownGrey)




    pygame.display.flip()
    time.sleep(1)

# loading images from source file
#i2a = pygame.image.load("2a.jpg") 
WoodBackground = pygame.image.load("WoodBackground.jpg")
board = pygame.image.load("board.png")
he_path = os.path.join("images","e1.png") 
he = pygame.image.load(he_path)
h1_path = os.path.join("images","1h.png") 
h1 = pygame.image.load(h1_path)
h2_path = os.path.join("images","2h.png") 
h2 = pygame.image.load(h2_path)
h3_path = os.path.join("images","3h.png") 
h3 = pygame.image.load(h3_path)
h4_path = os.path.join("images","4h.png") 
h4 = pygame.image.load(h4_path)
h5_path = os.path.join("images","5h.png") 
h5 = pygame.image.load(h5_path)
h6_path = os.path.join("images","6h.png") 
h6 = pygame.image.load(h6_path)
h7_path = os.path.join("images","7h.png") 
h7 = pygame.image.load(h7_path)
h8_path = os.path.join("images","8h.png") 
h8 = pygame.image.load(h8_path)
h9_path = os.path.join("images","9h.png") 
h9 = pygame.image.load(h9_path)
h10_path = os.path.join("images","10h.png") 
h10 = pygame.image.load(h10_path)
h11_path = os.path.join("images","11h.png") 
h11 = pygame.image.load(h11_path)
h12_path = os.path.join("images","12h.png") 
h12 = pygame.image.load(h12_path)
s_path = os.path.join("images","s.png") 
s = pygame.image.load(s_path)
'''h14_path = os.path.join("images","14h.png") 
h14 = pygame.image.load(h14_path)
h15_path = os.path.join("images","15h.png") 
h15 = pygame.image.load(h15_path)
hm_path = os.path.join("images","m.jpg") 
hm = pygame.image.load(hm_path)

se_path = os.path.join("images","se.jpg") 
se = pygame.image.load(se_path)

s1_path = os.path.join("images","s1.jpg") 
s1 = pygame.image.load(s1_path)
s2_path = os.path.join("images","s2.jpg") 
s2 = pygame.image.load(s2_path)
s3_path = os.path.join("images","s3.jpg") 
s3 = pygame.image.load(s3_path)
s4_path = os.path.join("images","s4.jpg") 
s4 = pygame.image.load(s4_path)
s5_path = os.path.join("images","s5.jpg") 
s5 = pygame.image.load(s5_path)
sm_path = os.path.join("images","sm.jpg") 
sm = pygame.image.load(sm_path)'''



mousex,mousey = 0,0
clickx,clixky = 0,0
MouseClicked = False
def Interactive(centerx,centery,radius,icolor,acolor,message):
    global mousex,mousey
    
            
    # print (mousex,mousey)
    lights(centerx,centery,radius,acolor)
    display_message(message,20,centerx,centery+50,black)
        
    

def lights(centerx,centery,radius,color):
        pygame.draw.circle(Display,color,(centerx,centery),radius)

def display_message(text,size,x,y,color):
    TextObj = pygame.font.Font("freesansbold.ttf",size)
    TextSurf = TextObj.render(text,True,color)
    RectSurf = TextSurf.get_rect()
    RectSurf.center=(x,y)
    Display.blit(TextSurf, RectSurf)
    pygame.display.update()


# The game logic
postive_infnity = float('inf')
negative_infnity = float('-inf')
stealing = 1
playerturn = 1
ai_turn = 0

flag=0
boul=16

def available_moves(state,player): 
        moves = []
        if(player):
            i = 0
            for move in state[0:7]:
                if(move != 0):
                    moves.append(i)
                i += 1
        else:
            i = 8
            for move in state[8:15]:
                if(move != 0):
                    moves.append(i)
                i += 1
        return moves

def get_children(state,player): 
    global ai_turn
    constant_turn = ai_turn
    children = []
    for move in available_moves(state,player):
        new_state = state[:]
        makemove(new_state,move,player,1)
        children.append([new_state,move,ai_turn])
        ai_turn = constant_turn
    return children


def Maxmin(state, depth, maximizingplayer, alpha = negative_infnity, beta = postive_infnity , counter=0) :
    global ai_turn
    global flag
    flag=1
    counter += 1
    if depth == 0 or not(end_game(state)):
        return state[7]-state[15]
    if maximizingplayer :
        ai_turn = 1
        value = negative_infnity
        # values = []
        for child in get_children(state,1) :
            new_value = Maxmin(child[0] , depth - 1, child[2] , alpha , beta , counter)
            # values.append(new_value)
            if(new_value > value):
                value = new_value
                move = child[1]
            alpha = max(alpha , value)
            if alpha >= beta:
                break
        if(counter==1):
            return move
        # print(depth,values)
        # flag=flag+1
        # print("F",flag)
        return value
    else :
        # values = []
        value =  postive_infnity
        ai_turn = 0
        for child in get_children(state,0) :
            new_value = Maxmin(child[0] , depth - 1, child[2] , alpha , beta , counter)
            # values.append(new_value)
            if(new_value < value):
                value = new_value
                move = child[1]
            beta = min(beta , value)
            if beta <= alpha :
                break
        if(counter==1):
            return move
        """print(value)
        print(depth,values)
        flag=flag+1
        print("F",flag)"""
        return value


def end_game (moves): 
    sideOne = 0
    sideTwo = 0
    for j in range(7):
        sideOne = int(sideOne) + int(moves[j])
        sideTwo = int(sideTwo) + int(moves[j+8])

    if(int(sideOne) == 0 or int(sideTwo) == 0):
        return False
    else:
        return True
        

def winning_message(moves): 
    #print("")
    #print("The game is over!")
    if int(moves[15]) < int(moves[7]):
        #print("Player One has won the game!")
        display_message("Player One Wins! :)", 40,600,500,BlurryWood)
        pygame.display.flip()
    elif int(moves[15]) > int(moves[7]):
        #print("Player Two has won the game!")
        display_message("Player Two Wins! :)", 40,600,500,BlurryWood)
        pygame.display.flip()
    else:
        #print("The game ended in a tie.")
        display_message("It's a tie..:)", 40,600,500,BlurryWood)
        pygame.display.flip()
        time.delay(3)

    Interactive(400,540,20,red,l_red,"Quit")
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                clickx,clicky = pygame.mouse.get_pos()
                MouseClicked = True
                print(clickx,clicky)
                if clickx > 380 and clickx < (380 + 40) and clicky > 520 and clicky < (520 + 40) and MouseClicked == True:
                    MouseClicked = False
                    pygame.display.quit()

    


def player_move(moves,player): 
    chosenBin = -1
    messageCode = 0
    message = " "
    invaled_input = False
    giveawayPile = -1
    global flag
    while (not(invaled_input)):
        if player == 1 and  messageCode == 0:
            # print the message................
            display_message("Player One's Turn", 40,600,500,BlurryWood)
            pygame.display.flip()
        elif player == 2 and messageCode == 0:
            display_message("Player Two's Turn", 40,600,500,BlurryWood)
            pygame.display.flip()
        elif player == 1 and messageCode == -2:
            message = "Invalid input. Try again, Player One."
        elif player == 2 and messageCode == -2:
            message = "Invalid input. Try again, Player Two."
        elif player == 1 and messageCode == -1:
            display_message("Player One's Turn", 40,600,500,BlurryWood)
            display_message("You must choose a non-empty bin",20,600,575,BlurryWood)
            pygame.display.flip()
        elif player == 2 and messageCode == -1:
            display_message("Player Two's Turn", 40,600,500,BlurryWood)
            display_message("You must choose a non-empty bin", 20,600,575,BlurryWood)
            pygame.display.flip()
        message  =  "message is on the pygame window"
        print("")
        print(message)
        print("")

        messageCode = 0 
        global MouseClicked
        userInput = 0
        if player == 1:
            # userInput = input("Enter a number to choose a bin or enter 'q' to QUIT: ")
           # CLICK functionality for player 1 needs to be provided
           # ....................................IMP>..........................................
           # ...................................................................................
            #print("testing for the click working for player 1 ")
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        clickx,clicky = pygame.mouse.get_pos()
                        MouseClicked = True
                        #print(clickx,clicky)
                        if clickx > 41 and clickx <= 147 and clicky > 297 and clicky < 393 and MouseClicked == True:
                            MouseClicked = False
                            userInput = 0
                            #print("Bowl 1 was chosen")
                            run = False
                            # break
                        elif clickx > 147 and clickx <= 253 and clicky > 297 and clicky < 393 and MouseClicked == True:
                            MouseClicked = False
                            userInput = 1
                            run = False
                            # break
                        elif clickx > 253 and clickx <= 359 and clicky > 297 and clicky < 393 and MouseClicked == True:
                            MouseClicked = False
                            userInput = 2
                            run = False
                            # break
                        elif clickx > 359 and clickx <=465 and clicky > 297 and clicky < 393 and MouseClicked == True:
                            MouseClicked = False
                            userInput = 3
                            run = False
                            # break
                        elif clickx > 465 and clickx <= 571 and clicky > 297 and clicky < 393 and MouseClicked == True:
                            MouseClicked = False
                            userInput = 4
                            run = False
                            # break
                        elif clickx > 571 and clickx <= 677 and clicky > 297 and clicky < 393 and MouseClicked == True:
                            MouseClicked = False
                            userInput = 5
                            run = False
                            # break
                        elif clickx > 677 and clickx <= 783 and clicky > 297 and clicky < 393 and MouseClicked == True:
                            MouseClicked = False
                            userInput = 6
                            run = False
                            # break
                        # break
                
            if userInput == "q":
                chosenBin = 15
                return chosenBin
            elif userInput == 6:
                chosenBin = 6
            elif userInput == 5:
                chosenBin = 5
            elif userInput == 4:
                chosenBin = 4
            elif userInput == 3:
                chosenBin = 3
            elif userInput == 2:
                chosenBin = 2
            elif userInput == 1:
                chosenBin = 1
            elif userInput == 0:
                chosenBin = 0
            else:
                chosenBin = -2
                messageCode = -2  # invalid input

        elif player == 2 :
            # userInput = input("Enter a number to choose a bin or enter 'q' to QUIT: ")
            # CLICK functionality for player 1 needs to be provided
            # ....................................IMP>..........................................
            # ...................................................................................
            #print("testing loop for player 2")
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        clickx,clicky = pygame.mouse.get_pos()
                        MouseClicked = True
                        # print(clickx,clicky)
                        if clickx > 41 and clickx <= 147 and clicky > 173 and clicky < 270 and MouseClicked == True:
                            MouseClicked = False
                            userInput = 0
                            run = False
                            # break
                        elif clickx > 147 and clickx <= 253 and clicky > 173 and clicky < 270 and MouseClicked == True:
                            MouseClicked = False
                            userInput = 1
                            run = False
                            # break
                        elif clickx > 253 and clickx <= 359 and clicky > 173 and clicky < 270 and MouseClicked == True:
                            MouseClicked = False
                            userInput = 2
                            run = False
                            # break
                        elif clickx > 359 and clickx <=465 and clicky > 173 and clicky < 270 and MouseClicked == True:
                            MouseClicked = False
                            userInput = 3
                            run = False
                            # break
                        elif clickx > 465 and clickx <= 571 and clicky > 173 and clicky < 270 and MouseClicked == True:
                            MouseClicked = False
                            userInput = 4
                            run = False
                            # break
                        elif clickx > 571 and clickx <= 677 and clicky > 173 and clicky < 270 and MouseClicked == True:
                            MouseClicked = False
                            userInput = 5
                            run = False
                            # break
                        elif clickx > 677 and clickx <= 783 and clicky > 173 and clicky < 393 and MouseClicked == True:
                            userInput = 6
                            run = False
                            # break

            if userInput == "q":
                chosenBin = 15
                return chosenBin
            elif userInput == 0:
                chosenBin = 14
            elif userInput == 6:
                chosenBin = 8
            elif userInput == 5:
                chosenBin = 9
            elif userInput == 4:
                chosenBin = 10
            elif userInput == 3:
                chosenBin = 11
            elif userInput == 2:
                chosenBin = 12
            elif userInput == 1:
                chosenBin = 13
            else:
                chosenBin = -2
                messageCode = -2  # invalid input

        if int(chosenBin) >= 0:
            giveawayPile = moves[chosenBin]
            if int(giveawayPile) <= 0:
                messageCode = -1  # empty bin was chosen
            else :
                invaled_input = True
                flag=flag+1
                #print("checking for infinite loop")
                return chosenBin


def makemove(state,move,player,test_mode): 
    global playerturn
    global ai_turn
    global flag
    global boul
    i = move
    # print(i)
    amount = state[move]
    state[move] = 0
    while(amount):
        flag=flag+1
        i += 1 
        if(player == 1):
            if( i%16 == 7 or i%16==15):
                    continue
        if(player == 0):
            if(i%16==7 or i%16==15):
                    continue
        state[i%16] += 1
        amount -= 1
    
    boul=(i+1)%16
    if(boul==7):
            boul=boul+1
    elif(boul==15):
            boul=0
    # print(boul)

    if(state[0] == 0 and state[1] == 0 and state[2] == 0 and state[3] == 0 and state[4] == 0 and state[5] == 0 and state[6] ==0):
        state[15] = state[13] + state[14] + state[8] + state[9] + state[10] + state[11] + state[12] +state[15]
        state[13] = 0
        state[8] = 0
        state[9] = 0
        state[10] = 0
        state[11] = 0
        state[12] = 0
        state[14]=0



    if(state[13] == 0 and state[8] == 0 and state[9] == 0 and state[10] == 0 and state[11] == 0 and state[12] == 0 and state[14]==0):
        state[7] = state[6] + state[0] + state[1] + state[2] + state[3] + state[4] + state[5]+state[7]
        state[0] = 0
        state[1] = 0
        state[2] = 0
        state[3] = 0
        state[4] = 0
        state[5] = 0
        state[6]=0

    if(player == 1 and state[boul]==0 and not(test_mode)):
        playerturn =  int(not(playerturn))
        if(boul==14 or boul==6):
                state[7]=state[(boul+2)%16]+state[7]
                state[(boul+2)%16]=0
                also=(boul+2)%16
                dif=abs(also-7)
                if(also<7):
                    state[7]=state[7+dif]+state[7]
                    state[7+dif]=0
                    # print(7+dif)
                else:
                    state[7]=state[7-dif]+state[7]
                    state[7-dif]=0
                    # print(7-dif)
        else:
                state[7]=state[(boul+1)%16]+state[7]
                state[(boul+1)%16]=0
                also=(boul+1)%16
                dif=abs(also-7)
                if(also<7):
                    state[7]=state[7+dif]+state[7]
                    state[7+dif]=0
                    # print(7+dif)
                else:
                    state[7]=state[7-dif]+state[7]
                    state[7-dif]=0
                    # print(7-dif)
        # add the shells from opposite boul too!
        flag=0
        boul=16
        
        return
    if(player == 0 and state[boul]==0 and not(test_mode)):
        playerturn =  int(not(playerturn))
        if(boul==14 or boul==6):
                state[15]=state[(boul+2)%16]+state[15]
                state[(boul+2)%16]=0
                also=(boul+2)%16
                dif=abs(also-7)
                if(also<7):
                    state[15]=state[7+dif]+state[15]
                    state[7+dif]=0
                    # print(7+dif)
                else:
                    state[15]=state[7-dif]+state[15]
                    state[7-dif]=0
                    # print(7-dif)
        else:
                state[15]=state[(boul+1)%16]+state[15]
                state[(boul+1)%16]=0
                also=(boul+1)%16
                dif=abs(also-7)
                if(also<7):
                    state[15]=state[7+dif]+state[15]
                    state[7+dif]=0
                    # print(7+dif)
                else:
                    state[15]=state[7-dif]+state[15]
                    state[7-dif]=0
                    # print(7-dif)
        flag=0
        boul=16
        
        return
    if(player == 1 and state[boul]==0 and test_mode):
        ai_turn =  int(not(ai_turn))
        if(boul==14 or boul==6):
                state[7]=state[(boul+2)%16]+state[7]
                state[(boul+2)%16]=0
                also=(boul+2)%16
                dif=abs(also-7)
                if(also<7):
                    state[7]=state[7+dif]+state[7]
                    state[7+dif]=0
                    # print(7+dif)
                else:
                    state[7]=state[7-dif]+state[7]
                    state[7-dif]=0
                    # print(7-dif)
        else:
                state[7]=state[(boul+1)%16]+state[7]
                state[(boul+1)%16]=0
                also=(boul+1)%16
                dif=abs(also-7)
                if(also<7):
                    state[7]=state[7+dif]+state[7]
                    state[7+dif]=0
                    # print(7+dif)
                else:
                    state[7]=state[7-dif]+state[7]
                    state[7-dif]=0
                    # print(7-dif)
        flag=0
        boul=16
        
        return
    if(player == 0 and state[boul]==0 and test_mode):
        ai_turn =  int(not(ai_turn))
        if(boul==14 or boul==6):
            state[15]=state[(boul+2)%16]+state[15]
            state[(boul+2)%16]=0
            also=(boul+2)%16
            dif=abs(also-7)
            if(also<7):
                state[15]=state[7+dif]+state[15]
                state[7+dif]=0
                # print(7+dif)
            else:
                state[15]=state[7-dif]+state[15]
                state[7-dif]=0
                # print(7-dif)
        else:
            state[15]=state[(boul+1)%16]+state[15]
            state[(boul+1)%16]=0
            also=(boul+1)%16
            dif=abs(also-7)
            if(also<7):
                state[15]=state[7+dif]+state[15]
                state[7+dif]=0
                # print(7+dif)
            else:
                state[15]=state[7-dif]+state[15]
                state[7-dif]=0
                # print(7-dif)
        flag=0
        boul=16
        
        return


def show_game(state): 
    print("|----0--1--2--3--4--5--6----|")
    print("|[{}]({})({})({})({})({})({})({})[ ]|".format(state[15],state[14],state[13],state[12],state[11],state[10],state[9],state[8]))
    print("|[ ]({})({})({})({})({})({})({})[{}]|".format(state[0],state[1],state[2],state[3],state[4],state[5],state[6],state[7]))
    print("|----0--1--2--3--4--5--6----|")
    print("++++++++++++++++++++++++++")
    UpdateDisplay(state)
    # turtle.delay(500)

def game(player1,player2,diffculty=6): 
    Display.blit(WoodBackground,(0,0))
    display_message("Alagulimane",30,400,100,Plum)
    Display.blit(board,(22,150))
    pygame.display.update()
    state =[5,5,5,5,5,5,5,0,5,5,5,5,5,5,5,0]
    game_not_finished = True
    quit = False
    show_game(state)
    global flag
    while(game_not_finished):
        if(playerturn):
            if(player1 == 1): #ai player
                if(flag<2):
                    move = Maxmin(state,diffculty,0)
                    #print("")
                    #print("")
                    # print("M",move)
                if(flag==1):
                    # print("here")
                    makemove(state,move,1,0)
                else:
                    if(flag>=2):
                            makemove(state,boul,1,0)
            if(player1 == 0): #human player
                if(flag<2):
                    move = player_move(state,1)
                    #print("")
                    #print("")
                # print(flag)
                    if(move == 15):
                        quit = True
                        break
                if(flag==1):
                    # print(flag)
                    makemove(state,move,1,0)
                else:
                    if(flag>=2):
                        # print(flag)
                        makemove(state,boul,1,0)
        else:
            if(player2 == 1): #ai player
                if(flag<2):
                    move = Maxmin(state,diffculty,0)
                    #print("")
                    #print("")
                    # print("M",move)
                if(flag==1):
                        # print("here0")
                        makemove(state,move,0,0)
                else:
                    if(flag>=2):
                            # print("nothere0")
                            makemove(state,boul,0,0)
            if(player2 == 0): #human player
                if(flag<2):
                        move = player_move(state,2)
                        #print("")
                        #print("")
                        if(move == 15):
                            quit = True
                            break
                if(flag==1):
                        makemove(state,move,0,0)
                else:
                        if(flag>=2):
                                makemove(state,boul,0,0)
        show_game(state)
        game_not_finished = end_game(state)
    if(quit):
        return
    winning_message(state)


easy = 2
medium = 6
hard = 10


def Entry_Display():  
    global MouseClicked 
    mode = 0
    '''print("1. human against human")
    print("2. human against ai")
    print("3. exit")'''

        # userinput = input("choose which mode to play: ")
    Display.blit(WoodBackground,(0,0))
    display_message("Alagulimane",70,400,100,Plum)
    display_message("Made By: TEAM A5 ",20,650,20,Plum)
    Interactive(250,450,20,green,l_green,"Human vs Human")
    Interactive(400,450,20,yellow,l_yellow,"Human vs AI")
    Interactive(550,450,20,red,l_red,"Quit")
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                clickx,clicky = pygame.mouse.get_pos()
                MouseClicked = True
                print(clickx,clicky)
                if clickx > 230 and clickx < (230 + 40) and clicky > 430 and clicky < (430 + 40) and MouseClicked == True:
                    MouseClicked = False
                    Display2(1)
                elif clickx > 380 and clickx < (380 + 40) and clicky > 430 and clicky < (430 + 40) and MouseClicked == True:
                    MouseClicked = False
                    Display2(2)
                    
                elif clickx > 530 and clickx < (530 + 40) and clicky > 430 and clicky < (430 + 40) and MouseClicked == True:
                    MouseClicked = False
                    Display2(3)

        
    
def Display2(userinput):
    global MouseClicked
    if(userinput == 1):
        mode = 1
        # break
    elif(userinput == 2):
        mode = 2
        # break
    elif(userinput == 3):
        pygame.quit()
        # break
    else:
        print("please enter valid input\n")
    if(mode == 1):
        turn = 0
        Display.blit(WoodBackground,(0,0))
        display_message("Alagulimane",70,400,100,Plum)
        display_message("Made By: TEAM A5 ",20,650,20,Plum)
        display_message("Which Player should start, One or Two?",30,400,300,black)
        Interactive(250,450,20,green,l_green,"Player 1")
        Interactive(400,450,20,yellow,l_yellow,"Player 2")
        Interactive(550,450,20,red,l_red,"Quit")
        pygame.display.update()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    clickx,clicky = pygame.mouse.get_pos()
                    MouseClicked = True
                    print(clickx,clicky)
                    if clickx > 230 and clickx < (230 + 40) and clicky > 430 and clicky < (430 + 40) and MouseClicked == True:
                        MouseClicked = False
                        userinput = 1
                        run = False
                    elif clickx > 380 and clickx < (380 + 40) and clicky > 430 and clicky < (430 + 40) and MouseClicked == True:
                        MouseClicked = False
                        userinput = 2
                        run = False
                    elif clickx > 530 and clickx < (530 + 40) and clicky > 430 and clicky < (430 + 40) and MouseClicked == True:
                        mode = 3
                        pygame.quit()
                        run = False
        
        if( userinput == 1):
            turn = 1

        elif( userinput == 2):
            turn = 0

        else:
            print("please enter either 1 or 2\n")

        playerturn = turn
        """while(True):
            print("1. with stealing")
            print("2. without stealing")
            userinput = input("play with or without stealing? ")
            if( userinput == "1"):
                stealing = 1
                break
            elif( userinput == "2"):
                stealing = 0
                break
            else:
                print("please enter either 1 or 2\n")"""
        game(0,0)
    elif(mode == 2):
        turn = 0
        Display.blit(WoodBackground,(0,0))
        display_message("Alagulimane",70,400,100,black)
        display_message("Made By: TEAM A5 ",20,650,20,black)
        display_message("Which Player should start, Human or AI?",30,400,300,black)
        Interactive(250,450,20,green,l_green,"Human")
        Interactive(400,450,20,yellow,l_yellow,"AI")
        Interactive(550,450,20,red,l_red,"Quit")
        pygame.display.update()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    clickx,clicky = pygame.mouse.get_pos()
                    MouseClicked = True
                    #print(clickx,clicky)
                    if clickx > 230 and clickx < (230 + 40) and clicky > 430 and clicky < (430 + 40) and MouseClicked == True:
                        MouseClicked = False
                        userinput = 1
                        run = False
                    elif clickx > 380 and clickx < (380 + 40) and clicky > 430 and clicky < (430 + 40) and MouseClicked == True:
                        MouseClicked = False
                        userinput = 2
                        run = False
                    elif clickx > 530 and clickx < (530 + 40) and clicky > 430 and clicky < (430 + 40) and MouseClicked == True:
                        userinput = 3
                        run = False

        if userinput == 1:
            turn = 1
        elif userinput == 2:
            turn  = 0    
        else:
            pygame.quit()
        playerturn = turn
        """while(True):
            print("1. with stealing")
            print("2. without stealing")
            userinput = input("play with or without stealing? ")
            if( userinput == "1"):
                stealing = 1
                break
            elif( userinput == "2"):
                stealing = 0
                break
            else:
                print("please enter either 1 or 2\n")"""

        Display.blit(WoodBackground,(0,0))
        display_message("Alagulimane",70,400,100,black)
        display_message("Made By: TEAM A5 ",20,650,20,black)
        display_message("Choose the level of difficulty",30,400,300,black)
        Interactive(200,450,20,green,l_green,"easy (depth=2)")
        Interactive(400,450,20,yellow,l_yellow,"medium (depth = 6)")
        Interactive(600,450,20,orange,orange,"hard (depth=10)")
        # Display.blit(board,(22,150))

        pygame.display.update()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    clickx,clicky = pygame.mouse.get_pos()
                    MouseClicked = True
                    # print(clickx,clicky)
                    if clickx > 180 and clickx < (180 + 40) and clicky > 430 and clicky < (430 + 40) and MouseClicked == True:
                        MouseClicked = False
                        userinput = 1
                        run = False
                    elif clickx > 380 and clickx < (380 + 40) and clicky > 430 and clicky < (430 + 40) and MouseClicked == True:
                        MouseClicked = False
                        userinput = 2
                        run = False
                    elif clickx > 580 and clickx < (580 + 40) and clicky > 430 and clicky < (430 + 40) and MouseClicked == True:
                        userinput = 3
                        run = False
        if userinput == 1:
            game(0,1,easy)
        elif userinput == 2:
            game(0,1,medium)
        elif userinput == 3:
            game(0,1,hard)
        '''while(True):
            print("1. easy (depth=2)")
            print("2. medium (depth=6)")
            print("3. hard (depth=10)")
            userinput = input("choose the ai difficulty: ")
            if( userinput == "1"):
                print("\nai is on easy difficulty\n")
                game(0,1,easy)
                break
            elif( userinput == "2"):
                print("\nai is on medium difficulty\n")
                game(0,1,medium)
                break
            elif( userinput == "3"):
                print("\nai is on hard difficulty\n")
                game(0,1,hard)
                break
            else:
                print("please enter either 1 ,2 or 3\n")'''

    elif(mode == 3):
        pygame.quit()
        '''print("we hope you liked the game")
        break
    print("//////////////////////////////////////////")
    print("//////////////////////////////////////////")
    print("//////////////////////////////////////////")
    print("\n")'''

Entry_Display()
pygame.quit()
sys.exit()

