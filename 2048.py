import numpy as np 
import random

class game:
    def __init__(self,width=4,height=4):
        self.val=np.zeros((height,width))
        self.add_new()
        self.add_new()

    def add_new(self):
        x=4 if random.randint(1,10)<=2 else 2
        s=divmod(random.randrange(1,16),4)
        while self.val[s[0]][s[1]]!=0:
            s=divmod(random.randrange(1,16),4)
        self.val[s[0]][s[1]]=x
    
    def lose(self):
        for i in range(3):
            for j in range(3):
                if self.val[i][j]==self.val[i+1][j] or self.val[i][j]==self.val[i][j+1]:
                    return False
        return True
    
    def check_horizontal(self):
        for i in range(4):
            for j in range(3):
                if self.val[i][j]==self.val[i][j+1]:
                    return True
        return False
    
    def check_vertical(self):
        for i in range(3):
            for j in range(4):
                if self.val[i][j]==self.val[i+1][j]:
                    return True
        return False
    
    def move_left(self):
        for i in range(4):
            for j in range(1,4):
                while self.val[i][j-1]==0:
                    self.val[i][j-1]=self.val[i][j]
                    self.val[i][j]=0
        for i in range(4):
            for j in range(1,4):
                if self.val[i][j]==self.val[i][j-1]:
                    self.val[i][j-1]=2*self.val[i][j]
                    self.score+=2*self.val[i][j]
                    self.val[i][j]=0
        for i in range(4):
            for j in range(1,4):
                while self.val[i][j-1]==0:
                    self.val[i][j-1]=self.val[i][j]
                    self.val[i][j]=0
        self.add_new()

    def move_right(self):
        for i in range(4):
            for j in range(2,-1,-1):
                while self.val[i][j+1]==0:
                    self.val[i][j+1]=self.val[i][j]
                    


    def move_up(self):
        for j in range(4):
            for i in range(1,4):
                while self.val[i-1][j]==0:
                    self.val[i-1][j]=self.[i][j]
                    self.val[i][j]=0
        for j in range(4):
            for i in range(1,4):
                while self.val[i-1][j]==self.val[i][j]:
                    self.val[i-1][j]=2*self.val[i][j]
                    self.score+=2*self.val[i][j]
                    self.val[i][j]=0
        for j in range(4):
            for i in range(1,4):
                while self.val[i-1][j]==0:
                    self.val[i-1][j]=self.[i][j]
                    self.val[i][j]=0

    def move_down(self):
