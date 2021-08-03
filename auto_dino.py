import time
import keyboard
import pyautogui
dino = (518,333)
obs1 = (710,329)
obs2 = (673,322)
obs3 = (740,322)
obs4 = (754,301)
while True:
	screen_shot = pyautogui.screenshot()
	pix1 = screen_shot.getpixel((obs1))
	pix2 = screen_shot.getpixel((obs2))
	pix3 = screen_shot.getpixel((obs3))
	pix4 = screen_shot.getpixel((obs4))

	if(int(pix1[0])<255 or int(pix2[0])<255 or int(pix3[0])<255 or int(pix4[0])<255):
		pyautogui.press('space')
		time.sleep(0.00001)