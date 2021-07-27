from engine import Cypher

cryptanalyst = Cypher()
print(cryptanalyst)
# print(cryptanalyst.__engines__())
result = cryptanalyst.encrypt(message='hello world', engine='multiplicative', key=16196516)
print(result)
print(cryptanalyst.decrypt(message=result['encrypted_message'], engine=result['engine'], key=result['key']))