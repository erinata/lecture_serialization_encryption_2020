import pandas
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from sklearn.metrics import confusion_matrix
from sklearn.metrics import r2_score


dataset = pandas.read_csv("dataset.csv")

target = dataset.iloc[:,30].values
data = dataset.iloc[:,0:30].values

data_training, data_test, target_training, target_test = train_test_split(data, target, test_size = 0.25, random_state = 0)

machine = RandomForestClassifier(n_estimators=21, criterion="gini", max_depth=30, random_state =1)
machine.fit(data_training,target_training)
prediction = machine.predict(data_test)

print(r2_score(target_test,prediction))
print(confusion_matrix(target_test,prediction))

with open("serialized_machine.pickle", "wb") as file:
	pickle.dump(machine, file)
