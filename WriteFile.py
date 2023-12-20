import pyautogui

f = open("File.txt", 'r')
for word in f:
    pyautogui.typewrite(word, interval = 0.09)

