from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import pandas as pd
import graphviz

df = pd.read_csv("titanic_2.csv")

clf = DecisionTreeClassifier(max_depth=4, min_samples_leaf=5)
X = df[df.columns[1:]]
y = df[df.columns[0]]
clf.fit(X, y)

feature_names = df.columns[1:]

dot_data = tree.export_graphviz(clf, out_file=None, feature_names=feature_names)
graph = graphviz.Source(dot_data)
graph.render("Titanic")
graph.view()
