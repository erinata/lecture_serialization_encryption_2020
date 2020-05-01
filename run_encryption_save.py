from cryptography.fernet import Fernet

import pickle
import base64

# key =Fernet.generate_key()
password = b"PasswordPasswordPasswordPassword"
key = base64.urlsafe_b64encode(password)
print(key)
f = Fernet(key)


original_object = "Baby Shark do do do do do doh"
print("Original:")
print(original_object)

serialized_object = pickle.dumps(original_object)
print("Serialized:")
print(serialized_object)

encrypted_object = f.encrypt(serialized_object)
print("Encrypted:")
print(encrypted_object)

