import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo con delimitación por espacios (ajustá el nombre si es diferente)
df = pd.read_csv("INV_DELAY_C17530_sim.txt", delim_whitespace=True)



# Gráfica 1: Vin vs tiempo
plt.figure(figsize=(8, 4))
plt.plot(df["time"], df["V(vin)"], color="green")
plt.title("Vin en función del tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Vin (V)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfica 2: Vout vs tiempo
plt.figure(figsize=(8, 4))
plt.plot(df["time"], df["V(vout)"], color="blue")
plt.title("Vout en función del tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Vout (V)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Graficar Vin y Vout en función del tiempo
plt.figure(figsize=(8, 5))
plt.plot(df["time"], df["V(vin)"], label="Vin(t)", color="green")
plt.plot(df["time"], df["V(vout)"], label="Vout(t)", color="blue")

# Personalización de la gráfica
plt.title("Vin y Vout en función del tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.grid(True)
plt.legend(fontsize=12)
plt.tight_layout()

# Mostrar en pantalla
plt.show()
