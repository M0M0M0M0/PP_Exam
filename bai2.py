import pandas as pd

data = {
    "id":       [1, 2, 3, 4, 5],
    "name":     ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphone"],
    "price":    [1500, 25, 45, 320, 85],
    "quantity": [10, 50, 30, 15, 25],
}

df=pd.DataFrame(data)

df.to_csv("data.csv",index=False)
print("Da luu ra csv")

df2=pd.read_csv("data.csv")
print(df2.to_string())

print(f"\nCac san pham co gia lon hon 100 la:")
print(df[df["price"] > 100].to_string(index=False))

df["total"] = df["price"] * df["quantity"]
total_value = df["total"].sum()
print(f"Tong gia tri cac san pham trong kho la {total_value} ")
df.to_csv("data.csv",index=False)



