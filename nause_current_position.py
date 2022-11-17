import pyautogui
while True:
	x,y = pyautogui.position()
	print(f"x:{x} y:{y}")
	pyautogui.sleep(2)