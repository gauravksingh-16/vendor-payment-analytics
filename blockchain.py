# blockchain.py
import os
import json
from web3 import Web3

# Connect to an Ethereum node (local or via an endpoint like Infura)
WEB3_PROVIDER = os.getenv("WEB3_PROVIDER", "http://127.0.0.1:8545")
w3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER))

# Contract address and ABI (assumed to be deployed already)
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS", "0xYourContractAddressHere")
with open("VendorPaymentABI.json", "r") as f:
    contract_abi = json.load(f)

contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

def record_payment_transaction(vendor: str, amount: float, tx_id: str):
    """
    Interact with the smart contract to record a vendor payment.
    """
    # Select an account (ensure proper key management in production)
    account = w3.eth.accounts[0]
    # Build transaction (amount converted to cents for this example)
    tx = contract.functions.payVendor(vendor, int(amount * 100), tx_id).buildTransaction({
        'from': account,
        'nonce': w3.eth.get_transaction_count(account),
        'gas': 3000000,
        'gasPrice': w3.toWei('20', 'gwei')
    })
    private_key = os.getenv("PRIVATE_KEY")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return receipt
