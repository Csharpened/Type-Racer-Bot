from pynput.keyboard import Key, Controller
import pytesseract
import pyautogui
import time

keyboard = Controller()

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\jonat\AppData\Local\Programs\Tesseract-OCR\tesseract'

time.sleep(5)
im = pyautogui.screenshot(region=(130,453,1109,321))
text = pytesseract.image_to_string(im)

print(text)
for i in text:
    if i == '|':
        keyboard.press("I")
    if i == 'F':
        keyboard.press("f")
    else:
        keyboard.press(i)
        keyboard.release(i)
    time.sleep(0.001)



