import pyautogui as pag 
p = pag.confirm(text = 'You are bot', title ='Conform Box', buttons = ['ok', 'cancel'])
print(p)