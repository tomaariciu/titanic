import matplotlib.pyplot as plt
import seaborn as sns

def is_alone(sibling_count, parch_count):
	if (sibling_count != 0):
		return 0
	if (parch_count != 0):
		return 0
	return 1

def task10(df):
	df['Alone'] = df.apply(lambda x: is_alone(x['SibSp'], x['Parch']), axis = 1)
	alone_df = df[df['Alone'] == 1]
	plt.hist(alone_df['Survived'])
	plt.xlabel("Survived")
	plt.ylabel("Number of passengers")
	plt.title("Survived vs Lost for alone passengers")
	plt.savefig("../Grafice/Alone_survival_rate.png")
	plt.close()

	df = df.head(100)
	sns.catplot(data=df, x = 'Pclass', y = 'Fare', hue = 'Survived', kind = 'swarm', size = 2.5)
	plt.title("Relationship between class, fare and survival", y=0.96)
	plt.savefig("../Grafice/Class-Fare-Survival_relationship.png")
	plt.close()
	pass