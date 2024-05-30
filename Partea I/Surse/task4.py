def print_percentage(df):
	for column in df.columns:
		if (df[column].isna().sum() > 0):
			empty = df[column].isna().sum()
			total = len(df[column])
			print(f"{column}:")
			print(f"Total number is {empty}")
			percentage = empty / total * 100
			print(f"The percentage is {percentage}%")
	pass

def task4(df):
	print("Total:")
	print_percentage(df)
	survived = df[df['Survived'] == 1]
	not_survived = df[df['Survived'] == 0]
	print("Survived:")
	print_percentage(survived)
	df.to_csv("../Date/survived.csv")
	print("Not survived:")
	print_percentage(not_survived)
	df.to_csv("../Date/not_survived.csv")
	pass
