import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "../data/climate_energy_cleaned.csv"
)

plt.figure(figsize=(10,6))
plt.plot(
    df["Year"],
    df["Global_CO2_Emissions_Mt"]
)
plt.title("Global CO₂ Emissions")
plt.xlabel("Year")
plt.ylabel("Mt CO₂")
plt.grid(True)
plt.show()
