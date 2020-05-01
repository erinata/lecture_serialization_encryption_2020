import pickle

# original_object = "Baby Shark do do do do do do doh"
original_object = list(range(100))

print(original_object)

with open("serialized_file.pickle", "wb") as file:
	pickle.dump(original_object, file)


