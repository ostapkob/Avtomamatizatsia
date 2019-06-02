import pyautogui, subprocess
from PIL import ImageColor, Image

pyautogui.PAUSE = 0.05
pyautogui.FAILSAFE =True
print(pyautogui.size())
width, height = pyautogui.size()
#===========MOVE===========
for _ in range(0):
	pyautogui.moveTo(100, 100, duration=0.25)
	pyautogui.moveTo(500, 100, duration=0.25)
	pyautogui.moveTo(500, 500, duration=0.25)
	pyautogui.moveTo(100, 500, duration=0.25)
for _ in range(0):
	pyautogui.moveRel(100, 0, duration=0.25)
	pyautogui.moveRel(0, 100, duration=0.25)
	pyautogui.moveRel(-100, 0, duration=0.25)
	pyautogui.moveRel(0, -100, duration=0.25)
#==========MOUSE==================
# print(pyautogui.position())
# pyautogui.click(10,5)
# pyautogui.click(1000,500, button='right')
# pyautogui.mouseDown(300,20)
# pyautogui.mouseUp(800,20)
# pyautogui.doubleClick(800,15)
# subprocess.Popen(['C:\\Windows\\system32\\mspaint.exe', 'D:\\YandexDisk\\IMG\\_D_fUvaCOhs.jpg']) #  work in Win and Lin
# pyautogui.mouseDown(230,230)
# pyautogui.mouseUp(300,320)
# pyautogui.click(200,200)
# pyautogui.scroll(-1500)

#===========DRAW===================
pyautogui.click(200,200)
pyautogui.PAUSE
rectangle = 5
distance = 200
while distance>0:
	pyautogui.dragRel(distance, 0, duration=0.02)
	distance -=rectangle
	pyautogui.dragRel(0, distance, duration=0.02)
	pyautogui.dragRel(-distance, 0, duration=0.02)
	distance-=rectangle
	pyautogui.dragRel(0, -distance, duration=0.02)

#===========FIND===================
# im = pyautogui.screenshot()
# xy_rgb = pyautogui.pixelMatchesColor(20,200,(240,240,240))
# print(xy_rgb)
# find = None
# try:

# 	find = pyautogui.locateOnScreen('find.png')
# 	center_ = pyautogui.center(find)
# 	pyautogui.click(center_)
# except Exception as ex:
# 	print (ex)
# print(find)
# im = Image.new('RGB',(50,50), rgb).show()
#===========KEYBOARD=======================
# pyautogui.click(200,200); pyautogui.typewrite('Python is the best! \t', .25)
# pyautogui.typewrite(['a', 'b', 'left', 'left', 'backspase', 'del', 'tab'], .20)
# pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')
# pyautogui.hotkey('ctrl', 'a')

# pyautogui.hotkey('ctrl', 'c')




