import serial
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

arduino = serial.Serial('COM4', 4800, timeout=1)
time.sleep(2)
arduino.reset_input_buffer()

tempos = []
tensoes = []

def animate(i):
    linha = arduino.readline().decode('utf-8', errors='ignore').strip()

    dados = linha.split(',')
    tempos.append(float(dados[0]))
    tensoes.append(float(dados[1]))
    
    if len(tempos) > 20:
        tempos.pop(0)
        tensoes.pop(0)

    plt.cla()

    plt.plot(tempos, tensoes)

ani = FuncAnimation(plt.gcf(), animate, interval=100)
plt.ylim(0, 5)
plt.tight_layout()
plt.show()