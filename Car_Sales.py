import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import zipfile
import os 


zip_path = r"C:\Users\aliem\Downloads\car_sales.zip"
extract_path = r"C:\Users\aliem\Downloads\car_sales"

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

df = pd.read_csv(os.path.join(extract_path, "car_sales_data.csv"))

print(df.head())

avg_price=df.groupby("Manufacturer")["Price"].mean().sort_values(ascending=False)

plt.figure(figsize=(10,6))
avg_price.plot(kind="bar")
plt.title("Average Price by Manufacturer")
plt.ylabel("Average Price")
plt.xlabel("Manufacturer")
plt.show()