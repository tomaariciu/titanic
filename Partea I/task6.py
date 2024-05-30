import matplotlib.pyplot as plt

def task6(df):
	df = df[df['Sex'] == "male"]
	age_groups = df['AgeGroup'].value_counts().sort_index()
	labels = []
	percentages = []
	for AgeGroup in age_groups.index:
		curr_df = df[df['AgeGroup'] == AgeGroup]
		total = len(curr_df)
		survived = curr_df['Survived'].sum()
		print(f"Number of male survivors for {AgeGroup} is {survived}")
		labels.append(AgeGroup)
		percentages.append(survived / total * 100)
	plt.bar(labels, percentages)
	plt.savefig("Male_survival_rate.png")
	pass
