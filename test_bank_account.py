import pytest
from bankAccount import BankAccount

#testing __init__
def test_default_balance_is_zero():
    account = BankAccount()
    assert account.balance == 0

def test_balance_less_than_zero():
    with pytest.raises(ValueError):
        BankAccount(-5)
    
def test_custom_balance():
    account = BankAccount(100)
    assert account.balance == 100

def test_transaction_history_starts_empty():
    account = BankAccount()
    assert account.transaction_history == []

#testing deposit

def test_deposit_greater_than_zero():
    account = BankAccount()
    account.balance = account.deposit(100)
    assert account.balance == 100
    
def test_deposit_equal_to_zero():
    account = BankAccount()
    with pytest.raises(ValueError):
        account.deposit(0)

def test_deposit_less_than_zero():
    account = BankAccount()
    with pytest.raises(ValueError):
        account.deposit(-1)

#testing withdraw

def test_withdraw_less_than_zero():
    account = BankAccount(100)
    with pytest.raises(ValueError):
        account.withdraw(-1)

def test_withdraw_equal_to_zero():
    account = BankAccount(100)
    with pytest.raises(ValueError):
        account.withdraw(0)

def test_withdraw_greater_than_zero():
    account = BankAccount(100)
    account.balance = account.withdraw(50)
    assert account.balance == 50

def test_withdraw_greater_than_balance():
    account = BankAccount(100)
    with pytest.raises(ValueError):
        account.withdraw(150)

#test getting balance

def test_get_balance_returns_correct_balance():
    account = BankAccount(100)
    assert account.get_balance() == 100

def test_get_balance_after_deposit():
    account = BankAccount(100)
    account.deposit(50)
    assert account.get_balance() == 150

def test_get_balance_after_withdrawal():
    account = BankAccount(100)
    account.withdraw(30)
    assert account.get_balance() == 70

#test transfer money 

def test_transfer_decreases_sender_balance():
    sender = BankAccount(100)
    receiver = BankAccount(0)
    sender.transfer(50, receiver)
    assert sender.get_balance() == 50

def test_transfer_increases_receiver_balance():
    sender = BankAccount(100)
    receiver = BankAccount(0)
    sender.transfer(50, receiver)
    assert receiver.get_balance() == 50

def test_transfer_exact_balance():
    sender = BankAccount(100)
    receiver = BankAccount(0)
    sender.transfer(100, receiver)
    assert sender.get_balance() == 0
    assert receiver.get_balance() == 100

def test_transfer_exceeding_balance_raises_error():
    sender = BankAccount(100)
    receiver = BankAccount(0)
    with pytest.raises(ValueError):
        sender.transfer(200, receiver)

def test_transfer_updates_both_transaction_histories():
    sender = BankAccount(100)
    receiver = BankAccount(0)
    sender.transfer(50, receiver)
    assert "Withdrew: 50" in sender.transaction_history
    assert "Deposited: 50" in receiver.transaction_history
    
