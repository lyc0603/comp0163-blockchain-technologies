// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

contract MyToken {
  // total supply of token
  uint256 constant supply = 1000000;

  // event to be emitted on transfer
  event Transfer(address indexed _from, address indexed _to, uint256 _value);

  // event to be emitted on approval
  event Approval(
    address indexed _owner,
    address indexed _spender,
    uint256 _value
  );

  // TODO: create mapping for balances

  // TODO: create mapping for allowances

  constructor() {
    // TODO: set sender's balance to total supply
  }

  function totalSupply() public pure returns (uint256) {
    // TODO: return total supply
  }

  function balanceOf(address _owner) public view returns (uint256) {
    // TODO: return the balance of _owner
  }

  function transfer(address _to, uint256 _value) public returns (bool) {
    // TODO: transfer `_value` tokens from sender to `_to`
    // NOTE: sender needs to have enough tokens
  }

  function transferFrom(
    address _from,
    address _to,
    uint256 _value
  ) public returns (bool) {
    // TODO: transfer `_value` tokens from `_from` to `_to`
    // NOTE: `_from` needs to have enough tokens and to have allowed sender to spend on his behalf
  }

  function approve(address _spender, uint256 _value) public returns (bool) {
    // TODO: allow `_spender` to spend `_value` on sender's behalf
    // NOTE: if an allowance already exists, it should be overwritten
  }

  function allowance(address _owner, address _spender)
    public
    view
    returns (uint256 remaining)
  {
    // TODO: return how much `_spender` is allowed to spend on behalf of `_owner`
  }
}
