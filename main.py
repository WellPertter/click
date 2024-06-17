import pyautogui
import keyboard

def click_left():
    pyautogui.click(button='left')

def click_right():
    pyautogui.click(button='right')

def main():

    # Definindo hotkeys globais
    keyboard.add_hotkey('f8', click_left)
    keyboard.add_hotkey('f9', click_right)

    # Manter o script rodando até que 'esc' seja pressionado
    try:
        while True:
            if keyboard.is_pressed('esc'):
                print("Saindo...")
                break
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
