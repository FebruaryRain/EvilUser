from User import player as Player
from Character import actor as Actor
from Narrative import narrative_builder as Narrative_Builder
from Scenario import scenario as Scenario

import sys
import distutils.util as util


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
                                  #input("Is your role customer facing? ")
                                  self.get_yn_input(input("Is your role customer facing? "))
                                  )
    self.hacker = None
    self.narrative =None
    self.scenario = None

    self.print_opening_splash()
    self.run_main_loop()
    return


  def run_main_loop(self):
    safety_catch = 0 # part of safety, below

    while self.b_playing: # careful of infinite loops!
      self.play_game()

      # safety to escape an infinite loop
      if safety_catch == 0:
        self.b_playing = False
        #print("safety catch used!")
      else:
        safety_catch +=1

    return


  def play_game(self):
    self.hacker = Actor.Actor(self.player)
    self.ask_for_hacker_selection()
    
    self.scenario = Scenario.Scenario(self.hacker)
    self.scenario.generate_scenario()
    points_accrued = self.scenario.get_points_total()

    self.narrative = Narrative_Builder.Narrative_Builder(self.scenario.get_options_selected(), self.hacker, self.player, points_accrued)
    self.narrative.pretty_print_narrative()
    self.narrative.print_ending()
    return


  def ask_for_hacker_selection(self):
    self.print_numbered_options_in_iterable(self.hacker.get_applicable_hackers(), "actor_type")
    #print(len(self.hacker.get_applicable_hackers()))
    response = self.request_input(len(self.hacker.get_applicable_hackers()))
    print(response)
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
    big_splash = r"""
     __________       ___________ ___          
    /   _____/ \     /  /__   __//  /         
   /   /___  \  \   /  /  /  /  /  /         
  /   ____/   \  \_/  /  /  /  /  /          
 /   /___      \     /__/  /__/  /____        
/_______/___    \___/________/_______/_____   
       /   /   /   /   _____/   ____/      \  
      /   /   /   /   /____/   /___/    ___/   
     /   /   /   /____    /   ____/     \     
    /    \__/   /____/   /   /___/   /\  \  
    \__________/________/_______/___/  \__\ 
"""
    print(big_splash)
    return


  def print_introduction(self):

    introduction = r"""
             ____ __  __   _       __ _________              
     / /\  /  /  / _\/  \ / \/   //    /  / /  \ /\  /   
    / /  \/  /  / \  \__//__/\__/ \__ /__/__\__//  \/   
    """
    print(introduction)

    print("""
Today, you will inhabit the role of the malicious attacker seeking to bring damage to LBG.
In the below scenario, you will take on the role of such a person and role play the steps that they would take in order to gain a deeper understanding of how these attacks are executed.
We hope you have fun looking through the other side of the glass!
""")

    return


  def print_instructions(self):
    instructions = r"""
             __ ____ __       ____________        __       
     / /\  //__  /  / _\/   //    /  / /  \ /\  //__   
    / /  \/ __/ /  / \  \__/ \__ /__/__\__//  \/ __/ 
    """
    print(instructions)

    print("""
Through this game, you will be presented with a series of multiple choice scenario sections. 
In each section, you will choose the path that the hacker follows. 
A full narrative will be provided at the end for you to see!
""")
    return


  def request_input(self, options_range):
    selection = None
    b_selection_not_good = True
    while b_selection_not_good:
      try:
        selection = int(input("Please give your selection: "))
        if selection in range(1, options_range+1):
          b_selection_not_good = False
        else:
          b_selection_not_good = True
      except: 
        print("Entry was not an int!")
        print("You entered:", type(selection), selection)
        if selection == "EXIT":
          self.b_playing = False
          print("Attempting to exit the game...")
          break
        else:
          print("Please ensure that your input is a specified number!")

    return selection

  def get_yn_input(self, answer):
    if "y" in answer or "Y" in answer:
      return True
    else:
      return False


if __name__ == "__main__":
  demo = False
  if len(sys.argv) > 1:
    demo = util.strtobool(sys.argv[1])
  game = Game(demo)
