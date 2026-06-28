import hashlib
def hashTrasnaction(transaction):
    transaction_array = [transaction.sender, transaction.reciever, transaction.value, transaction.timestamp]
    byte_input = bytearray(transaction_array, "utf-8")
    return hashlib.sha256(byte_input).hexdigest() 

def sign_transaction(hash):
    
    
    
    