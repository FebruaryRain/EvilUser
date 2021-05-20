

class Option:

  def __init__(self, act_number, option_descriptor, actions_descriptor, points = 0, fun_fact = "Placeholder_fun_fact"):
    self.act = act_number
    self.option_descriptor = option_descriptor
    self.actions_descriptor = actions_descriptor
    self.action_taken = False
    self.points_for_action = points
    self.fun_fact = fun_fact
    return


  def get_act(self):
    return self.act


  def get_action_taken(self):
    return self.action_taken


  def get_actions_descriptor(self):
    return self.actions_descriptor


  def get_fun_fact(self):
    return self.fun_fact


  def get_option_descriptor(self):
    return self.option_descriptor


  def get_points_for_action(self):
    return self.points_for_action