import serial
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

porta = 'COM4'
baud_rate = 9600
arduino = serial.Serial(porta, baud_rate, timeout=1)
time.sleep(2)
arduino.reset_input_buffer()

plt.style.use('fivethirtyeight')

tempos = []
tensões = []

def animate(i):
    try:
        linha = arduino.readline().decode('utf-8', errors='ignore').strip()

        if linha:  # Garante que a linha não está vazia
            dados = linha.split(',')
            tempos.append(float(dados[0]))
            tensões.append(float(dados[1]))

    except ValueError:
        print(f"Erro ao converter: '{linha}'")  # Caso venha um texto inesperado

    plt.cla()

    plt.plot(tempos, tensões, label='Tensão')

    plt.legend(loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=50)

plt.tight_layout()
plt.show()