import pandas as pd
import matplotlib.pyplot as plt

title_to_gender = {
	"Mr" : "male",
	"Miss" : "female",
	"Mrs" : "female",
	"Master" : "male",
	"Dr" : "male",
	"Rev" : "male",
	"Mlle" : "female",
	"Major" : "male",
	"Col" : "male",
	"the Countess" : "female",
	"Capt" : "male",
	"Ms" : "female",
	"Sir" : "male",
	"Lady" : "female",
	"Mme" : "female",
	"Don" : "male",
	"Jonkheer" : "male"
}

def task9(df):
	df['Title'] = df.apply(lambda x: x['Name'].split(',')[1].split('.')[0].strip(), axis = 1)
	titles = df['Title'].value_counts().sort_index()
	labels = titles.index
	values = titles.values
	plt.bar(labels, values)
	plt.xticks(rotation = 90)
	plt.savefig("../Grafice/Titles.png")
	plt.close()
	df['Title gender'] = df.apply(lambda x: title_to_gender[x['Title']], axis = 1)
	differences = len(df[df['Sex'] != df['Title gender']])
	print(differences)
	df.to_csv("../Date/titles.csv")
	pass