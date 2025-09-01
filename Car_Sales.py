import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import zipfile
import os 
import seaborn as sns

zip_path = r"C:\Users\aliem\Downloads\car_sales.zip"
extract_path = r"C:\Users\aliem\Downloads\car_sales"

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

df = pd.read_csv(os.path.join(extract_path, "car_sales_data.csv"))
df["KM"]=df["Mileage"]* 1.6


print(df.head)
avg_price=df.groupby("Manufacturer")["Price"].mean().sort_values(ascending=False)
avg_km=df.groupby("Manufacturer")["KM"].mean().sort_values(ascending=False)


#plt.figure(figsize=(10,6))
#avg_km.plot(kind="line")
#plt.title("Average KM by Manufacturer")
#plt.ylabel("Average KM")
#plt.xlabel("Manufacturer")
#plt.show()


plt.figure(figsize=(10,6))
sns.scatterplot(x="KM", y="Price", data=df, hue="Fuel type", palette="deep")
plt.title("Mileage vs Price (colored by Fuel Type)")
plt.xlabel("Kilometers")
plt.ylabel("Price")
plt.show()

