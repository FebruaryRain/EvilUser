from User import player as Player
from Character import actor as Actor
from Narrative import narrative_builder as Narrative_Builder


class Game:
  """
  Game class
  This is the class containing the relevant logic for playing the game.
  This is a class that acts as a controller for all other classes, coordinating them. 
  Please use help(Game) to see the functions.
  """

  # Dummy values used in testing
  # Live version is hoped to speak with a database
  demo_user_values = {}
  demo_user_values["forename"] = "Matt"
  demo_user_values["surname"] = "Damon"
  demo_user_values["email"] = "matt.damon@LBG.ac.uk"
  demo_user_values["role"] = "Customer Person"
  demo_user_values["id"] = "112358"
  demo_user_values["is_customer_facing"] = True


  def __init__(self):
    
    self.b_playing = True
    self.player = Player.Player(Game.demo_user_values["forename"],
                                Game.demo_user_values["surname"],
                                Game.demo_user_values["email"],
                                Game.demo_user_values["role"],
                                Game.demo_user_values["id"],
                                Game.demo_user_values["is_customer_facing"])
    self.hacker = Actor.Actor()
    self.narrative = Narrative_Builder.Narrative_Builder()


    # Sanity Checks
    # alpha = self.player.get_full_name()
    # print(alpha)
    # print(self.player._forename)
    # print(self.player.get_role())


    self.print_opening_splash()
    self.run_main_loop()
    return


  def run_main_loop(self):
    safety_catch = 0 # part of safety, below

    while self.b_playing: # careful of infinite loops!
      self.play_game()

      # safety to escape an infinite loop
      if safety_catch == 5:
        self.b_playing = False
        print("safety catch used!")
      else:
        safety_catch +=1

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