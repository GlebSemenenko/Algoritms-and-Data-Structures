import random
import time
import pyautogui

pyautogui.FAILSAFE = True

try:
    width, height = pyautogui.size()

    while True:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        delay = random.randint(1, 95)

        print(f"Click at ({x}, {y}), next in {delay} sec")
        pyautogui.click(x, y)

        time.sleep(delay)

except KeyboardInterrupt:
    print("Stopped by user")