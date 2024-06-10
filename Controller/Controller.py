from matplotlib import animation
from View import Root, Processor
from Model import Cpu, Venv

class ProcessorView():
    
    def __init__(self):

        # Inicializando el View y el Model
        self.root = Root.Root()
        self.cpu = Cpu.Cpu_info()
        self.venv = Venv.Temperature()
        self.law = Venv.LeyCalentamiento()
        self.frame = Processor.ProcessorView(self.root)
        
        # Seteando texto en los labels en el View 
        self.cpu_name()
        self.cpu_percent()
        self.cores_cpu()
        self.threads_cpu()
        self.cpu_gpu_temp()
        self.temp_ext()

        self.root.start_mainloop()
    
    def cpu_name(self):
        self.frame.set_NameCpu(name=self.cpu.get_cpu())
    
    def cpu_percent(self):
        self.frame.set_labelPercentCpu(percent=self.cpu.get_cpu_percent())
        self.root.after(1000, self.cpu_percent)
    
    def cores_cpu(self):
        self.frame.set_labelCoresCpu(cores=self.cpu.get_cpu_cores())

    def threads_cpu(self):
        self.frame.set_labelThreadsCpu(threads=self.cpu.get_cpu_threads())

    def cpu_gpu_temp(self):
        self.frame.set_tempCpuGpu(cpu=self.cpu.get_cpu_temperature(), 
                                  gpu=self.cpu.get_gpu_temperature(),
                                  est_cpu=self.law.temp_estimado(tempAmbiente=self.venv.get_temperature(), 
                                                                 tempInicial=self.cpu.get_cpu_temperature(), 
                                                                 tempFinal=self.cpu.get_cpu_temperature(),
                                                                 tiempoFinal=30))
        self.root.after(1000, self.cpu_gpu_temp)

    def temp_ext(self):
        self.frame.set_tempExt(temp=self.venv.get_temperature())
        self.root.after(1000, self.temp_ext)