import pyautogui as pag 
import keyboard as kb
import time

first = (0, 0)
second = (0, 0)
positions = [(0, 0), (0, 0), (0, 0), (0, 0)]
color = (11, 11, 11)


while True:
    screenshot = pag.screenshot()
    if kb.is_pressed('1'):
        first = pag.position()
        del positions
        positions = []
        positions.append(tuple(first))
        positions.append(((second[0] - first[0]) // 3 + first[0], (second[1] - first[1]) // 3 + first[1]))
        positions.append(((second[0] - first[0]) // 3 * 2 + first[0], (second[1] - first[1]) // 3 * 2 + first[1]))
        positions.append(tuple(second))
    elif kb.is_pressed('2'):
        second = pag.position()
        del positions 
        positions = []
        positions.append(tuple(first))
        positions.append(((second[0] - first[0]) // 3 + first[0], (second[1] - first[1]) // 3 + first[1]))
        positions.append(((second[0] - first[0]) // 3 * 2 + first[0], (second[1] - first[1]) // 3 * 2 + first[1]))
        positions.append(tuple(second))
    elif kb.is_pressed('3'):
        color = screenshot.getpixel(tuple(pag.position()))
    if (first != (0, 0)) & (second != (0, 0)):
        print('Options confirm, run!')
        break

while True:
    starttime = time.time()
    screenshot = pag.screenshot()
    for position in positions:
        if screenshot.getpixel(position) == color:
            pag.click(x=position[0], y=position[1])
    difference = time.time()-starttime
    if difference > 0.1:
        print(difference)