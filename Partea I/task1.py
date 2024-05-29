import pandas as pd

def task1():
	df = pd.read_csv("../train.csv", index_col=0)
	print(f"The number of columns is {len(df.columns)}")
	print("The data types are:")
	print(df.dtypes)
	print(df.isna().sum())
	print(f"The number of rows is {len(df)}")
	print(f"The number of duplicated rows is {df.duplicated().sum()}")
	return df