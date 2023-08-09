import tkinter as tk
import serial

# Configuração da comunicação serial
arduino_port = "/dev/ttyUSB0"  # Substitua pela porta correta
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate, timeout=1)

# Função para enviar o comando para o Arduino
def send_command(led_index):
    command = str(led_index + 1)  # Envia o índice do LED como um número (1 a 6)
    ser.write(command.encode())

# Criar a interface gráfica
root = tk.Tk()
root.title("Controle de LEDs")

# Função para lidar com o clique de um botão
def button_clicked(index):
    send_command(index)

# Criar os botões em forma de grade (duas colunas e três linhas)
buttons = []
button_frame = tk.Frame(root)
button_frame.pack()

for i in range(3):
    button_left = tk.Button(button_frame, text=f"LED {i + 1}", command=lambda idx=i: button_clicked(idx))
    button_right = tk.Button(button_frame, text=f"LED {i + 4}", command=lambda idx=i + 3: button_clicked(idx + 3))
    
    button_left.grid(row=i, column=0, padx=10, pady=10)
    button_right.grid(row=i, column=1, padx=10, pady=10)
    
    buttons.append(button_left)
    buttons.append(button_right)

# Função para fechar a porta serial ao fechar a janela
def close_serial():
    ser.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", close_serial)
root.mainloop()
