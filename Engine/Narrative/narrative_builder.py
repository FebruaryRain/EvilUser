

class Narrative_Builder:


  def __init__(self, options_list, hacker, player):
    self.options_list = options_list
    self.hacker = hacker
    self.player = player

    return

  def pretty_print_narrative(self):
    for option in self.options_list:
      phase_name = ""
      if option.act == 1:
        phase_name = "Recconnaisance"
      if option.act == 2:
        phase_name = "Infiltration"
      if option.act == 3:
        phase_name = "Exploitation"
      print("*** In the" + " " + phase_name + " " + "phase, the hacker," + " " + self.hacker.get_full_name() + ", " + "chose to:")
      print(option.get_option_descriptor())
    print("")
    print("Throughout," + " " + self.hacker.get_full_name() + " " + "was thinking:")
    for option in self.options_list:
      print(option.get_actions_descriptor())
    return

  def print_ending(self):
    print("And so, this was the story of how you could have been hacked.")
    print("")
    print("Yes, you." + " " + self.player.get_full_name() + "\n")
    print("")
    print("Through this exercise, we hope you can see how a hacker operates; the techniques and tricks they use in order to gather information from seemingly innocuous sources")
    print("Please see below, for examples of how the scenario the hacker," + " " + self.hacker.get_full_name() + ", " + "might have targetted you.")
    print("WIP: Add the examples of each stage below!")
    return