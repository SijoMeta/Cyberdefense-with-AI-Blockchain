from web3 import Web3

# Connect to blockchain
infura_url = "https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(infura_url))

contract_address = "0xYourContractAddress"
abi = [  # Paste the ABI from Remix here
    {
        "constant": False,
        "inputs": [{"name": "_attackType", "type": "string"}],
        "name": "addThreat",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

contract = web3.eth.contract(address=contract_address, abi=abi)

def store_threat_in_blockchain(attack_type):
    tx = contract.functions.addThreat(attack_type).build_transaction({
        'from': web3.eth.accounts[0],
        'gas': 100000,
        'gasPrice': web3.toWei('10', 'gwei'),
        'nonce': web3.eth.getTransactionCount(web3.eth.accounts[0])
    })
    signed_tx = web3.eth.account.sign_transaction(tx, private_key="YOUR_PRIVATE_KEY")
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print("Threat logged in blockchain. Tx Hash:", web3.toHex(tx_hash))
