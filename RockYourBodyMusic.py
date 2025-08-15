from rich import print
from time import sleep

#install rich in Terminal

def type_line(text, letter_delay):
    for char in text:
        print(char, end="", flush=True)
        sleep(letter_delay)
    print()  

def printLyrics():
    lines = [
        ("I wanna da-", 0.06), #1
        ("I wanna dance in the lights", 0.05), #2
        ("I wanna ro-", 0.07),#3
        ("I wanna rock your body", 0.08), #4
        ("I wanna go", 0.08), #5
        ("I wanna go for a ride", 0.068), #6
        ("Hop in the music and", 0.07), #7
        ("Rock your body", 0.08), #8
        ("Rock that body", 0.069), #9
        ("come on, come on", 0.035), #10
        ("Rock that body", 0.05), #11
        ("(Rock your body)", 0.03), #12
        ("Rock that body (Come on , Come on)", 0.049), #13
        ("Rock Your body", 0.035) #14

    ]

    for text, delay in lines:
        type_line(text, delay)

printLyrics()

