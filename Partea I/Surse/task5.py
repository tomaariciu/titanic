import matplotlib.pyplot as plt

def get_age_group(age):
	if (age <= 20):
		return "0 - 20"
	if (21 <= age and age <= 40):
		return "21 - 40"
	if (41 <= age and age <= 60):
		return "41 - 60"
	if (age > 60):
		return "60+"

def task5(df):
	df['AgeGroup'] = df.apply(lambda x: get_age_group(x['Age']), axis = 1)
	age_groups = df['AgeGroup'].value_counts()
	labels = age_groups.index
	values = age_groups.values
	plt.pie(values, labels=labels)
	plt.savefig("../Grafice/AgeGroups.png")
	plt.close()
	df.to_csv("../Date/age_groups.csv")
	return df
