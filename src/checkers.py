class CheckersGame():
    def __init__(self):
        self.board=[[0,2,0,2,0,2,0,2],
                    [2,0,2,0,2,0,2,0],
                    [0,2,0,2,0,2,0,2],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [1,0,1,0,1,0,1,0],
                    [0,1,0,1,0,1,0,1],
                    [1,0,1,0,1,0,1,0]]
        self.whoseMove="white"
        self.isWon=False
    def parseMove(self,move):
        if('8' in move or '9' in move):
            raise ValueError
        move=move.split(' ')
        xys=()
        for m in move:
            if(len(m)!=2):
                raise ValueError
            xys+=((int(m[1]),int(m[0])),)
        return xys
    def checkWinner(self):
        white=0
        red=0
        for r in self.board:
            if((1 in r or 3 in r) and white==0):
                white=1
            if((2 in r or 4 in r) and red==0):
                red=1
        if(white==0):
            self.isWon="red"
            return "red"
        if(red==0):
            self.isWon="white"
            return "white"
    def changeTurn(self):
        if(self.whoseMove=="white"):
            self.whoseMove="red"
        else:
            self.whoseMove="white"
    def move(self,move):
        move=self.parseMove(move)
        p=self.board[move[0][1]][move[0][0]]
        if(abs(move[1][0]-move[0][0])==2):
            for i in range(len(move)-1):
                self.board[(move[i+1][1]+move[i][1])//2][(move[i+1][0]+move[i][0])//2]=0
        self.board[move[0][1]][move[0][0]]=0
        if(p==1 and move[-1][1]==0):
            self.board[move[-1][1]][move[-1][0]]=3
        elif(p==2 and move[-1][1]==7):
            self.board[move[-1][1]][move[-1][0]]=4
        else:
            self.board[move[-1][1]][move[-1][0]]=p
        self.checkWinner()
        self.changeTurn()
    def isValidMove(self,move):
        if(self.isWon):return False
        try:
            move=self.parseMove(move)
            if(self.board[move[0][1]][move[0][0]]==0):return False
            if((self.board[move[0][1]][move[0][0]]==1 or self.board[move[0][1]][move[0][0]]==3) and self.whoseMove=="red"):return False
            if((self.board[move[0][1]][move[0][0]]==2 or self.board[move[0][1]][move[0][0]]==4) and self.whoseMove=="white"):return False
            for i in range(len(move)):
                if(move[i][0]%2==move[i][1]%2):return False
                if(i!=0):
                    if(self.board[move[i][1]][move[i][0]]!=0):
                        if(not((self.board[move[0][1]][move[0][0]]==3 or self.board[move[0][1]][move[0][0]]==4) and move[i]==move[0])):return False                            
                    if(move[i][1]-move[i-1][1]>0 and self.whoseMove=="white" and self.board[move[0][1]][move[0][0]]==1):return False
                    if(move[i][1]-move[i-1][1]<0 and self.whoseMove=="red" and self.board[move[0][1]][move[0][0]]==2):return False
                    if(abs(move[i][0]-move[i-1][0])!=1 or abs(move[i][1]-move[i-1][1])!=1 or len(move)>2):
                        if(abs(move[i][0]-move[i-1][0])==2 and abs(move[i][1]-move[i-1][1])==2):
                            if(self.board[(move[i][1]+move[i-1][1])//2][(move[i][0]+move[i-1][0])//2]==0):return False
                            if((self.board[(move[i][1]+move[i-1][1])//2][(move[i][0]+move[i-1][0])//2]==1 or self.board[(move[i][1]+move[i-1][1])//2][(move[i][0]+move[i-1][0])//2]==3) and self.whoseMove=="white"):return False
                            if((self.board[(move[i][1]+move[i-1][1])//2][(move[i][0]+move[i-1][0])//2]==2 or self.board[(move[i][1]+move[i-1][1])//2][(move[i][0]+move[i-1][0])//2]==4) and self.whoseMove=="red"):return False
                        else:return False
        except:return False
        return True

    def __str__ (self) :
        out = "  0 1 2 3 4 5 6 7 \n ╔═╤═╤═╤═╤═╤═╤═╤═╗\n"
        i = 0
        for row in self.board :
            out += f"{str(i)}║"
            j = 0
            for item in row :
                if item == 0:
                    out += "░" if (i + j) % 2 == 0 else " "
                elif item >= 1 and item <= 4:
                    out += ["○", "●", "♔", "♚"][item-1]
                out += "│"
                j += 1
            out = out[:-1]
            out += f"║{str(i)}\n ╟─┼─┼─┼─┼─┼─┼─┼─╢\n"
            i += 1
        out = out[:-18]
        out += "╚═╧═╧═╧═╧═╧═╧═╧═╝\n  0 1 2 3 4 5 6 7 \n"
        return out
    
def runGame (init = False, moveList = False) :
    game = CheckersGame()

    if (init != False) :
        game.board = init
    
    print("Checkers Initialized...")
    print(game)
    if (moveList != False) :
        print("Move List Detected, executing moves")
        for move in moveList :
            print(f"{game.whoseMove} makes move {move}\n")
            if (move == "q") :
                return
            if (game.isValidMove(move)) :
                game.move(move)
                print(game)
                if (game.isWon != 0) :
                    break
            else :
                print("Invalid Move")    
                
    print("Moves must be typed as coordinates (with no commas or brackets) separated by spaces. Row, then column.")
    print("Example: 54 43")
    print("When performing multiple jumps, enter each co-ordinate your piece will land on in sequence.")
    while (game.isWon == False) :
        print(f"{game.whoseMove} to move")
        move = input(">> ")
        if (move == "q") :
            return
        if (game.isValidMove(move)) :
            game.move(move)
            print(game)
            if (game.isWon != 0) :
                break
        else :
            print("Invalid Move")
    print("The Game is Finished!")
    print(f"Congratulations, {game.isWon}!")