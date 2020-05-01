import pickle

with open("serialized_file.pickle", "rb") as file:
	deserialized_object = pickle.load(file)


print(deserialized_object)

