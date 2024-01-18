import pandas as pd

df = pd.read_csv("filtered_data.csv")

strengthfactor_threshold = 110000
filtered_sku_numbers = [row["SKU_number"] for _, row in df.iterrows() if float(row["StrengthFactor"]) > strengthfactor_threshold]

print(filtered_sku_numbers)
