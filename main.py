import pyautogui
import keyboard
import tkinter as tk

def click_left():
    pyautogui.click(button='left')

def click_right():
    pyautogui.click(button='right')

def on_closing():
    root.destroy()

def close_program(event=None):
    on_closing()

def main():
    # Definindo hotkeys globais
    keyboard.add_hotkey('f8', click_left)
    keyboard.add_hotkey('f9', click_right)

    # Criando a interface gráfica
    global root
    root = tk.Tk()
    root.title("Click-Key-Hots")

    # Dimensões da janela
    window_width = 320
    window_height = 100

    # Centralizar a janela na tela
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    root.protocol("WM_DELETE_WINDOW", on_closing)

    label = tk.Label(root, text="Sistema de Click-Key-Hots está rodando.\nPressione F8 para clique esquerdo, F9 para clique direito.")
    label.pack(pady=20)

    # Vinculando a tecla ESC ao fechamento do programa
    root.bind('<Escape>', close_program)

    # Manter a janela aberta
    root.mainloop()

if __name__ == "__main__":
    main()
