import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(df, column):
	plt.hist(df[column].dropna())
	plt.xlabel(f"{column} values")
	plt.ylabel(f"Frequency")
	plt.title(f"{column} histogram")
	plt.savefig(f"../Grafice/{column}.png")
	plt.close()
	pass

def task3(df):
	for column in df.select_dtypes(include=np.number).columns:
		plot_histogram(df, column)
	pass
