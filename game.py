import pygame, sys
from time import sleep
from pygame.locals import QUIT
import threading

pygame.init()

class Game:
  def __init__(self):
    self.running = True
    self.width = 200 
    self.height = 200

    font = pygame.font.Font("freesansbold.ttf", 32)
    
    self.winText = font.render("You Win!", True, (0, 255, 0), None)
    self.winTextRect = self.winText.get_rect()
    self.winTextRect.center = (self.width // 2, self.height // 2)
    
    # self.loseText = font.render("Game Over!", True, (255, 0, 0), None)
    # self.loseTextRect = self.loseText.get_rect()
    # self.loseTextRect.center = (self.width // 2, self.height // 2)

    self.position = [0, 7]
    self.direction = [1, 0]
    
    self.window = pygame.display.set_mode((self.width, self.height))
    pygame.display.set_caption('Hello World!')
    
    self.grid = [
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 1, 1, 0, 1, 0],
      [0, 0, 1, 0, 1, 0, 1, 0],
      [0, 0, 1, 0, 1, 0, 1, 0],
      [0, 0, 1, 0, 1, 1, 1, 0],
      [0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0],
      [1, 1, 1, 0, 0, 0, 0, 0]
    ]

    self.colours = [(0, 0, 0), (255, 255, 255)]

    self.gridLength = len(self.grid)
    self.cellSize = self.width / self.gridLength
    
    self.applePosition = [1, 6]
    self.appleImg = pygame.transform.scale(pygame.image.load("apple.png"), (self.cellSize, self.cellSize))
    
    self.grassImg = pygame.transform.scale(pygame.image.load("grass.png"), (self.cellSize, self.cellSize))
    
    self.sandImg = pygame.transform.scale(pygame.image.load("sand.jpeg"), (self.cellSize, self.cellSize))

    self.playerImg = pygame.transform.scale(pygame.image.load("player.png"), (self.cellSize, self.cellSize))
    self.playerImg = pygame.transform.rotate(self.playerImg, -90)
    
    print("Game instantiated")

  def drawFrame(self):
    for event in pygame.event.get():
      if event.type == QUIT:
        self.running = False
      
    for i in range(self.gridLength):
      for j in range(self.gridLength):
        imgNumber = self.grid[i][j]
        
        if imgNumber == 0:
          self.window.blit(self.grassImg, (j * self.cellSize, i * self.cellSize))
        elif imgNumber == 1:
          self.window.blit(self.sandImg, (j * self.cellSize, i * self.cellSize))
        
    self.window.blit(self.appleImg, (self.applePosition[1] * self.cellSize, self.applePosition[0] * self.cellSize))
    self.window.blit(self.playerImg, (self.position[0] * self.cellSize, self.position[1] * self.cellSize))

  def forward(self):
     sleep(1)
     self.currentPos = self.applePosition[1]
     self.currentPos =+ 1
     self.applePosition[1] = self.currentPos
    
  def mainLoop(self):
    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
          sys.exit()
          pygame.quit()
      if self.position[0] == self.applePosition[1] and self.position[1] == self.applePosition[0]:
        self.window.fill((255, 255, 255))
        self.window.blit(self.winText, self.winTextRect)
        pygame.display.update()
        sleep(5)
        pygame.quit()
        sys.exit()
        self.running = False
        
      self.drawFrame()
      pygame.display.update()

    self.cleanup()
    
  def cleanup():
    pygame.quit()
    sys.exit()

  def checkBounds(self):
    if (self.position[0] < 0):
      self.position[0] = 0
      print("You hit the wall")
    if (self.position[0] > 7):
      self.position[0] = 7
      print("You hit the wall")
    if (self.position[1] < 0):
      self.position[1] = 0
      print("You hit the wall")
    if (self.position[1] > 7):
      self.position[1] = 7
      print("You hit the wall")

    if (self.grid[self.position[1]][self.position[0]] == 0):
      print("You cannot move onto the grass!")
      self.move("backward")

  def move(self, direction):
    if (direction == "forward" or direction == "forwards"):
      self.position[0] += self.direction[0]
      self.position[1] -= self.direction[1]
    elif (direction == "backward" or direction == "backwards"):
      self.position[0] -= self.direction[0]
      self.position[1] += self.direction[1]
    
    self.checkBounds()

    # print(self.position)
    
  def rotate(self, direction):
    if (direction == 'left'):
      temp = self.direction[0]
      self.direction[0] = -self.direction[1]
      self.direction[1] = temp
      self.playerImg = pygame.transform.rotate(self.playerImg, 90)
    elif (direction == 'right'):
      temp = self.direction[0]
      self.direction[0] = self.direction[1]
      self.direction[1] = -temp
      self.playerImg = pygame.transform.rotate(self.playerImg, -90)
    sleep(1)