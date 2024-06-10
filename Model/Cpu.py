import psutil
import platform as pl
from time import sleep

class Cpu_info():

    def get_cpu(self):
        perfil_so = [
            'processor',
        ]
        for perfil in perfil_so:
            if hasattr(pl, perfil):
                return'%s: %s' % (perfil, getattr(pl, perfil)())
    
    def get_cpu_cores(self):
        return f'Cores: {psutil.cpu_count(logical=False)}'
    
    def get_cpu_threads(self):
        return f'Threads: {psutil.cpu_count(logical=True)}'
    
    def get_cpu_percent(self):
        return psutil.cpu_percent(interval=None)
    
    # Por alguna razon esos metodos de abajo me devuelven una lista y necesito un numero para el label
    def get_cpu_temperature(self):
        temp_cpu = psutil.sensors_temperatures().get('k10temp')
        cadena = str(temp_cpu)
        indice_current = cadena.find('current=')
        indice_coma = cadena.find(',', indice_current)

        temp_cpu = float(cadena[indice_current + len('current='): indice_coma])

        return round(temp_cpu, 1)
    
    def get_gpu_temperature(self):
        temp_gpu = psutil.sensors_temperatures().get('amdgpu')
        cadena = str(temp_gpu)
        indice_current = cadena.find('current=')
        indice_coma = cadena.find(',', indice_current)

        temp_gpu = float(cadena[indice_current + len('current='): indice_coma])

        return round(temp_gpu, 1)
