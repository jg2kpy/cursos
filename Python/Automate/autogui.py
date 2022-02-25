import pyautogui
width, height = pyautogui.size()
print(pyautogui.position())

try:
    #Mouse
    pyautogui.moveTo(10, 10, duration=1.5)
    pyautogui.moveRel(200, 0, duration=2)
    pyautogui.moveRel(0, -100, duration=2)

    pyautogui.click()
    pyautogui.click(416, 22)
    pyautogui.doubleClick(416, 22)
    pyautogui.middleClick(416, 22)

    #Keyboard
    pyautogui.click(200,200)
    pyautogui.typewrite('Hello World!',interval=0.2)
    pyautogui.typewrite(['a','b','left','left','X','Y'],interval=0.2)
    pyautogui.typewrite('f1')

    #Screenshot
    pyautogui.screenshot()
except:
    print('Programa terminado por el usuario')