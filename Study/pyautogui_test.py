# import pyautogui
# pyautogui.FAILSAFE = False
# # 获取当前屏幕分辨率
# screenWidth, screenHeight = pyautogui.size()
# # 获取当前鼠标位置
# currentMouseX, currentMouseY = pyautogui.position()
# pyautogui.moveTo(x=100, y=100,duration=2, tween=pyautogui.linear)
# pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
# pyautogui.click()
# pyautogui.doubleClick()


import  os
import  time
import pyautogui
import pyautogui as pag
pyautogui.FAILSAFE = False
try:
    while True:
        print("Press Ctrl-C to end")
        screenWidth, screenHeight = pag.size()  #获取屏幕的尺寸
        print(screenWidth,screenHeight)
        x,y = pag.position()   #获取当前鼠标的位置
        posStr = "Position:" + str(x).rjust(4)+','+str(y).rjust(4)
        print(posStr)
        time.sleep(0.2)
        os.system('cls')   #清楚屏幕
except KeyboardInterrupt:
    print('end....')

