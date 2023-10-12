from game import Game
import threading
from time import sleep
''' ** DON'T TOUCH INIT! ** '''

# Init
game = Game()
threadMain = threading.Thread(target=game.mainLoop)
threadMain.start()
'''
- You have two commands: game.move() and game.rotate()
- To move forwards or backwards, tell the computer by using a direction ("forward" or "backward").
- Quote marks are important - game.move("backward") will work, but game.move(backward) won't!

- To rotate, tell the computer by using a direction ("left" or "right").
- Quote marks are important - game.rotate("left") will work, but game.rotate(left) won't!

Hint: use sleep() to make the program wait! Otherwise, Steve will go too fast!

Use the space below to help Steve get to the apple!
'''

# Start writing your code here
# Hint remember that it is game.move("forward") and game.move("left") or right to turn

print("Start writing code")

game.move("forward")
game.move("forward")
game.rotate("left")
for i in range(6): 
  game.move("forward")
game.rotate("right")
game.move("forward")
game.move("forward")
game.rotate("right")
for i in range(3):
  game.move("forward")
game.rotate("left")
game.move("forward")
game.move("forward")
game.rotate("left")
for i in range(3):
  game.move("forward")
 