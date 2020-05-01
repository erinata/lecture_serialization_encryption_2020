from cryptography.fernet import Fernet
import pickle
import base64

password = b"PasswordPasswordPasswordPassword"
key = base64.urlsafe_b64encode(password)
print(key)

f = Fernet(key)

encrypted_object = b'gAAAAABerFnv9edbYn1xzJrVCny9lEHm4AMRZXBJyldo4BF1bkLB3XxkR1wG1FMcKx9AwbfReKT_78Lq4yg9u4H11bd-7HNank0gm4SMuhPQuasHpfy80S5b2q5uT6ArDGX-TbfZ3OWL'
print("Encrypted:")
print(encrypted_object)

decrypted_object = f.decrypt(encrypted_object)
print("Decrypted:")
print(decrypted_object)

deserialized_object = pickle.loads(decrypted_object)
print("deserialized:")
print(deserialized_object)