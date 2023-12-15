import argparse
from web3 import Web3
import hashlib

web3 = Web3()

def generate_wallet(seed):
    hashed_seed = hashlib.sha256(seed.encode()).hexdigest()
    address = web3.eth.account.from_key(hashed_seed).address
    return str(hashed_seed), address

def generate_wallet_from_file(filename):
    try:
        with open(filename, 'r') as file:
            seed = file.read().strip()
            return generate_wallet(seed)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Ethereum wallet from any text or file.')
    parser.add_argument('-f', '--file', help='Read seed from file')

    args = parser.parse_args()

    if args.file:
        private_key, address = generate_wallet_from_file(args.file)
    else:
        input_string = input("Enter a string to generate wallet: ")
        private_key, address = generate_wallet(input_string)

    print(f"\nPrivate Key: {private_key}")
    print(f"Address: {address}")
