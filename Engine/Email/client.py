from .email import Email
import curses
from Utils.multi_line_input import *
class Email_Client():
    emails = {
        "inbox":[],
        "outbox":[],
        "sent":[],
        "drafts":[]    
        }

    currentFolder = ""


    def __init__(self):
        self.currentFolder = "inbox"
        
    def receive_email(self, email):
        self.emails["inbox"].append(email)

    def read_email_by_position_in_array(self, pos):
        self.read_email_by_array_pos_in_folder("inbox", pos)

    def read_email_by_pos(self, pos):
        self.read_email_by_pos_in_folder("inbox", pos)

    def read_email_by_uid(self, uid):
        self.read_email_by_uid_in_folder("inbox", uid)

    def compose_email(self, player_email):
        curses.setupterm()
        curses.update_lines_cols()
        print("="*curses.tigetnum("cols"))
        sender = player_email
        recipient = input("Recipient: ")
        print("Use ctrl+D to cancel.")
        cc = multi_line_input("cc: ")
        print("Use ctrl+D to cancel.")
        bcc = multi_line_input("bcc: ")
        subject = input("subject: ")
        print("Use ctrl+D to cancel.")
        print("Contents:")
        contents = multi_line_input()
        print("="*curses.tigetnum("cols"))
        if input("Send email? [y/n] ").lower() == 'y':
            self.send_email(Email(sender, recipient, contents, subject, cc.splitlines(), bcc.splitlines()))
        elif input("Save email? [y/n] ").lower() == "y":
            self.emails["drafts"].append(Email(sender, recipient, contents, subject, cc.splitlines(), bcc.splitlines()))
        
    def print_folder(self, folder):
        folders = list(self.emails)
        if folder not in folders:
            print(folder + " is not a folder")
            return
        curses.setupterm()
        curses.update_lines_cols()
        print("="*curses.tigetnum("cols"))
        for i in self.emails[folder]:
            shortUid = ""
            for j in range (0,min(len(i.uid), curses.tigetnum("cols") - len(i.sender + "\t" + i.subject + "\t"))):
                shortUid += i.uid[j]
            print(i.sender + "\t" + i.subject + "\t" + shortUid)
        print("="*curses.tigetnum("cols"))

    def edit_email_in_folder(self, player_email, folder, uid):
        if folder == "sent":
            print("You can't edit sent emails!")
            return
        if folder == "inbox":
            print("You can't edit received emails!")
            return
        curses.setupterm()
        curses.update_lines_cols()
        if input("Are you sure you want to edit this email, saving the email will override all contents of the email. [y/n] ").lower() == "n":
            return
        print("="*curses.tigetnum("cols"))
        sender = player_email
        recipient = input("Recipient: ")
        print("Use ctrl+D to cancel.")
        cc = multi_line_input("cc: ")
        print("Use ctrl+D to cancel.")
        bcc = multi_line_input("bcc: ")
        subject = input("subject: ")
        print("Use ctrl+D to cancel.")
        print("Contents:")
        contents = multi_line_input()
        print("="*curses.tigetnum("cols"))
        if input("Are you sure you want to save this email, saving the email will override all contents of the email. [y/n] ").lower() == "n":
            return
        for i in self.emails[folder]:
            if uid in i.uid:
                i.set_sender = sender
                i.set_recipient = recipient
                i.set_cc = cc.splitlines()
                i.set_bcc = bcc.splitlines()
                i.set_contents = contents()
                return

    def print_inbox(self):
        self.print_folder("inbox")

    def print_outbox(self):
        self.print_folder("outbox")

    def print_sent_box(self):
        self.print_folder("sent")

    def print_drafts(self):
        self.print_folder("drafts")

    def print_current_folder(self):
        self.print_folder(self.currentFolder)

    def read_email_by_pos_in_folder(self, folder, pos):
        print(self.emails[folder][pos-1])

    def read_email_by_array_pos_in_folder(self, folder, pos):
        print(self.emails[folder][pos])

    def read_email_by_uid_in_folder(self, folder, uid):
        for i in self.emails[folder]:
            if uid in i.uid:
                print(i)
                return

    """
    Send an email using the client, email must be of email object
    Returns true is successful, returns false if failure
    If failure email resides in outbox, else it is in the sent box
    """
    def send_email(self, email):
        if email in self.emails["drafts"]:
            self.emails["drafts"].remove(email)
        if email not in self.emails["outbox"]:
            self.emails["outbox"].append(email)
        if email.is_valid():
            self.emails["outbox"].remove(email)
            self.emails["sent"].append(email)
            return True
        else:
            return False
