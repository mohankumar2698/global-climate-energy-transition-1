import pandas as pd

df = pd.read_csv(
    "../data/climate_energy_cleaned.csv"
)

print(df.describe())

print(df.corr(numeric_only=True))
