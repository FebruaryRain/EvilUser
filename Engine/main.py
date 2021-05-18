#from Player import Player
#from Hacker import Hacker
#from Narrative_builder import Narrative_builder

class Game:
  """
  Game class
  This is the class containing the relevant logic for playing the game.
  This is a class that acts as a controller for all other classes, coordinating them. 
  Please use help(Game) to see the functions.
  """
  def __init__(self):
    self.b_playing = True
    #self.player = Player()
    #self.hacker = Hacker()
    #self.narrative = Narrative_builder()
    
    return


  def run_main_loop(self):
    safety_catch = 0 # part of safety, below

    while self.b_playing: # careful of infinite loops!
      self.play_game()

      # safety to escape an infinite loop
      if safety_catch == 5:
        self.b_playing = False
      else:
        safety_catch +=1
        print(safety_catch)

    return

  def play_game(self):
    print()
    return

  def print_opening_splash(self):
    self.print_title()
    self.print_introduction()
    self.print_instructions()
    return


  def print_title(self):
    print("Here's the place holder title!")
    return


  def print_introduction(self):
    print("This is where the introduction text will be!")
    return


  def print_instructions(self):
    print("This is where the instructions will be!")
    return


  def update_narrative(self):
    
    return



if __name__ == "__main__":
  game = Game()
  game.run_main_loop()