import pandas as pd

df = pd.read_csv(
    "../data/Global_Climate_Energy_Transition_Project_2000_2026.csv"
)

print(df.info())

df.drop_duplicates(inplace=True)

df.fillna(method="ffill", inplace=True)

df.to_csv(
    "../data/climate_energy_cleaned.csv",
    index=False
)

print("Cleaning Complete")
