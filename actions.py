import pyautogui as pg

#Usa BM3 pula pra barra de skills da BM e seguro o botão da primeira skill
def kill_monster(monstro):
    
    pg.hotkey('alt', '3')
    pg.press('f2')
    while pg.locateOnScreen(monstro) == True:
        pg.hold('1')
    