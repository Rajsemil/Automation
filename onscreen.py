# onscreen show creen current height and width  is that present and not true or false 
import pyautogui
ons = pyautogui.onScreen(int(input("Enter a width: ",)), int(input("Enter a height: ")))
print(ons)