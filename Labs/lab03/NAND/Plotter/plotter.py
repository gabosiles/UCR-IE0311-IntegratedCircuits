import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo combinado
data = pd.read_csv("NAND_Curves.txt", delim_whitespace=True)

# Graficar todas las señales
plt.figure(figsize=(10, 6))
plt.plot(data['VIN'], data['V(vout)'], label='Vout vs Va', color='red')
plt.plot(data['VIN'], data['V(vout_1)'], label='Vout vs Vb', color='blue')
plt.plot(data['VIN'], data['V(vout_2)'], label='Vout vs Vin', color='green')

# Estética del gráfico
plt.title("Curvas características de la NAND2",fontsize=18)
plt.xlabel("Va-Vb-Vin [V]", fontsize=14)
plt.ylabel("Vout [V]",fontsize=14)
plt.grid(True)
plt.legend(fontsize=13,loc='upper right')
plt.tight_layout()
plt.show()