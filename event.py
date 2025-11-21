import keyboard

print("Press ESC to quit.")
while True:
    if keyboard.is_pressed("esc"):
        print("Goodbye")
        break