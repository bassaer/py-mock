from user import User, Me
from mock import Mock, patch


def test_user():
    user = User("test-user")
    assert not user.work()


def mock_work(*args, **kwargs):
    print("[mock]: OK")
    return False


@patch('user.User.work', side_effect=mock_work)
def test_me(mocked_func):
        me = Me("me")
        assert not me.work()
        mocked_func.assert_called_with(cheat=True, done=False)
