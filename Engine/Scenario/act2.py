from .option import Option


class Act2:
  """
  Factory to generate the correct Act1 scenario details and options.
  """

  objectives_list = ["install_malware", "steal_card_details", "gain_payment"]

  def __init__(self, Hacker):
    self.act_number = 2
    self.hacker = Hacker
    self.hacker_type = Hacker.chosen_hacker_info["actor_type"]
    self.hacker_objective = Hacker.chosen_hacker_info["objectives"]
    self.objective_descriptor = ""
    self.narrative_description = ""
    self.options = []
    self.chosen_option = None
    return


  def get_chosen_option(self):
    return self.chosen_option


  def create_act(self):
    # Start Scenario
    self.select_scenario_description()
    self.background_to_current_activity()
    self.generate_options()
    self.display_options_descriptions()
    selection = self.request_input(len(self.options))
    self.chosen_option = self.options[selection-1]
    print("You have chosen: " + self.chosen_option.option_descriptor)
    return


#  def create_act(self):
#    # Start Scenario
#    self.select_scenario_description()
#    self.generate_options()
#    self.display_options_descriptions()
#    selection = self.request_input(len(self.options))
#    self.chosen_option = self.options[selection-1]
#    print("You have chosen: " + self.chosen_option.option_descriptor)
#    return


  def display_options_descriptions(self):
    num = 1
    for item in self.options:
      print(str(num) + " => " + str(item.option_descriptor))
      num += 1
    return


  def select_scenario_description(self):
    if self.hacker_objective == "install_malware":
      self.objective_descriptor = "install malware on a LBG device"
    if self.hacker_objective == "steal_card_details":
      self.objective_descriptor = "steal the credit/debit card details of your target"
    if self.hacker_objective == "gain_payment":
      self.objective_descriptor = "persuade your target to make a payment to you"

    scenario_open_fluff_start = "Welcome, you are the hacker" + " " + self.hacker.first_name + " " + self.hacker.surname + ". " + "Your objective is to use all of your nefarious schemes to"
    scenario_open_fluff_end = "for your own dastardly gain!"
    self.narrative_description =  scenario_open_fluff_start + " " + self.objective_descriptor + " " + scenario_open_fluff_end
    return


  def background_to_current_activity(self):
    background_blurb = """
Once information has been collected on a target, person or organisation, the next step is to "Infiltrate" in some manner. 
This can include a wide array of techniques, depending on the goal and type of target. 
The ultimate aim here is to gain (greater) access to later exploit in order to carry out the attack and complete the goal.

Select how to gain this access below:
    """
    print(background_blurb)
    return


  def generate_options(self):

    if self.hacker_objective == "install_malware":
      descriptor = "Send an email from an account with a similar email address to internal ones with a convincing dodgy link in the body"
      actions_descriptor = "Rootkits are a classic and yet people always fall for them. Their mistake means I’m in charge of the system now!"
      points = 40
      install_malware_infil_option1 = Option(self.act_number, descriptor, actions_descriptor, points)
      descriptor = "Send an email from an account with an email that makes it look like a legitimate supplier sent it, with a virus attached in a file"
      actions_descriptor = "Nice of them to label the ATM control system. Bit of manipulation and I can get any ATM to drop its cash into my hands!"
      points = 50
      install_malware_infil_option2 = Option(self.act_number, descriptor, actions_descriptor, points)
      descriptor = "Send an email that is broadly generic to a generated list of names using the standard email format"
      actions_descriptor = "Ha! Let’s see them try and be a bank when their systems are encrypted by me! Should be worth a couple of million to unblock this!"
      points = 60
      install_malware_infil_option3 = Option(self.act_number, descriptor, actions_descriptor, points)

      self.options.append(install_malware_infil_option1)
      self.options.append(install_malware_infil_option2)
      self.options.append(install_malware_infil_option3)

    if self.hacker_objective == "steal_card_details":
      descriptor = "Craft a text to send with notice about a missed delivery"
      actions_descriptor = "Everyone has been ordering online like crazy, this is sure to catch at least a few out!"
      points = 40
      install_malware_infil_option1 = Option(self.act_number, descriptor, actions_descriptor, points)
      descriptor = "Craft a generic HMRC notice that they need to handle"
      actions_descriptor = "Everyone hates taxes, so anything promising to give back their own money is sure to get a lot of hits!"
      points = 50
      install_malware_infil_option2 = Option(self.act_number, descriptor, actions_descriptor, points)
      descriptor = "Send a text from a well-known charity asking for donations"
      actions_descriptor = "Ha, this one is genius, if they fall for it then the expect the money to go out each month!"
      points = 60
      install_malware_infil_option3 = Option(self.act_number, descriptor, actions_descriptor, points)

      self.options.append(install_malware_infil_option1)
      self.options.append(install_malware_infil_option2)
      self.options.append(install_malware_infil_option3)

    if self.hacker_objective == "gain_payment":
      gain_payment_infil_option1 = Option(self.act_number, descriptor, actions_descriptor, points)
      descriptor = "Email the person in charge of making payments to a supplier"
      actions_descriptor = "As long as I spell check and mention pertinent details to recent deals (I'm sure I can find something out online) then they might miss my slightly wrong email address!"
      points = 40
      descriptor = "Call the person in charge of making payments to a supplier"
      actions_descriptor = "OK, deep breath in, and out, now convince them you're not wearing sweats and a hoody "
      points = 50
      gain_payment_infil_option2 = Option(self.act_number, descriptor, actions_descriptor, points)
      descriptor = "Call a system administrator"
      actions_descriptor = "If they think they're talking to an internal person, they migt be willing to set up the payments to get around a bug I report - diabolical!"
      points = 60
      gain_payment_infil_option3 = Option(self.act_number, descriptor, actions_descriptor, points)

      self.options.append(gain_payment_infil_option1)
      self.options.append(gain_payment_infil_option2)
      self.options.append(gain_payment_infil_option3)

    return


  def get_narrative_description(self):
    return self.narrative_description


  def request_input(self, options_range):
    selection = None
    b_selection_not_good = True
    while b_selection_not_good:
      try:
        selection = int(input("Please give your selection: "))
        if selection in range(1, options_range+1):
          b_selection_not_good = False
        else:
          print("Please ensure that you select one of the valid options!")
      except: 
        print("Entry was not an int!")
        print("You entered:", type(selection), selection)
        if selection == "EXIT":
          self.b_playing = False
        else:
          print("Please ensure that your input is a specified number!")
      
    return selection