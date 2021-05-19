from User import player as Player
from Character import actor as Actor
from Narrative import narrative_builder as Narrative_Builder
from Scenario import scenario as Scenario

import sys

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


  def __init__(self, is_in_demo_mode):
    self.b_playing = True
    if is_in_demo_mode:
      self.player = Player.Player(Game.demo_user_values["forename"],
                                  Game.demo_user_values["surname"],
                                  Game.demo_user_values["email"],
                                  Game.demo_user_values["role"],
                                  Game.demo_user_values["id"],
                                  Game.demo_user_values["is_customer_facing"]
                                  )
    else:
      self.player = Player.Player(input("What is your forename? "), 
                                  input("What is your surname? "), 
                                  input("What is your email? "), 
                                  input("What is your role? "), 
                                  input("What is your employee id? "), 
                                  input("Is your role customer facing? ")
                                  )
    self.hacker = None
    self.narrative =None
    self.scenario = None
    #print(self.hacker.get_applicable_hackers())
    #for hacker in self.hacker.hackers_list:
    #  if self.hacker.

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
      if safety_catch == 1:
        self.b_playing = False
        print("safety catch used!")
      else:
        safety_catch +=1

    return

  def play_game(self):
    self.hacker = Actor.Actor(self.player)
    self.ask_for_hacker_selection()
    
    self.scenario = Scenario.Scenario(self.hacker)



    self.narrative = Narrative_Builder.Narrative_Builder()
    return


  def ask_for_hacker_selection(self):
    self.print_numbered_options_in_iterable(self.hacker.get_applicable_hackers(), "actor_type")
    b_seeking_input = True
    while b_seeking_input:
      response = None
      try:
        response = int(self.request_input())
        if response <= len(self.hacker.get_applicable_hackers()) and response != 0:
          b_seeking_input = False
        else:
          print("Please ensure that your input is a specified number!")
      except: 
        print("Please ensure that your input is a specified number!")
        #print("Unknown Error!")
      
    print(self.hacker.get_applicable_hackers()[response-1])
    self.hacker.set_chosen_hacker_info(self.hacker.get_applicable_hackers()[response-1])
    return


  def print_numbered_options_in_iterable(self, iterable, field = None):
    """
    iterable var can be of dict or list. 
    If of type dict, field must be set as one of the expected dictionary entries (dict[field]).
    If of type list, field must be set as type int, indicating a positional value wanted to print.
    """

    num = 1 # Ooh, we do hate a magic number but here it makes sense (for now)

    for element in iterable:
    # deal with dicts
      if isinstance(element, dict):
        if field == None:
          print("There has been a terrible error, the passed var was full of dicts but no field has been selected, please ensure the field is selected!")
          raise Exception
        else:
          try:
              print(str(num) + " => " + str(element[field]))
          except:
            pass
        num +=1

    # deal with lists
      elif isinstance(element, list):
        if field == None:
          print(str(num) + " => " + str(element))
        else:
          if type(field) == "int":
            print(element[field])
          else: 
            print("There has been a terrible error, the passed var was full of lists but field was set to not a string, a dict may have been expected!")
            #raise Exception
        num +=1
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


  def request_input(self):
    try:
      selection = input("Please give your selection: ")
    except: 
      print("entry was not an int!")
      print("here",type(selection), selection)
      if selection == "EXIT":
        self.b_playing = False
      else:
        print("Please ensure that your input is a specified number!")
      
    return selection


if __name__ == "__main__":
  demo = False
  if len(sys.argv) > 1:
    demo = sys.argv[1]
  game = Game(demo)
