#!/usr/bin/env python3
import pytest
from wallet.wallet import Wallet, InsufficientAmount


@pytest.fixture(autouse=True)
def debug(request):
    print(f"Starting {request} ")


@pytest.fixture
def empty_wallet():
    """Returns a Wallet instance with a zero balance """
    return Wallet()


@pytest.fixture
def wallet():
    """Returns a Wallet instance with a balance of 20"""
    return Wallet(20)


def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0


def test_setting_initial_amount(wallet):
    assert wallet.balance == 20


def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100


@pytest.mark.parametrize('money', [2, 3, 5, 7])
def test_wallet_spend_cash(wallet, money):
    wallet.spend_cash(money)
    assert wallet.balance == (20 - money)


def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)
