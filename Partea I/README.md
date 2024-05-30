**Nume: Ariciu Toma**
**Grupă: 312CAb**

## Proiect PCLP3 - Titanic

### Descriere:

# Cerinta 1

* Am importat csv-ul cu ajutorul bibliotecii Pandas, iar apoi folosind functii din cadrul acesteia, am determinat:

* Numarul de coloane:
11

* Tipurile datelor din coloane:
Survived      int64
Pclass        int64
Name         object
Sex          object
Age         float64
SibSp         int64
Parch         int64
Ticket       object
Fare        float64
Cabin        object
Embarked     object

* Numarul de valori lipsa din fiecare coloana:
Survived      0
Pclass        0
Name          0
Sex           0
Age         177
SibSp         0
Parch         0
Ticket        0
Fare          0
Cabin       687
Embarked      2

* Numarul de linii:
891

* Numarul de linii duplicate:
0

# Cerinta 2

* Am folosit functia value_counts() pentru a calcula numarul aparitiilor din fiecare coloana ceruta - Survived, Pclass, Sex. Apoi, le-am pus in pie-charturi folosind biblioteca matplotlib.

![plot_survivors](Grafice/survivors.png)

![plot_classes](Grafice/classes.png)

![plot_sexes](Grafice/sexes.png)

# Cerinta 3

* Am luat pe rand fiecare coloana cu valori numerice, am eliminat valorile lipsa cu ajutorul functiei dropna(), iar apoi am generat histograma corespunzatoare:

![plot_Survived](Grafice/Survived.png)

![plot_Pclass](Grafice/Pclass.png)

![plot_Age](Grafice/Age.png)

![plot_SibSp](Grafice/SibSp.png)

![plot_Parch](Grafice/Parch.png)

![plot_Fare](Grafice/Fare.png)

# Cerinta 4

* Am verificat pentru fiecare coloana daca are valori lipsa si, daca da, cate sunt si ce procentaj reprezinta.

* Age:
Numarul total este 177
Procentajul este 19.865319865319865%
* Cabin:
Numarul total este 687
Procentajul este 77.10437710437711%
* Embarked:
Numarul total este 2
Procentajul este 0.22446689113355783%

* Am facut aceeasi verificare luand in parte cele doua clase date de coloana Survived: cei care au supravietuit si cei care nu.

#### Survived:

* Age:
Numarul total este 52
Procentajul este 15.204678362573098%
* Cabin:
Numarul total este 206
Procentajul este 60.23391812865497%
* Embarked:
Numarul total este 2
Procentajul este 0.5847953216374269%

#### Not survived:

* Age:
Numarul total este 125
Procentajul este 22.768670309653917%
* Cabin:
Numarul total este 481
Procentajul este 87.61384335154827%

# Cerinta 5

* Am adaugat o coloana in data frame, care sa ne spuna carui grup de varsta apartine un pasager, folosind functia apply. Folosind value_counts, am scos datele necesare pentru crearea unui pie-chart, care sa ilustreze distributia pasagerilor:

![plot_AgeGroups](Grafice/AgeGroups.png)

* De asemenea, am salvat noul data frame ca fisier csv.

# Cerinta 6

* Folosind coloana creata la cerinta anterioara, am filtrat tabelul initial pentru a ramane doar cu barbatii, pe care i-am impartit dupa grupele de varsta si le-am calculat rata de supravietuire, pe care am pus-o in urmatorul grafic:

![plot_Male_survival_rate](Grafice/Male_survival_rate.png)

# Cerinta 7

* Am filtrat din data frame-ul mare doar copiii (cu varsta sub 18 ani) si adultii (varsta peste 18 ani) si am calculat rata de supravietuire pentru ambele categorii:

![plot_Children&Adults_survival_rates](Grafice/Children%26Adults_survival_rates.png)

* Am omis pasagerii a caror varsta este necunoscuta. De asemenea, am salvat cele doua data frame-uri create ca fisiere csv.

# Cerinta 8

* Am impartit data frame-ul dupa cele doua clase date de coloana Survived. Folosind functia fillna(), am inlocuit valorile lipsa cu media celorlalte valori, daca coloana continea date numerice, sau cu cea mai frecventa intrare, daca nu. Apoi, am inlocuit valorile calculate pe clase in data frame-ul original.

* Am salvat fisierul in format csv (filled.csv).