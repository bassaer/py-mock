from user import User, Me
from mock import Mock, patch


def test_user():
    user = User("test-user")
    assert not user.work()

def mock_work(*args, **kwargs):
    print("[mock]: OK")
    return False

def test_me():
    with patch('user.User.work', side_effect=mock_work) as mocked_work:
        me = Me("me")
        assert not me.work()
        mocked_work.assert_called_with(cheat=True, done=False)
