import pandas as pd
import matplotlib.pyplot as plt


# Cargar el archivo (usá el nombre que hayas guardado)
df = pd.read_csv("INVERSORES_C17530_sim.txt", delim_whitespace=True)
# Graficar las curvas de los inversores
plt.figure(figsize=(8, 5))
plt.plot(df["V(vin)"], df["V(vout_inv_10_10)"], label="Inversor 10/10", color="red")
plt.plot(df["V(vin)"], df["V(vout_inv_15_05)"], label="Inversor 15/05", color="orange")
plt.plot(df["V(vin)"], df["V(vout_inv_20_10)"], label="Inversor 20/10", color="blue")

# Personalización de la gráfica
plt.title("Curvas Vout vs Vin Inversores CMOS")
plt.xlabel("Vin (V)")
plt.ylabel("Vout (V)")
plt.grid(True)
plt.legend(fontsize=12, loc='center left', bbox_to_anchor=(0.75, 0.5))
plt.tight_layout()

# Mostrar en pantalla
plt.show()