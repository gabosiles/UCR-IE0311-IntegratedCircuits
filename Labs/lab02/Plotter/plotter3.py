import pandas as pd
import matplotlib.pyplot as plt


# Cargar el archivo (usá el nombre que hayas guardado)
df = pd.read_csv("INV_power_C17530_sim.txt", delim_whitespace=True)

plt.figure(figsize=(8, 4))
plt.plot(df["time"], df["V(vdd)*Ix(xinv_20_1@0:vdd)"], color="red", label="Pdinámica")
plt.title("Potencia Dinámica en función del tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Potencia Dinámica (W)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
