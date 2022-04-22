import pyautogui, keyboard, time

running = False

print("Welcome to Auto-Clicker (made by Anh Đức)")
click_type = input("Single click or double click? (s for single click, d for double click) ")
while click_type != "s" and click_type != "d":
    print("Hey!. Invalid response")
    click_type = input("Single click or double click? (s for single click, d for double click) ")
duration = float(input("Duration between each click? (in seconds)"))
print("Press F6 to start, spam F8 to stop program")

while True:
    if running == False and keyboard.is_pressed("f6"):
        running = True
    while running:

        if keyboard.is_pressed("f8"):
            quit()

        time.sleep(duration)

        if keyboard.is_pressed("f8"):
            quit()

        if click_type == "s":
            pyautogui.click(pyautogui.position())
        else:
            pyautogui.click(pyautogui.position())
            pyautogui.click(pyautogui.position())

        if keyboard.is_pressed("f8"):
            quit()
    if keyboard.is_pressed("f8"):
        quit()
