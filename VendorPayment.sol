// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract VendorPayment {
    struct Payment {
        string vendor;
        uint amount; // amount in cents
        string txId;
        uint timestamp;
    }
    
    Payment[] public payments;
    address public owner;
    
    event PaymentRecorded(string vendor, uint amount, string txId, uint timestamp);
    
    constructor() {
        owner = msg.sender;
    }
    
    function payVendor(string memory vendor, uint amount, string memory txId) public returns (bool) {
        // Add validations as needed (e.g., access control)
        Payment memory newPayment = Payment({
            vendor: vendor,
            amount: amount,
            txId: txId,
            timestamp: block.timestamp
        });
        payments.push(newPayment);
        emit PaymentRecorded(vendor, amount, txId, block.timestamp);
        return true;
    }
    
    function getPaymentCount() public view returns (uint) {
        return payments.length;
    }
}
