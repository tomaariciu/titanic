import pandas as pd
pd.options.mode.chained_assignment = None

def task8(df):
	survived = df[df['Survived'] == 1]
	not_survived = df[df['Survived'] == 0]
	for column in df.columns:
		if (df[column].dtype.kind in 'iufc'):
			survived_mean = survived[column].mean()
			not_survived_mean = not_survived[column].mean()
			survived[column].fillna(survived_mean, inplace = True)
			not_survived[column].fillna(not_survived_mean, inplace = True)
		else:
			survived_most_frequent = survived[column].value_counts().idxmax()
			not_survived_most_frequent = not_survived[column].value_counts().idxmax()
			survived[column].fillna(survived_most_frequent, inplace = True)
			not_survived[column].fillna(not_survived_most_frequent, inplace = True)
	
	df.fillna(survived, inplace = True)
	df.fillna(not_survived, inplace = True)
	df.to_csv("../Date/filled.csv")
	pass