import pyautogui as pag 
pag.sleep(4)
# write function is used auto write
# interval is used to typing speed 
pag.write(input("Enter characters: "), interval=0.10)
pag.sleep(5)
pag.press("Enter")