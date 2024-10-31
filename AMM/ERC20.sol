// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

// Import the IERC20 interface and inherit from it
import "./IERC20.sol";

contract ERC20 is IERC20 {
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(
        address indexed owner, address indexed spender, uint256 value
    );

    uint256 public totalSupply;
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;
    string public name;
    string public symbol;
    uint8 public decimals;

    constructor(string memory _name, string memory _symbol, uint8 _decimals) {
        name = _name;
        symbol = _symbol;
        // In solidity, we do not have a floating point number.
        // To represent a decimal number, we need to store it as an integer.
        // In ERC20 tokens, decimals represent the smallest unit in which the token can be divided. 
        // If the decimals is 18, we can use 0.5 * 10^18 to represent 0.5 tokens, which is 500000000000000000.
        decimals = _decimals;
    }

    function transfer(address recipient, uint256 amount)
        external
        returns (bool)
    {
        balanceOf[msg.sender] -= amount;
        balanceOf[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    function approve(address spender, uint256 amount) external returns (bool) {
        allowance[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount)
        external
        returns (bool)
    {
        allowance[sender][msg.sender] -= amount;
        balanceOf[sender] -= amount;
        balanceOf[recipient] += amount;
        emit Transfer(sender, recipient, amount);
        return true;
    }

    function _mint(address to, uint256 amount) internal {
        // TODO: Mint the amount of tokens to the recipient
        // Hint: When emitting the Transfer event, the `from` 
        // address should be the address(0), which is the
        // conventional address used to represent minted tokens
        // 0x0000000000000000000000000000000000000000
    }

    function _burn(address from, uint256 amount) internal {
        // TODO: Burn the amount of tokens from the address
        // Hint: When emitting the Transfer event, the `to`
        // address should be the address(0), which is the
        // conventional address used to represent burned tokens
        // 0x0000000000000000000000000000000000000000
    }

    function mint(address to, uint256 amount) external {
        _mint(to, amount);
    }

    function burn(address from, uint256 amount) external {
        _burn(from, amount);
    }
}