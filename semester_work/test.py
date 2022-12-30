import pytest
import main


def test_password_normal():
    assert main.passworld_check("qwaszx12RT") == True


def test_password_long():
    with pytest.raises(main.PasswordError):
        main.passworld_check("qw")


def test_password_no_number():
    with pytest.raises(main.PasswordError):
        main.passworld_check("qwaszxRTb")


def test_password_simple():
    assert main.pass_is_valid("12RTqweqweqwe") == False


def test_password_uppercase():
    with pytest.raises(main.PasswordError):
        main.passworld_check("12RTTBOLTG6")


def test_password_capital():
    with pytest.raises(main.PasswordError):
        main.passworld_check("12qwaszxbnt")