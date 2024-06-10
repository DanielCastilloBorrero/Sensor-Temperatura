import serial
import time
from math import log, exp

class Temperature():

    def __init__(self):
        self.get_serial()
    
    def get_serial(self):
        try:
            self.serialArduino = serial.Serial('/dev/ttyACM0', baudrate=9600)
            time.sleep(1)
        except serial.SerialException:
            self.serialArduino = None

    def get_temperature(self):
        if self.serialArduino == None:
            return "Sensor no encontrado"
        else: 
            cad = self.serialArduino.readline().decode('ascii')
            return float(cad)
    
    def serial_close(self):
        self.serialArduino.close()

class LeyCalentamiento():   # T = Tm +Ce^(kt)

    def __init__(self):
        pass

    def constante_C(self, tempInicial, tempAmbiente):
        constante_C = tempInicial- tempAmbiente
        return constante_C
    
    def constante_k(self, tempFinal, tempAmbiente, tempInicial, tiempoFinal):
        div = log((tempFinal - tempAmbiente) / self.constante_C(tempInicial, tempAmbiente))
        constante_k = (div / tiempoFinal)
        return float(constante_k)
    
    def temp_estimado(self, tempAmbiente, tempFinal, tempInicial, tiempoFinal):
        tempEstimado = (tempAmbiente + self.constante_C(tempInicial, tempAmbiente) * exp(self.constante_k(tempFinal, tempAmbiente, tempInicial, tiempoFinal) * tiempoFinal))
        return tempEstimado