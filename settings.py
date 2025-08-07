import pygame
from os.path import join

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
SIZE = {'paddle': (40,100), 'ball': (30,30)}
POS = { 'player': (WINDOW_WIDTH - 50, WINDOW_HEIGHT // 2), 'player2' : (50, WINDOW_HEIGHT // 2)}
SPEED = {'player': 500,'player2': 500, 'ball': 250}
COLORS = {
  'paddle' : "#ee802c",
  'paddle shadow' : "#b12521",
  'ball' : "#ffffff",
  'ball shadow': "#c14f24",
  'bg' : "#270033",
  'center_line': "#ffffff80",  # Semi-transparent white
  'score': "#ffffff"
}

# Score settings
SCORE_FONT_SIZE = 72
SCORE_POS = {
  'player1': (WINDOW_WIDTH // 4 * 3, 100),  # Right side
  'player2': (WINDOW_WIDTH // 4, 100)       # Left side
}