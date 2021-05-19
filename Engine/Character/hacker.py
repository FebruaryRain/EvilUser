import random

class Hacker:

  # FOH = Front Of House (Customer Facing)
  # BOH = Back Of House (non-Customer Facing)

# True and False for FOH and BOH is arbitrary to aid in ensuring that values all pass correctly at a later date, only for use during testing
  phishing_hacker = {"actor_type": "smish_hacker", 
                  "objectives": "install_malware",
                  "for_FOH": True,
                  "for_BOH": True
                  } 

  smish_hacker = {"actor_type": "smish_hacker", 
                  "objectives": "steal_card_details",
                  "for_FOH": False,
                  "for_BOH": True
                  } 

  vish_hacker = {"actor_type": "vish_hacker", 
                  "objectives": "gain_payment",
                  "for_FOH": True,
                  "for_BOH": False
                  } 

  all_hackers=[phishing_hacker, smish_hacker, vish_hacker]

  def __init__(self):
    self.first_name = ""
    self.generate_first_name()
    self.surname = ""
    self.generate_surname()
    self.hackers_list = Hacker.all_hackers

    # Sanity Checks
    #print(self.hackers_list)
    #for hacker in self.hackers_list:
    #  if hacker["for_FOH"]:
    #    print(hacker["actor_type"])

    return


  def generate_first_name(self):
    first_name_list = ["Sandra","Victor","Michael","Anna","Brian","Belle","Shelley","William"]
    self.first_name = random.choice(first_name_list)
    return 


  def generate_surname(self):
    last_name_list = ["McVeigh","Paterson","Reynolds","Vicks","Gruffudd","Blanc","Stern","Blake"]
    self.surname = random.choice(last_name_list)
    return 


  def get_full_name(self):
    full_name = self.first_name + " " + self.surname
    return full_name


  def get_hackers_list(self):
    return self.hackers_list