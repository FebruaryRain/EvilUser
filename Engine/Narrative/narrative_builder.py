

class Narrative_Builder:


  def __init__(self, options_list, hacker, player, points_at_end):
    self.options_list = options_list
    self.hacker = hacker
    self.player = player
    self.points = points_at_end

    return


  def pretty_print_narrative(self):
    summary = """
     __                  _    __   __              
    /__/   //\\/\\  /\\/\\  /_\\  / _\\ / _\\ \\\\// 
    __/\\__//    \\/    \\/   \\/  \\ /  \\   //    
    """

    print(summary)
    print("")
    for option in self.options_list:
      phase_name = ""
      if option.get_act() == 1:
        phase_name = "Reconnaissance"
      if option.get_act() == 2:
        phase_name = "Infiltration"
      if option.get_act() == 3:
        phase_name = "Exploitation"
      print("*** In the" + " " + phase_name + " " + "phase, the hacker," + " " + self.hacker.get_full_name() + ", " + "chose to:")
      print(option.get_option_descriptor())
    story = """
     __ ___ __   __          
    /__  / /  \\ / _\\\\\\// 
    __/ /  \\__//  \\  //    
    """

    print(story)
    print("")
    print("Throughout," + " " + self.hacker.get_full_name() + " " + "was thinking:")
    for option in self.options_list:
      print(option.get_actions_descriptor())
    print("")
    print("While they went, they scored" + " " + str(self.points) + " " + "points - good job" + " " + self.hacker.get_full_name() + "!")
    return


  def print_ending(self):
    print("")
    print("And so, this was the story of how you could have been hacked.")
    print("")
    print("Yes, you." + " " + self.player.get_full_name() + "\n")
    print("")
    print("Through this exercise, we hope you can see how a hacker operates; the techniques and tricks they use in order to gather information from seemingly innocuous sources, and chain these together to be able to later carry out an attack using a variety of methods.")
    print("Please see below, for examples of how the scenario the hacker," + " " + self.hacker.get_full_name() + ", " + "might have targetted you.")
    print("WIP: Add the examples of each stage below!")
    return