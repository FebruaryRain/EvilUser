from .option import Option


class Act3:
  """
  Factory to generate the correct Act1 scenario details and options.
  """

  objectives_list = ["install_malware", "steal_card_details", "gain_payment"]

  def __init__(self, Hacker):
    self.act_number = 3
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
    looping = True
    while looping:
      self.background_to_current_activity()
      self.generate_options()
      self.display_options_descriptions()
      selection = self.request_input(len(self.options))
      self.chosen_option = self.options[selection-1]
      looping = False
      if self.chosen_option.option_descriptor == "Check your emails":
        self.hacker.check_emails()
        self.options.clear()
        looping = True
    print("You have chosen: " + self.chosen_option.option_descriptor)
    return


  # def create_act(self):
  #   # Start Scenario
  #   self.select_scenario_description()
  #   self.generate_options()
  #   self.display_options_descriptions()
  #   selection = self.request_input(len(self.options))
  #   self.chosen_option = self.options[selection-1]
  #   print("You have chosen: " + self.chosen_option.option_descriptor)
  #   return


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
Once access is gained, the time to strike is ripe.
In the attack, there is always a a risk of things not working quite right but seeking reward brings risk - for both parties.

What does the attack look like?
    """
    print(background_blurb)
    return


  def generate_options(self):

    if self.hacker_objective == "install_malware":
      descriptor = "Install rootkit and gain full admin access"
      actions_descriptor = "Rootkits are a classic and yet people always fall for them. Their mistake means I’m in charge of the system now!"
      points = 40
      install_malware_exploit_option1 = Option(self.act_number, descriptor, actions_descriptor, points)
      descriptor = "Jackpot ATM"
      actions_descriptor = "Nice of them to label the ATM control system. Bit of manipulation and I can get any ATM to drop its cash into my hands!"
      points = 50
      install_malware_exploit_option2 = Option(self.act_number, descriptor, actions_descriptor, points)
      descriptor = "Install Ransomware"
      actions_descriptor = "Ha! Let’s see them try and be a bank when their systems are encrypted by me! Should be worth a couple of million to unblock this!"
      points = 60
      install_malware_exploit_option3 = Option(self.act_number, descriptor, actions_descriptor, points)

      self.options.append(install_malware_exploit_option1)
      self.options.append(install_malware_exploit_option2)
      self.options.append(install_malware_exploit_option3)

    if self.hacker_objective == "steal_card_details":
      descriptor = "Fake a phone call"
      actions_descriptor = "Fake the source number, a little bit of phone line interference, fake a bit of a cold, and demand some card details, and they’ll never know who they’re really talking to!"
      points = 40
      install_malware_exploit_option1 = Option(self.act_number, descriptor, actions_descriptor, points)
      descriptor = "Send a spoofed email"
      actions_descriptor = "If I ask for card details whilst pretending to be someone high up in the organisation, I bet they’ll respond with everything I ask for, especially if I turn up the heat!"
      points = 50
      install_malware_exploit_option2 = Option(self.act_number, descriptor, actions_descriptor, points)
      descriptor = "Install a key logger"
      actions_descriptor = "A nice little present to pick up all their key strokes. A bit of analysis and I’ll be able to see every single card and account number they enter!"
      points = 60
      install_malware_exploit_option3 = Option(self.act_number, descriptor, actions_descriptor, points)

      self.options.append(install_malware_exploit_option1)
      self.options.append(install_malware_exploit_option2)
      self.options.append(install_malware_exploit_option3)

    if self.hacker_objective == "gain_payment":
      descriptor = "Provide alternative bank details"
      actions_descriptor = "Easy enough to convince them that a supplier has changed bank details, a bit of fast-talking and before they know it, they’re paying me instead!"
      points = 40
      gain_payment_exploit_option1 = Option(self.act_number, descriptor, actions_descriptor, points)
      descriptor = "Pretend to be a legitimate creditor"
      actions_descriptor = "They often pay this company a large amount of money. Easy enough to fake a call or email and demand a late payment. Threaten lawyers to grease-the-wheels!"
      points = 50
      gain_payment_exploit_option2 = Option(self.act_number, descriptor, actions_descriptor, points)
      descriptor = "set up fake transactions"
      actions_descriptor = "Lots of little transactions to an account I control should net me a good amount. If I keep them small but frequent, it’ll be months before they notice!"
      points = 60
      gain_payment_exploit_option3 = Option(self.act_number, descriptor, actions_descriptor, points)

      self.options.append(gain_payment_exploit_option1)
      self.options.append(gain_payment_exploit_option2)
      self.options.append(gain_payment_exploit_option3)

    self.options.append(Option(self.act_number, "Check your emails", ""))

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
