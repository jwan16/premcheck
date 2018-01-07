import pandas as pd
import os
import glob
def scan_folder(loc):
    extension = ['csv', 'xls', 'xlsx']
    allFiles = {ext: []for ext in extension}
    for path, dirs, files in os.walk(loc):
        for f in files:
            for ext in extension:
                if f.endswith('.{}'.format(ext)):
                    allFiles[ext].append(os.path.join(path, f))
    return allFiles

def find_header(df):
    header = ["Name", "DOB", "Gender"]

    # Check the first 10 rows. If a row exists in header[], it becomes the header
    for i in range(0, 10):
        if set(df.iloc[i]).intersection(header):
            df.columns = df.iloc[i]
            df = df[i+1:]
            return df
        else:
            pass
    print("No matched header")


def transform_date(df):
    date_patterns = ["%d%m%Y", "%Y-%m-%d", "%m-%d-%Y"]
    col_list = df.columns.values
    print(col_list)
    for col in col_list:
        for pattern in date_patterns:
            try:
                df[col] = pd.to_datetime(df[col], format=pattern)
            except:
                pass
    return df

def check_csv(dir):
    df = pd.read_csv(dir, sep=",", header=None)
    df = find_header(df)
    df = transform_date(df)
    if not os.path.exists(REFORMATED_DATA_DIR):
        os.mkdir(REFORMATED_DATA_DIR)
    df.to_csv(REFORMATED_DATA_DIR + "output.csv", index=False)
    print(df.dtypes)

def check_excel(dir):
    file = pd.ExcelFile(dir)
    sheet_names = file.sheet_names
    for sheet in sheet_names:
        df = file.parse(sheet)