import pyautogui
pyautogui.FAILSAFE = False
# 获取当前屏幕分辨率
screenWidth, screenHeight = pyautogui.size()
# 获取当前鼠标位置
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.moveTo(x=100, y=100,duration=2, tween=pyautogui.linear)
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
pyautogui.click()
pyautogui.doubleClick()



