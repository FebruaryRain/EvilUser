EvilUser
========

Lloyds x IBM Hackathon project
------------------------------

How to run from terminal to use curses:

- This app will not currently work in IDLE due to unhandled exceptions from curses which can only operate on a terminal or command line

- This app *can* take a single command-line argument for if it should run in demo mode or not and is case sensitive.

- Example usage: `python3 Engine/main.py True` or if you are on mac/linux you can run `sh run.sh` (this will also work if you have a shell on Windows (e.g git for Windows))

Structure of the repo and application
-------------------------------------

- [The main class](Engine/main.py) contains the main game loop and main class.

- The packages contain all classes relevent to themselves and heavily used generic classes belong in the [util package](Engine/Utils) such as multi-line input and email validation.
