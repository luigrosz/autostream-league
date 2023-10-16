import pyautogui
import ctypes
import time
from pynput.mouse import Button, Controller

mouse = Controller()


global in_game, accounts
in_game = True

url = "https://www.op.gg/summoners/"


def main():
    if in_game:
        wait_game_to_finish()
    else:
        search_for_game()


def wait_game_to_finish():
    while 1:
        # click the finish game button
        if pyautogui.locateOnScreen('end.png', confidence=0.9) != None:
            mouse.position = (960, 640)
            mouse.press(Button.left)
            time.sleep(0.1)
            mouse.release(Button.left)
        else:
            time.sleep(1)


def search_for_game():
    # todo
    print('searching for game...')
    with open("accounts.txt", "r") as txt_file:
        accounts = txt_file.readlines()
        for account in accounts:
            region = account.split(' ').pop(0)

            print(account)
    # while 1:
    #     print('\naccounts:')
    #     print(accounts)
    #     time.sleep(20)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    main()
else:
    print('Re-launch the terminal with admin rights')
