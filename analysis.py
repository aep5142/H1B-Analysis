import pandas as pd

df = pd.read_csv("data/Employer Information.csv")

print(df.dtypes)

def treatment_data():
    columns_to_int = ["Petitioner Zip Code", "Initial Approval",
                      "Continuing Approval"]
    for column in columns_to_int:
        df[column] = pd.to_numeric(df[column], errors='coerce')

treatment_data()
