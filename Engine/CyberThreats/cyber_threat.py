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
    WITHDRAWAL = 3
    DEPOSIT = 4
    LOTTERY = 5
    TAX = 6
    UTILITIES = 7
    TECH_PROVIDER = 8
    ISP = 9
    DELIVERY = 10
    RETAILER = 11

    def build(self):
        if self.value == 0:
            return {"BEGINNING":[""],"MIDDLE":[""]}
        elif self.value == 1:
            return {"BEGINNING":["URGENT:\nGOVuk\n","URGENT:\nGOV UK","GOV.UK\nCORONAVIRUS ALERT\n","GOV.UK\nCOVID-19\n","GOVUK\nCOVID ALERT\n"],
                    "MIDDLE":[
                            "you're area has been effected by coronavirus; we can only give you the details ",
                            "Your area has been badly affected by COVID-19, a bursary is being given out. Claim your bursary ",
                            "Your area has been effected by Coronavirus; new rules are now in force in your area. To receive the details we can give you them "]
                    }
        elif self.value == 2:
            return {"BEGINNING": ["NHS\n", "RED-CROSS\n", "VITALITY INSURANCE\n", "BUPA\n", "AVIVA\n", "FREEDOM HEALTH INSURANCE\n"],
                    "MIDDLE":[
                            "your medical care is now voided. youre unable to log in to see your plan. We can resolve this for you ",
                            "Due to recent discoveries about your health, we are disabling your account. If you think this is wrong then please help us resolve this ",
                            "Your medical care number has been lost, due to this you cannot access your care. Please inform us "
                    ]}
        elif self.value == 3:
            return {"BEGINNING": ["BARCLAYS\n", "HSBC\n","LLOYDS\n","TESCO\n","CO-OPERATIVE\n","STARLING\n","ROYAL BANK OF SCOTLAND\n","BANK OF ENGLAND\n","SANTANDER\n","NATIONWIDE\n"],
                    "MIDDLE":[
                            "WITHDRAWAL, PERS ACCT - youve spent £"+str(random.randint(1000,7000)+round(random.random(),2))+" from your account ending in "+str(random.randint(1000,9999))+". If this is not you, inform us please "
                            ]}
        elif self.value == 4:
            return {"BEGINNING": ["BARCLAYS\n", "HSBC\n","LLOYDS\n","TESCO\n","CO-OPERATIVE\n","STARLING\n","ROYAL BANK OF SCOTLAND\n","BANK OF ENGLAND\n","SANTANDER\n","NATIONWIDE\n"],
                    "MIDDLE": ["ATTEMPTED DEPOSIT, PERS ACCT - weve tried to deposit £"+str(random.randint(1000,7000)+round(random.random(),2))+" to your account ending in "+str(random.randint(1000,9999))+", this is not working. We need more information to continue. To give us more informtion, inform us please "]}
        elif self.value == 5:
            return {"BEGINNING": ["EURO MILLIONS\n", "POST CODE LOTTERY\n", "THE NATIONAL LOTTERY\n"],
                    "MIDDLE": ["CONGRATULATIONS! You have won the jackpot of our lottery! With the numbers you have chosen you have been our LUCKY WINNER! YOU MUST REPLY WITHIN 25HRS TO CLAIM YOUR WINNINGS!\nTo confirm please: "]}
        elif self.value == 6:
            return {"BEGINNING": ["HMRC\n", "GOVUK\n"],
                    "MIDDLE": ["You have a tax refund of £"+str(random.randint(125,2768)+round(random.random(),2))+" pending for you to collect. To confirm this is you and collect your refund please: "]}
        elif self.value == 7:
            return {"BEGINNING":[""],
                    "MIDDLE": [""]}
        elif self.value == 8:
            return {"BEGINNING":[""],
                    "MIDDLE": [""]}
        elif self.value == 9:
            return {"BEGINNING": [""],
                    "MIDDLE": [""]}
        elif self.value == 10:
            return {"BEGINNING": [""],
                    "MIDDLE": [""]}
        elif self.value == 11:
            return {"BEGINNING": [""],
                    "MIDDLE": [""]}


class Cyber_Threat():

    chance_of_success = 0.0
    elaboration = 0.0

    location = Location.NONE
    theme = Theme.NONE

    def __init__(self):
        self.chance_of_success = random.random()
        self.elaboration = random.random()

    def generate_threat(self):
        return
