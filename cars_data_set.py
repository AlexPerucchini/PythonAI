#import kagglehub
import pandas as pd
import matplotlib.pyplot as plt

# Download latest version
#path = kagglehub.dataset_download("nehalbirla/vehicle-dataset-from-cardekho")
# /Users/alexp/.cache/kagglehub/datasets/nehalbirla/vehicle-dataset-from-cardekho/versions/4
# print("Path to dataset files:", path)

df = pd.read_csv('/Users/alexp/.cache/kagglehub/datasets/nehalbirla/vehicle-dataset-from-cardekho/versions/4/car_data.csv')
#print(df)

print(df[df["Selling_Price"]>= 18.00])

filtered_data = df[df["Year"]==2015]
print(filtered_data["Selling_Price"].median())

plt.figure(figsize=(8, 4)) # Adjust the figure size if needed!
plt.bar(df['Car_Name'], df['Selling_Price'])  # Create bars from "Selling Price" column
plt.xlabel("Car Name") # Label for the x-axis
plt.ylabel("Selling Price") # Label for the y-axis
plt.title("Distribution of Selling Prices by Car Model")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()  # Ensure good spacing and prevent overlap!


plt.show()
