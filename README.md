# blockchain_simulation

# Blockchain Simulation

## Project Description
This project is a simple blockchain simulation implemented in Python. It demonstrates the core concepts of blockchain technology, including:
- Creating blocks with transactions.
- Linking blocks using cryptographic hashes.
- Implementing proof-of-work for mining.
- Validating the blockchain's integrity.
- Detecting tampering with the blockchain.

## Features
- **Block Structure:** Each block contains an index, timestamp, transactions, previous block hash, and a unique hash.
- **SHA-256 Hashing:** Ensures data integrity by linking blocks securely.
- **Proof-of-Work:** Adds computational difficulty to mining new blocks.
- **Tamper Detection:** Detects and invalidates tampered data in the blockchain.

## Prerequisites
Ensure you have Python installed on your system. You can check by running:
```sh
python --version
```
If Python is not installed, download it from [python.org](https://www.python.org/).

## Installation & Execution
1. **Clone the Repository**
```sh
git clone https://github.com/Shashankwagde/blockchain_simulation.git
cd <repository_folder>
```

2. **Run the Blockchain Simulation**
```sh
python blockchain_simulation.py
```

3. **Expected Output**
- The program will print the original blockchain.
- It will demonstrate tampering with a block.
- Finally, it will validate the blockchain and detect any inconsistencies.

## Code Structure
- `blockchain_simulation.py`: Main script that contains the blockchain and block classes.
- `README.md`: Instructions and documentation.

## Demonstration
The script runs automatically and prints:
1. The original blockchain.
2. A tampered version of the blockchain.
3. Validation check results.

## Future Enhancements
- Implement a peer-to-peer network simulation.
- Add a transaction pool with dynamic block creation.
- Implement digital signatures for transaction authenticity.

## Author
Developed as part of a blockchain coding challenge.

---
Feel free to reach out for any questions or improvements!

