import tkinter as tk
import serial

# Configuração da porta serial
porta_serial = serial.Serial('/dev/ttyUSB0', 9600)  # Substitua '/dev/ttyUSB0' pela porta serial correta

def acender_led1():
    porta_serial.write(b'1')  # Envia o caractere '1' para acender o LED 1

def apagar_led1():
    porta_serial.write(b'0')  # Envia o caractere '0' para apagar o LED 1

def acender_led2():
    porta_serial.write(b'2')  # Envia o caractere '2' para acender o LED 2

def apagar_led2():
    porta_serial.write(b'3')  # Envia o caractere '3' para apagar o LED 2

# Cria a janela principal
janela = tk.Tk()
janela.title("Controle dos LEDs")

# Cria os botões para o LED 1
lbl_led1 = tk.Label(janela, text="LED 1")
lbl_led1.pack()

btn_acender1 = tk.Button(janela, text="Acender", command=acender_led1)
btn_acender1.pack()

btn_apagar1 = tk.Button(janela, text="Apagar", command=apagar_led1)
btn_apagar1.pack()

# Cria os botões para o LED 2
lbl_led2 = tk.Label(janela, text="LED 2")
lbl_led2.pack()

btn_acender2 = tk.Button(janela, text="Acender", command=acender_led2)
btn_acender2.pack()

btn_apagar2 = tk.Button(janela, text="Apagar", command=apagar_led2)
btn_apagar2.pack()

# Executa o loop principal da interface gráfica
janela.mainloop()
