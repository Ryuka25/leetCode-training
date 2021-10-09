# Game project just for fun --- Copyright © 2021 by Ryuka
#  
#* Let's introduce about me: 
#* I'm an IT student from Madagascar. If lucky me, you search for a developer!
#* And my competence is enough to work with you,
#* Please see my portfolio at: ryuka25.github.io/
#  
#! This is a guess_me challenge game 
# 

from Game import *
from Gameset import *

if (__name__ == "__main__"):
    Game.gameBanner()
    gameSet = GameSet()
    Game.execute(gameSet)
