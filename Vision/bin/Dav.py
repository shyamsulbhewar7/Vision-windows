import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
def datanalysis(filename):
    df = pd.read_csv(filename)

    feature = list(df.columns)

    length = len(feature)

    dependent = feature[-1]

    plt.figure(figsize = (15,15))
    for i in enumerate(feature):
        print(plt.subplot(length, 1, i[0]+1))##
        print(sns.countplot(i[1], hue = dependent, data = df))##
        print(plt.xticks(rotation = 45))

    x = df.iloc[:,0:length-2].values

    y = df.iloc[:,length-1].values

    labelencoder_y = LabelEncoder()
    y = labelencoder_y.fit_transform(y)

    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2)

    logmodel = LogisticRegression()
    logmodel.fit(x_train,y_train)

    y_pred = logmodel.predict(x_test)

    
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    classifier_knn = KNeighborsClassifier(n_neighbors=5, metric = 'minkowski', p=2)
    classifier_knn.fit(x_train, y_train)

    y_pred = classifier_knn.predict(x_test)
    cm = confusion_matrix(y_test, y_pred)
    print(cm)

datanalysis("iris_data.csv")