import pytest
from users.standard_user import StandardUser

@pytest.fixture
def standard_user():
    return StandardUser("Pedro", "López", "pedro@example.com", "pass456")

def test_inheritance(standard_user):
    assert standard_user.get_is_admin() is False

def test_view_device(standard_user):
    result = standard_user.view_device("Smart Light")
    assert "Smart Light" in result

def test_run_automation(standard_user):
    result = standard_user.run_automation("Energy Saving")
    assert "Energy Saving" in result
