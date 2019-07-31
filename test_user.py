from user import User, Me
from mock import Mock, patch


def test_user():
    user = User("test-user")
    assert not user.work()

def mock_work(*args, **kwargs):
    print("[mock]: OK")
    return False

def test_me():
    with patch('user.User') as mock_user:
        usr = mock_user.return_value
        usr.work.side_effect = mock_work
        me = Me("me")
        assert not me.work()
