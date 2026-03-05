import time
import pygame

msg = "Welcome to ShotEm the ultimate paintball experience (cause you play as robots)"

print(msg, end="\r", flush=True)
time.sleep(3)
print(" " * len(msg), end="\r")

print("Controls: WASD to move. 'j' to shoot. Type 'quit' to stop.")

char_x = 10
char_y = 10
bullet_color = "blue"

while True:
    action = input(f"Character at ({char_x}, {char_y}). Action: ").lower()

    if action == "w":
        char_y = char_y + 1
    if action == "s":
        char_y = char_y - 1
    if action == "a":
        char_x = char_x - 1
    if action == "d":
        char_x = char_x + 1
    if action == "j":
        print("Character (Rectangle) shot a " + bullet_color + " ball!")
        print("Position: X=" + str(char_x) + " Y=" + str(char_y))
    if action == "quit":
        break
