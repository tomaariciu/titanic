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
