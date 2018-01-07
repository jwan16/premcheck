import pandas as pd
header = ["Name", "DOB", "Gender"]
file = pd.ExcelFile("Workbook2.xlsx")

# for i in range(0,4):
#     df = file.parse(0, skiprows=i)
#     if set(df.columns.values).intersection(header):
#         print(i)
#         print("Yo")
#         break

# print(df.head())

