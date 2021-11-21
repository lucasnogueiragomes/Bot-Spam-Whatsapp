import pyautogui, time 
time.sleep(10)
texto = open('roteiro.txt')
for frase in texto:
    pyautogui.typewrite(frase)
    pyautogui.press('enter')
                                    