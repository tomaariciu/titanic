import matplotlib.pyplot as plt

def task7(df):
	children = df[df['Age'] < 18]
	children_survival_rate = children['Survived'].sum() / len(children) * 100
	df.to_csv("../Date/children.csv")
	adults = df[df['Age'] >= 18]
	adults_survival_rate = adults['Survived'].sum() / len(adults) * 100
	df.to_csv("../Date/adults.csv")
	values = [children_survival_rate, adults_survival_rate]
	labels = ["Children", "Adults"]
	plt.bar(labels, values)
	plt.title("Survival rates for children and adults")
	plt.savefig("../Grafice/Children&Adults_survival_rates.png")
	plt.close()
	pass