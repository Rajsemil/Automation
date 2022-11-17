import pyautogui as pag
pag.sleep(5)
while True:
	j = pag.mouseDown()
	k = pag.mouseUp()
	print(j,k)