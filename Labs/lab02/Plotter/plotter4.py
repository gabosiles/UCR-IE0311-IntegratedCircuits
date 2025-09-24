import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo
df = pd.read_csv("INV_Iinv_Vout_C17530_sim.txt", delim_whitespace=True)

# Crear figura y eje principal (para Vout)
fig, ax1 = plt.subplots(figsize=(8, 5))

# Primer eje Y: Vout
ax1.plot(df["time"], df["V(vout)"], color='blue', label="Vout(t)")
ax1.set_xlabel("Tiempo (s)")
ax1.set_ylabel("Vout (V)", color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.grid(True)

ax2 = ax1.twinx()
ax2.plot(df["time"], df["Ix(xinv_20_1@0:y_c17530)"] * 1e6, color='orange', label="I_INV(t) [µA]")
ax2.set_ylabel("Corriente I_INV (µA)", color='orange')
ax2.tick_params(axis='y', labelcolor='orange')
# Título general
plt.title("Vout y Corriente Inversor en función del tiempo")
plt.tight_layout()
plt.show()
