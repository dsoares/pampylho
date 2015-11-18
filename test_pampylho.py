import getpass

import pytest

import pampylho


def test_pam_error_noargs():
    e = pampylho.PAMError()
    s = str(e)
    r = repr(e)
    assert 'Unknown' in s
    assert 'Unknown' in r


def test_pam_error_errno():
    en = 2
    e = pampylho.PAMError(errno=en)
    assert str(en) in str(e)
    assert 'Unknown' not in str(e)


def test_auth_nouser():
    with pytest.raises(pampylho.PAMError) as exc_info:
        pampylho.authenticate('userdoesntexist', 'wrongpassword')
    
    e = exc_info.value
    assert 'Unknown' not in str(e)


def test_auth_badpassword():
    with pytest.raises(pampylho.PAMError) as exc_info:
        pampylho.authenticate(getpass.getuser(), 'wrongpassword')

    e = exc_info.value
    assert 'Unknown' not in str(e)


def test_all():
    for name in pampylho.__all__:
        getattr(pampylho, name)
