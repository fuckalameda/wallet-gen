from web3 import Web3
import hashlib

web3 = Web3()

def generate_wallet(seed):
    hashed_seed = hashlib.sha256(seed.encode()).hexdigest()
    address = web3.eth.account.from_key(hashed_seed).address
    return str(hashed_seed), address

if __name__ == "__main__":
    input_string = input("Enter a string to generate wallet: ")
    private_key, address = generate_wallet(input_string)

    print(f"\nPrivate Key: {private_key}")
    print(f"Address: {address}")
