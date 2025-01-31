import pyautogui as pg
import actions
import constants

def kill_GM():
    cont = 0
    for GM, imagem in constants.GMs.items():
        for nome, caminho in imagem.items():
            
            if nome == 'life':
                print(imagem[nome])
                break
                #if pg.locateAllOnScreen(constants.GMs[nome][caminho]):
                    #actions.kill_monster(constants.GMs[nome][caminho])

#print(constants.GMs['GM']['image'])
kill_GM()