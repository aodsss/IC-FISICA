import serial
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

porta = 'COM4'
baud_rate = 9600
arduino = serial.Serial(porta, baud_rate, timeout=1)
time.sleep(2)
arduino.reset_input_buffer()

tempos = []
tensoes = []
maxsize = 10
inicio = time.time()  # Tempo inicial

def animate(i):
    try:
        linha = arduino.readline().decode('utf-8', errors='ignore').strip()

        if linha:
            tensao = float(linha)  # Converte para float (assumindo que a string é um número)
            tempo_decorrido = time.time() - inicio  # Tempo desde o início
            tensoes.append(tensao)
            tempos.append(tempo_decorrido)

        if len(tempos) > maxsize:
            tempos.pop(0)
            tensoes.pop(0)

    except ValueError:
        print(f"Erro ao converter: '{linha}'")

    plt.cla()
    plt.plot(tempos, tensoes, label='Tensão (V)')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Tensão (V)')
    plt.legend(loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.show()
