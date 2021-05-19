from .option import Option


class Act1:
  """
  Factory to generate the correct Act1 scenario details and options.
  """

  objectives_list = ["install_malware", "steal_card_details", "gain_payment"]

  def __init__(self, Hacker):
    self.act_number = 1
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
    self.generate_options()
    self.display_options_descriptions()
    selection = self.request_input(len(self.options))
    self.chosen_option = self.options[selection-1]
    print("You have chosen: " + self.chosen_option.option_descriptor)
    return


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


  def give_background_to_current_activity(self):
    background_blurb = """
The first act of any hacker is to carry out recconnaissance on your given target.
This can be passive, looking at social media like Facebook and LinkedIn; or googling public information on an organisation (for example, Companies House). 
This is done so that you can better target your approach, such as when an individual's birthday is, or finding out what an organisation's standard format for an email address is. 
How do you want to gather information on your targets today?
    """
    return background_blurb


  def generate_options(self):

    if self.hacker_objective == "install_malware":
      descriptor = "Check social media for common email address formats"
      actions_descriptor = "Combing through LinkedIn, a pattern to the standard emails of the organisation's employees is discovered. FirstName.LastName @organisation.co.uk is the ticket to the next step!"
      install_malware_recce_option1 = Option(self.act_number, descriptor, actions_descriptor)
      descriptor = "Check social media for supply chain partners to impersonate"
      actions_descriptor = "Sweeping eyes back and forth over news articles and organisation websites, a shortlist of partner companies is compiled, pathing the way to the back door!"
      install_malware_recce_option2 = Option(self.act_number, descriptor, actions_descriptor)
      descriptor = "Search for organisational information and charts"
      actions_descriptor = "Company websites are always keen to show off 'The Team' - today the team will be marionettes in a deception."
      install_malware_recce_option3 = Option(self.act_number, descriptor, actions_descriptor)

      self.options.append(install_malware_recce_option1)
      self.options.append(install_malware_recce_option2)
      self.options.append(install_malware_recce_option3)

    if self.hacker_objective == "steal_card_details":
      descriptor = "Gather information on a target from social media"
      actions_descriptor = "The target was keen to share their personal life on social media - now armed with a keener understanding of the target, the next phase can begin"
      steal_card_details_recce_option1 = Option(self.act_number, descriptor, actions_descriptor)
      descriptor = "Procure a large number of phone numbers from illicit vendor"
      actions_descriptor = "The dark web isn't as hard to get onto as people think, and a list of known good phone numbers to 'cold call' with a text costs less than one might think"
      steal_card_details_recce_option2 = Option(self.act_number, descriptor, actions_descriptor)

      self.options.append(steal_card_details_recce_option1)
      self.options.append(steal_card_details_recce_option2)

    if self.hacker_objective == "gain_payment":
      descriptor = "Get number for internal offices"
      actions_descriptor = "Company websites are often poorly mapped and it's not difficult to root around and find other numbers than the customer service line with a little patience"
      gain_payment_recce_option1 = Option(self.act_number, descriptor, actions_descriptor)
      descriptor = "Get internal phone extensions for those who make payments"
      actions_descriptor = "A little charm and a plausible scenario can get others to share extension numbers relatively easily."
      gain_payment_recce_option2 = Option(self.act_number, descriptor, actions_descriptor)
      descriptor = "Find out who the bank regularly makes payments to"
      actions_descriptor = "Get in touch with the right people and they can reveal who the organisation regularly interacts with"
      gain_payment_recce_option3 = Option(self.act_number, descriptor, actions_descriptor)

      self.options.append(gain_payment_recce_option1)
      self.options.append(gain_payment_recce_option2)
      self.options.append(gain_payment_recce_option3)

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
