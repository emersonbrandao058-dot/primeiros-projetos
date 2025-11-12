# primeiro grande código
# autor: Emerson Brandão
# data: 12/11/2025

import psutil  # pegar dados do sistema
import time    # pausar execução
from datetime import datetime

CPU_LIMITE = 80
MEMORIA_LIMITE = 80
INTERVALO = 2

print("=== MONITOR DE SISTEMA ===")
print("Pressione Ctrl + C para encerrar.\n")

try:
    while True:
        cpu = psutil.cpu_percent(interval=0.5)  # percentual total da CPU
        memoria = psutil.virtual_memory().percent
        tempo = datetime.now().strftime("%H:%M:%S")

        print(f"[{tempo}] CPU: {cpu:.1f}% | Memória: {memoria:.1f}%")

        if cpu > CPU_LIMITE or memoria > MEMORIA_LIMITE:
            print("⚠️  Alerta: recurso acima do limite!")

        time.sleep(INTERVALO)

except KeyboardInterrupt:
    print("\n=== Monitor finalizado ===")
