from enum import Enum
import random

class Location(Enum):
        NONE = 0
        PHONE = 1
        COMPUTER = 2
        SERVER = 3
        EMAIL = 4
        DOMAIN = 5

class Theme(Enum):
    NONE = 0
    COVID = 1
    HEALTH = 2
    WITHDRAWAL = 4
    DEPOSIT = 5
    LOTTERY = 6
    TAX = 7
    UTILITIES = 8
    TECH_PROVIDER = 9
    ISP = 10
    DELIVERY = 11
    RETAILER = 12

    def build(self):
        if self.NONE:
            return [""]
        elif self.COVID:
            return {"BEGINNING":["URGENT:\nGOVuk\n","URGENT:\nGOV UK","GOV.UK\nCORONAVIRUS ALERT\n","GOV.UK\nCOVID-19\n","GOVUK\nCOVID ALERT\n"],
                    "MIDDLE":[
                            "you're area has been effected by coronavirus;\n",
                            "Your area has been badly affected by COVID-19, a bursary is being given out.\n",
                            "Your area has been effected by Coronavirus; new rules are now in force in your area.\n"]
                    }
        elif self.HEALTH:
            return {"BEGINNING": ["NHS\n", "RED-CROSS\n", "VITALITY INSURANCE\n", "BUPA\n", "AVIVA\n", "FREEDOM HEALTH INSURANCE\n"],
                    "MIDDLE":[
                            "your medical care is now voided. youre unable to log in to see your plan\n",
                            "Due to recent discoveries about your health, we are disabling your account. If you think this is wrong then ",
                            "Your medical care number has been lost, due to this you cannot access your care. Please inform us using "
                    ]}
        elif self.WITHDRAWAL:
            return {"BEGINNING": ["BARCLAYS\n", "HSBC\n","LLOYDS\n","TESCO\n","CO-OPERATIVE\n","STARLING\n","ROYAL BANK OF SCOTLAND\n","BANK OF ENGLAND\n","SANTANDER\n","NATIONWIDE\n"],
                    "MIDDLE": [""]}
        elif self.DEPOSIT:
            return {"BEGINNING": [""],
                    "MIDDLE": [""]}
        elif self.LOTTERY:
            return {"BEGINNING": [""],
                    "MIDDLE": [""]}
        elif self.TAX:
            return {"BEGINNING": [""],
                    "MIDDLE": [""]}
        elif self.UTILITIES:
            return {"BEGINNING": [""],
                    "MIDDLE": [""]}
        elif self.TECH_PROVIDER:
            return {"BEGINNING": [""],
                    "MIDDLE": [""]}
        elif self.ISP:
            return {"BEGINNING": [""],
                    "MIDDLE": [""]}
        elif self.DELIVERY:
            return {"BEGINNING": [""],
                    "MIDDLE": [""]}
        elif self.RETAILER:
            return {"BEGINNING": [""],
                    "MIDDLE": [""]}


class Cyber_Threat():

    chance_of_success = random.random()
    elaboration = random.random()

    location = Location.NONE
    theme = Theme.NONE

    def __init__(self):
        return

    def generate_threat(self):
        return
