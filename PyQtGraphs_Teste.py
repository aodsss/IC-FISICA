import serial
import time
import threading
from collections import deque
from PyQt6 import QtWidgets
import pyqtgraph as pg
import sys

# Configuração da porta serial
arduino = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)
arduino.reset_input_buffer()

# Deques para manter tamanho fixo
maxsize = 100
tempos = deque([0.0] * maxsize, maxlen=maxsize)
tensoes = deque([0.0] * maxsize, maxlen=maxsize)

# Função de leitura contínua em thread separada
def leitura_serial():
    while True:
        try:
            linha = arduino.readline().decode('utf-8', errors='ignore').strip()
            if linha:
                dados = linha.split(',')
                if len(dados) == 2:
                    tempo = float(dados[0])
                    tensao = float(dados[1])
                    tempos.append(tempo)
                    tensoes.append(tensao)
        except:
            continue

# Inicia thread de leitura
thread_serial = threading.Thread(target=leitura_serial, daemon=True)
thread_serial.start()

# Criação da janela e gráfico
app = QtWidgets.QApplication(sys.argv)
janela = pg.GraphicsLayoutWidget(show=True)
janela.resize(800, 500)
grafico = janela.addPlot()
grafico.setYRange(0, 5)
linha_plotada = grafico.plot([], [], pen=pg.mkPen('r', width=2))

# Atualiza apenas a visualização
def update_plot():
    linha_plotada.setData(list(tempos), list(tensoes))

# Timer PyQt para atualizar o gráfico
timer = pg.QtCore.QTimer()
timer.timeout.connect(update_plot)
timer.start(10)

# Inicia o app
sys.exit(app.exec())
