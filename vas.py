import random
import time
import pyautogui

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.05

screen_width, screen_height = pyautogui.size()

min_delay = 30
max_delay = 120

print("Старт через 3 секунды. Остановить можно, уведя мышь в угол экрана.")
time.sleep(3)

try:
    while True:
        x = random.randint(0, screen_width - 1)
        y = random.randint(0, screen_height - 1)

        print(f"Клик по координатам: x={x}, y={y}")
        pyautogui.click(x, y)

        delay = random.uniform(min_delay, max_delay)
        print(f"Следующий клик через {delay:.2f} сек")
        time.sleep(delay)

except pyautogui.FailSafeException:
    print("Остановлено через fail-safe.")
except KeyboardInterrupt:
    print("Остановлено вручную.")