import tkinter as tk
import serial

# Configurar a comunicação serial
arduino_port = "/dev/ttyUSB0"  # Substitua pela porta correta
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate, timeout=1)

# Função para enviar o comando para o Arduino
def send_command(letter):
    ser.write(letter.encode())

# Criar a interface gráfica
root = tk.Tk()
root.title("Controle de LEDs em Braille")

# Funções dos botões
def button_pressed(letter):
    send_command(letter)

# Criar os botões para cada letra
letters = "abcdefghijklmnopqrstuvwxyz"
for letter in letters:
    button = tk.Button(root, text=letter, command=lambda l=letter: button_pressed(l))
    button.pack()

# Botão para apagar todos os LEDs
clear_button = tk.Button(root, text="Apagar Todos", command=lambda: send_command(' '))
clear_button.pack()

# Função para fechar a porta serial ao fechar a janela
def close_serial():
    ser.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", close_serial)
root.mainloop()
