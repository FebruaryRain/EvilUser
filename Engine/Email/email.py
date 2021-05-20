from email.utils import parseaddr
from Utils.email_validator import validate_email
import curses
import hashlib

class Email():

    def __init__(self, sender, recipient, contents, subject="", cc = [], bcc = []):
        self.sender = sender
        self.subject = subject
        self.recipient = recipient
        self.cc = cc
        self.bcc = bcc
        self.contents = contents
        self.update_uid()

    def set_sender(self, sender):
        self.sender = sender
        self.update_uid()


    def set_subject(self, subject):
        self.subject = subject
        self.update_uid()


    def set_recipient(self, recipient):
        self.recipient = recipient
        self.update_uid()
    
    def set_cc(self, cc = []):
        self.cc = cc
        self.update_uid()

    def set_bcc(self, bcc = []):
        self.bcc = bcc
        self.update_uid()

    def set_contents(self, contents):
        self.contents = contents
        self.update_uid()
        

    def update_uid(self):
        uidHasher = hashlib.sha3_512(str(self.sender+self.subject+''.join(self.cc)+''.join(self.bcc)+self.contents+''.join(self.cc)).encode())
        self.uid = uidHasher.hexdigest()

    def is_valid(self):
        if self.recipient == "*":
            if len(self.cc) > 0:
                for i in self.cc:
                    if i != "*":
                        return False
            if len(self.bcc) > 0:
                for i in self.bcc:
                    if i != "*":
                        return False
            return True
        if validate_email(self.sender) == False:
            return False
        if validate_email(self.recipient) == False:
            return False
        if len(self.cc) > 0:
            for i in self.cc:
                if validate_email(i) == False:
                    return False
        if len(self.bcc) > 0:
            for i in self.bcc:
                if validate_email(i) == False:
                    return False
        return True
    
    def __str__(self):
        curses.setupterm()
        string = "="*curses.tigetnum("cols")
        string += "Sender: " + self.sender
        string += "\nRecipient: " + self.recipient
        string += "\ncc: " + ''.join(self.cc)
        string += "\nSubject: " + self.subject
        string += "\n"+("="*curses.tigetnum("cols"))
        string += "\nContents: \n\n" + self.contents
        string += "\n"+("="*curses.tigetnum("cols"))
        return string

        

