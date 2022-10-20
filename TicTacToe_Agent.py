#IMPORTING DEPENDENCIES...
#ML Libraries...
import pygame as pg
import numpy as np
import sys




#FUNCTION FOR MAIN...
def draw_lines(win):
    #Setting properties of our lines...
    LINE_COLOR = (0,0,0)
    LINE_WIDTH = 10
    SQUARE_SIZE = 200             #or even width since both are the same...
    WIDTH = 600
    HEIGHT = 600
        
    #Drawing lines for the window...
    pg.draw.line( win, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH )
    pg.draw.line( win, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH )
    pg.draw.line( win, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH )
    pg.draw.line( win, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )
    


# ALL THE CLASSES...
class Players():
    def __init__(self):
        self.player = 1

    def switch_turn(self):
        if (self.player == 1):
            self.player = 2
            print("Circle's Turn...")
        elif (self.player == 2):
            self.player = 1
            print("Square's Turn...")

    def reset_player(self):
        self.player = 1

class Tiles():
    def __init__(self, win):
        self.win = win
        self.tile_Length = 190 
        self.tile_Width = 190
        self.tile_Color = (170,170,170)
        self.players = Players()
        self.tilelist =[]
            
    def draw(self):
        x_start_pos = 0
        for row in range(BOARD_ROWS):
            y_start_pos = 0 
            for col in range(BOARD_COLS):
                #pygame.draw.rect(surface, (color), (startx,starty,length width))
                new_tile = pg.draw.rect(self.win, self.tile_Color , (x_start_pos,y_start_pos,self.tile_Length,self.tile_Length))
                self.tilelist.append(new_tile)
                y_start_pos = y_start_pos + 205
            x_start_pos = x_start_pos + 205
    
    #Check all the tiles if clicked...
    def check_tiles(self,pos,board):
        win = self.win
        print("\nChecking the Tiles...")
        radius = 50
        side = 100
        player = self.players.player
        list(open_list)

        #1st Column...
        if self.tilelist[0].collidepoint(pos) and open_list[0]:
            print("\n1st Tile...")
            #Draws a shapes based on whose turn it is
            if  self.players.player == 2:
                #pygame.draw.circle(surface, (color), (centerx, centery),radius)
                pg.draw.circle(win,red_color, (100,100), radius)
                self.players.switch_turn()
            elif self.players.player == 1:
                pg.draw.rect(win,green_color, (50,50,side,side))    #Width, length
                self.players.switch_turn()
            #Fill the board array...
            board[0][0] = player
            print(board)
            #Marks this space as taken
            open_list[0] = False
        
        elif self.tilelist[1].collidepoint(pos) and open_list[1]:
            print("\n4rth Tile...")
            if  self.players.player == 2:
                pg.draw.circle(win, red_color, (100,300), radius)
                self.players.switch_turn()
            else:
                pg.draw.rect(win, green_color, (50,250,side,side))
                self.players.switch_turn()
            board[1][0] = player
            print(board)
            open_list[1] = False
        
        elif self.tilelist[2].collidepoint(pos) and open_list[2]:
            print("\n7th Tile...")
            if  self.players.player == 2:
                pg.draw.circle(win, red_color, (100,500),radius)
                self.players.switch_turn()
            else:
                pg.draw.rect(win, green_color, (50,450,side,side))
                self.players.switch_turn()
            board[2][0] = player
            print(board)
            open_list[2] = False
        

        #2nd Column...
        elif self.tilelist[3].collidepoint(pos) and open_list[3]:
            print("\n2nd Tile...")
            if  self.players.player == 2:
                pg.draw.circle(win, red_color, (300,100),radius)
                self.players.switch_turn()
            else:
                pg.draw.rect(win, green_color, (250,50,side,side))
                self.players.switch_turn()
            board[0][1] = player
            print(board)
            open_list[3] = False
        
        elif self.tilelist[4].collidepoint(pos) and open_list[4]:
            print("\n5th Tile...")
            if  self.players.player == 2:
                pg.draw.circle(win, red_color, (300,300),radius)
                self.players.switch_turn()
            else:
                pg.draw.rect(win, green_color, (250,250,side,side))
                self.players.switch_turn()
            board[1][1] = player
            print(board)
            open_list[4] = False

        elif self.tilelist[5].collidepoint(pos) and open_list[5]:
            print("\n8th Tile...")
            if  self.players.player == 2:
                pg.draw.circle(win, red_color, (300,500),radius)
                self.players.switch_turn()
            else:
                pg.draw.rect(win, green_color, (250,450,side,side))
                self.players.switch_turn()
            board[2][1] = player
            print(board)
            open_list[5] = False
        

        #3rd Column...
        elif self.tilelist[6].collidepoint(pos) and open_list[6]:
            print("\n3rd Tile...")
            if  self.players.player == 2:
                pg.draw.circle(win, red_color, (500,100),radius)
                self.players.switch_turn()
            else:
                pg.draw.rect(win, green_color, (450,50,side,side))
                self.players.switch_turn()
            board[0][2] = player
            print(board)
            open_list[6] = False

        elif self.tilelist[7].collidepoint(pos) and open_list[7]:
            print("\n6th Tile...")
            if  self.players.player == 2:
                pg.draw.circle(win, red_color, (500,300),radius)
                self.players.switch_turn()
            else:
                pg.draw.rect(win, green_color, (450,250,side,side))
                self.players.switch_turn()
            board[1][2] = player
            print(board)
            open_list[7] = False
        
        elif self.tilelist[8].collidepoint(pos) and open_list[8]:
            print("\n9th Tile...")
            if  self.players.player == 2:
                pg.draw.circle(win, red_color, (500,500),radius)
                self.players.switch_turn()
            else:
                pg.draw.rect(win, green_color, (450,450,side,side))
                self.players.switch_turn()
            board[2][2] = player
            print(board)
            open_list[8] = False
            
        else:
            print("\nClick on another tile...")

        return player, board   #returning the last player who made the turn...

    #Reset all the boolean values for the tiles...
    def reset(self):
        
        #Reset the player from here...
        self.players.reset_player()

        #Resetting the tiles from here...
        open_list = [True, True, True, True, True, True, True, True, True]
        list(open_list)

        #Reseting the board array...
        board = np.array([[0,0,0],[0,0,0],[0,0,0]], dtype='int32')
        print("\nReseting the game...")
        print(board)

        return open_list, board

class TicTacToe():
    
    def __init__(self):        
        Window_Length = 600 
        Window_Width = 600
        gray_color = (200, 200, 200)
        
        #Create a Pygame window...
        pg.display.set_caption('Tic Tac Toe')
        self.win = pg.display.set_mode((Window_Length, Window_Width))
        self.win.fill(gray_color)
        draw_lines(self.win)
        self.tiles = self.draw_tiles(self.win)
        pg.display.update()

                
    def draw_tiles(self, win):
        tiles = Tiles(self.win)
        tiles.draw()
        return tiles

    def check_tiles(self,pos,board, reward):
        last_player, update_board = self.tiles.check_tiles(pos, board)
        new_open_list, update_board,reward_update = self.win_checker(self.win, last_player,open_list, update_board, reward)
        board = update_board
        reward = reward_update
        return board,new_open_list,reward

    #Checkpoint...
    def win_checker(self, win, last_player,open_list, update_board, reward):
        THICKNESS = 15
        board = update_board
        print("\nChecking who's won....")
        list(open_list)

        #First we are checking the tiles for a winner...
        #Horizontal first row...
        if (open_list[0] == False and open_list[3] == False and open_list[6] == False):
            print("Condition One...")
            if (board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1):
                print("Squares won...")
                pg.draw.line(win,green_color,(25,100),(575,100), THICKNESS)
                pg.display.update()
                pg.time.delay(2000)
                open_list, board = self.reset()
                reward += 10
                print("Reward: ",reward)
            elif (board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2):
                print("Circles won...")
                pg.draw.line(win,red_color,(25,100),(575,100), THICKNESS)
                pg.display.update()
                pg.time.delay(2000)
                open_list, board = self.reset()
                reward -= 5
                print("Reward: ",reward)
            else:
                print("\nNothing yet...")
                

        #Horizontal second row...
        if (open_list[1] == False and open_list[4] == False and open_list[7] == False):
            print("Condition Two...")
            if (board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1):
                print("Squares won...")
                pg.draw.line(win,green_color,(25,300),(575,300), THICKNESS)
                pg.display.update()
                pg.time.delay(2000)
                open_list, board = self.reset()
                reward += 10
                print("Reward: ",reward)
            elif (board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2):
                print("Circles won...")
                pg.draw.line(win,red_color,(25,300),(575,300), THICKNESS)
                pg.display.update()
                pg.time.delay(2000)
                open_list, board = self.reset()
                reward -= 5
                print("Reward: ",reward)
            else:
                print("\nNothing yet...")
        
        #Horizontal third row...
        if (open_list[2] == False and open_list[5] == False and open_list[8] == False):
            print("Condition Three...")
            if (board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1):
                print("Squares won...")
                pg.draw.line(win,green_color,(25,500),(575,500), THICKNESS)
                pg.display.update()
                pg.time.delay(2000)
                open_list, board = self.reset()
                reward += 10
                print("Reward: ",reward)
            elif (board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 2):
                print("Circles won...")
                pg.draw.line(win,red_color,(25,500),(575,500), THICKNESS)
                pg.display.update()
                pg.time.delay(2000)
                open_list, board = self.reset()
                reward -= 5
                print("Reward: ",reward)
            else:
                print("\nNothing yet...")
        
        #Vertical first column...
        if (open_list[0] == False and open_list[1] == False and open_list[2] == False):
            print("Condition Four...")
            if (board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1):
                print("Squares won...")
                pg.draw.line(win,green_color,(100,25),(100,575), THICKNESS)
                pg.display.update()
                pg.time.delay(2000)
                open_list, board = self.reset()
                reward += 10
                print("Reward: ",reward)
            elif (board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2):
                print("Circles won...")
                pg.draw.line(win,red_color,(100,25),(100,575), THICKNESS)
                pg.display.update()
                pg.time.delay(2000)
                open_list, board = self.reset()
                reward -= 5
                print("Reward: ",reward)
            else:
                print("\nNothing yet...")
        
        #Vertical second row...
        if (open_list[3] == False and open_list[4] == False and open_list[5] == False):
            print("Condition Five...")
            if (board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1):
                print("Squares won...")
                pg.draw.line(win,green_color,(300,25),(300,575), THICKNESS)
                pg.display.update()
                pg.time.delay(2000)
                open_list, board = self.reset()
                reward += 10
                print("Reward: ",reward)
            elif (board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2):
                print("Circles won...")
                pg.draw.line(win,red_color,(300,25),(300,575), THICKNESS)
                pg.display.update()
                pg.time.delay(2000)
                open_list, board = self.reset()
                reward -= 5
                print("Reward: ",reward)
            else:
                print("\nNothing yet...")
                
        #Vertical third column...
        if (open_list[6] == False and open_list[7] == False and open_list[8] == False):
            print("Condition Six...")
            if (board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1):
                print("Squares won...")
                pg.draw.line(win,green_color,(500,25),(500,575), THICKNESS)
                pg.display.update()
                pg.time.delay(2000)
                open_list, board = self.reset()
                reward += 10
                print("Reward: ",reward)
            elif (board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2):
                print("Circles won...")
                pg.draw.line(win,red_color,(500,25),(500,575), THICKNESS)
                pg.display.update()
                pg.time.delay(2000)
                open_list, board = self.reset()
                reward -= 5
                print("Reward: ",reward)
            else:
                print("\nNothing yet...")

        #Cross Left-to-Right...
        if open_list[0] == False and open_list[4] == False and open_list[8] == False:
            print("Condition Seven...")
            if (board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1):
                print("Squares won...")
                pg.draw.line(win,green_color,(25,25),(575,575), THICKNESS)
                pg.display.update()
                pg.time.delay(2000)
                open_list = self.reset()
                reward += 10
                print("Reward: ",reward)
            elif (board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2):
                print("Circles won...")
                pg.draw.line(win,red_color,(25,25),(575,575), THICKNESS)
                pg.display.update()
                pg.time.delay(2000)
                open_list, board = self.reset()
                reward -= 5
                print("Reward: ",reward)
            else:
                print("\nNothing yet...")
       

        '''
        #Cross Right-to-Left...
        if open_list[2] == False and open_list[4] == False and open_list[6] == False:
            print("Condition Eight...")
            if (board[2][0] == 1 and board[1][1] == 1 and board[0][2] == 1):
                print("Squares won...")
                pg.draw.line(win,green_color,(25,575),(575,25), THICKNESS)
                pg.display.update()
                pg.time.delay(2000)
                open_list = self.reset()
                reward += 10
                print("Reward: ",reward)
            elif (board[2][0] == 2 and board[1][1] == 2 and board[0][2] == 2):
                print("Circles won...")
                pg.draw.line(win,red_color,(25,575),(575,25), THICKNESS)
                pg.display.update()
                pg.time.delay(2000)
                open_list, board = self.reset()
                reward -= 5
                print("Reward: ",reward)
            else:
                print("\nNothing yet...")
        '''
        
        
        
        #Since all the tiles are taken by players and don't satisfy a condition...
        if open_list[0] == False and open_list[1] == False and open_list[2] == False and open_list[3] == False and open_list[4] == False and open_list[5] == False and open_list[6] == False and open_list[7] == False and open_list[8] == False:
            print("Condition Nine...")
            print(board)
            print("DRAW!")
            pg.draw.circle(win,green_color,(300,300),200,THICKNESS)
            pg.display.update()
            pg.time.delay(2000)
            open_list, board = self.reset()
             
        return open_list, board, reward
    
    def reset(self):
        #Resetting the game screen...
        self.win.fill((200,200,200))
        draw_lines(self.win)
        self.draw_tiles(self.win)
        
        #Reset the open_list, numpy_board, and the player (squares) as well...
        open_list, board = self.tiles.reset()
        
        #Update and refresh...
        pg.display.update()
        
        return open_list, board
 



#Main Program
if __name__ == "__main__":
    
    #Initialize all the variables...
    #Color...
    red_color = (255, 0, 0)
    green_color = (0, 255, 0)

    #target
    reward = 0
    target = 50

    #Board...
    BOARD_ROWS = 3
    BOARD_COLS = 3
    board = np.array([[0,0,0],[0,0,0],[0,0,0]], dtype='int32') 

    #Tiles...
    first_open = True
    second_open = True
    third_open = True
    fourth_open = True
    fifth_open = True
    sixth_open = True
    seventh_open = True
    eighth_open = True
    ninth_open = True
    open_list = [first_open, second_open, third_open, fourth_open, fifth_open, sixth_open, seventh_open, eighth_open, ninth_open]
    
    #Initialize Pygame...
    pg.init()
    tictactoe = TicTacToe()
    
    Window_Loop = True
    while (Window_Loop):
        pg.time.delay(100)
    
        for event in pg.event.get():
            if event.type == pg.QUIT:
                Window_Loop = False                                #Press 'Esc' to exit...
    
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    print("\nReseting the game...")
                    open_list, board = tictactoe.reset()  

            if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                board_update, open_list, reward = tictactoe.check_tiles(pos, board, reward)
                list(open_list)
                board = board_update
                
                #Updating the window...
                pg.display.update()

            if (reward >= target):
                print("\nEnd of the Game.Target Reached.\n")
                Window_Loop = False
    
    print("Closing Pygame...")
    pg.quit()
