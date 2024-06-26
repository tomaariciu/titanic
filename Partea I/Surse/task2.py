import matplotlib.pyplot as plt

def plot_survivors(df):
	total = len(df)
	survived = df['Survived'].sum()
	percentage = survived / total * 100
	labels = ['Survived', 'Lost']
	values = [percentage, 100 - percentage]
	plt.pie(values, labels=labels, autopct='%1.0f%%')
	plt.title("Survived vs Lost")
	plt.savefig("../Grafice/survivors.png")
	plt.close()
	pass

def plot_classes(df):
	classes = df['Pclass'].value_counts().sort_index()
	labels = classes.index
	values = classes.values
	plt.pie(values, labels=labels, autopct='%1.0f%%')
	plt.title("Classes distribution")
	plt.savefig("../Grafice/classes.png")
	plt.close()
	pass

def plot_sexes(df):
	sexes = df['Sex'].value_counts().sort_index()
	labels = sexes.index
	values = sexes.values
	plt.pie(values, labels=labels, autopct='%1.0f%%')
	plt.title("Sexes distribution")
	plt.savefig("../Grafice/sexes.png")
	plt.close()
	pass

def task2(df):
	plot_survivors(df)
	plot_classes(df)
	plot_sexes(df)
	pass
