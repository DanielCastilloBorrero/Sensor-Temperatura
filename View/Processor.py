import tkinter as tk
from tkinter import ttk

class ProcessorView(tk.Frame):

    def __init__(self, master):
        super().__init__(master=master)
        self.config(bg="#ffffff", border=5)
        self.pack(fill='both', expand=True, padx=10, pady=10)

        # Treeveiew
        self.arbol = ttk.Treeview(self, columns=("Value", "estimated_value"))
        
        # Columna Hardware
        self.arbol.heading("#0", text="Info Hardware")
        self.arbol.column("#0", width=400)
        self.name_cpu = self.arbol.insert("", 
                                          tk.END, 
                                          iid="nameCpu", 
                                          open=True, 
                                          image=tk.PhotoImage(file="View/src/procesador.png"))

        # Columna Info
        self.arbol.heading("Value", text="Value")
        self.arbol.column("Value", anchor="center")
        self.cpuPercent = self.arbol.insert(self.name_cpu, tk.END, iid='cpuPercent')
        self.cpuCores = self.arbol.insert(self.name_cpu, tk.END, iid='cpuCores')
        self.cpuThreads = self.arbol.insert(self.name_cpu, tk.END, iid='cpuThreads')
        self.temperatures = self.arbol.insert(self.name_cpu, 
                                              tk.END, 
                                              text='Temperatura', 
                                              open=True,
                                              image=tk.PhotoImage(file="View/src/termometro.png"))

        # Columna Temperatura
        self.cpuTemperature = self.arbol.insert(self.temperatures, tk.END, iid='cpuTemperature')
        self.gpuTemperature = self.arbol.insert(self.temperatures, tk.END, iid='gpuTemperature')
        self.arduinoTemperature = self.arbol.insert(self.temperatures, tk.END, iid='arduinoTemperature')

        # Columna Estimado
        self.arbol.heading("estimated_value", text="Estimated")
        self.arbol.column("estimated_value", anchor="center")

        self.arbol.pack(fill='both')
    
    def set_NameCpu(self, name):
        self.arbol.item("nameCpu", text=f"{name}(AMD® Ryzen 5 5500u)")

    def set_labelPercentCpu(self, percent):
        self.arbol.item("cpuPercent", text=f"Porcentaje de Uso (%)", values=percent)

    def set_labelCoresCpu(self, cores):
        self.arbol.item("cpuCores", text=f"Nucleos: {cores}")
    
    def set_labelThreadsCpu(self, threads):
        self.arbol.item("cpuThreads", text=f"Hilos: {threads}")

    def set_tempCpuGpu(self, cpu, gpu, est_cpu):
        self.arbol.item("cpuTemperature", text=f"Temperatura CPU: [°C]", values=(cpu, est_cpu))
        self.arbol.item("gpuTemperature", text=f"Temperatura GPU: [°C]", values=(gpu, est_cpu))

    def set_tempExt(self, temp):
        self.arbol.item("arduinoTemperature", text=f"Temperatura Exterior: [°C]", values=temp)