// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CyberDefense {
    struct Threat {
        uint id;
        string attackType;
        uint timestamp;
    }

    Threat[] public threats;
    uint public threatCount = 0;

    function addThreat(string memory _attackType) public {
        threats.push(Threat(threatCount, _attackType, block.timestamp));
        threatCount++;
    }

    function getThreats() public view returns (Threat[] memory) {
        return threats;
    }
}
