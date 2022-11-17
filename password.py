import pyautogui as pag 
p = pag.password(text = '', title ='Password Box', mask = '*')
print(p)