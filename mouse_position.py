import pyautogui

try:
	while True:
		x,y = pyautogui.position()
		pixelColor = pyautogui.screenshot().getpixel((x,y))
		pos = 'X ' + str(x).rjust(4) + ' Y' + str(y).rjust(4) + ' RGB: ' + str(pixelColor) 
		print(pos, end='')
		print('\b' * len(pos), end='', flush=True)
except KeyboardInterrupt:
	print('Finish')
