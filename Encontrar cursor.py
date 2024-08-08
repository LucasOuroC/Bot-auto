import pyautogui
import time

print("Mova o ponteiro do mouse para a posição desejada e pressione Enter...")

time.sleep(5)

position = pyautogui.position()

print(f"A posição do ponteiro do mouse é: {position}")
