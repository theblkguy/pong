#!/home/banj0k0/senior/pong/.venv/bin/python
from settings import *
from sprites import *


class Game:
  def __init__(self):
    pygame.init()
    self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Pong')
    self.clock = pygame.time.Clock()
    self.running = True

    # sprites
    self.all_sprites = pygame.sprite.Group()
    self.paddle_sprites = pygame.sprite.Group()
    self.player = Player((self.all_sprites, self.paddle_sprites))
    self.ball = Ball(self.all_sprites, self.paddle_sprites)
    Player2((self.all_sprites, self.paddle_sprites))

    # Initialize scores and font
    self.scores = {'player1': 0, 'player2': 0}
    self.font = pygame.font.Font(None, SCORE_FONT_SIZE)

  def run(self):
    while self.running:
      dt = self.clock.tick(60) / 1000  # 60 FPS target
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False

      # update
      self.all_sprites.update(dt) 
      scored = self.ball.update(dt)
      if scored:
          self.scores[f'player{scored}'] += 1
          # Reset ball moving towards the player who just scored
          self.ball.reset_ball(1 if scored == 1 else -1)

      # draw
      self.display_surface.fill(COLORS['bg'])
      self.all_sprites.draw(self.display_surface)

      # Draw center line
      center_line_surface = pygame.Surface((4, WINDOW_HEIGHT))
      center_line_surface.set_alpha(128)  # Semi-transparent
      center_line_surface.fill(pygame.Color(COLORS['center_line'][:7]))  # Remove alpha from color string
      self.display_surface.blit(center_line_surface, (WINDOW_WIDTH // 2 - 2, 0))

      # Draw scores
      player1_score = self.font.render(str(self.scores['player1']), True, COLORS['score'])
      player2_score = self.font.render(str(self.scores['player2']), True, COLORS['score'])
      self.display_surface.blit(player1_score, SCORE_POS['player1'])
      self.display_surface.blit(player2_score, SCORE_POS['player2'])

      pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
  game = Game()
  game.run()