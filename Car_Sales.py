import pandas as pd
import matplotlib as mpl
import numpy as np
import zipfile

zip_path = r"C:\Users\aliem\Downloads\car_sales.zip"
extract_path = r"C:\Users\aliem\Downloads\car_sales"

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print("Dosyalar buraya açıldı:", extract_path)