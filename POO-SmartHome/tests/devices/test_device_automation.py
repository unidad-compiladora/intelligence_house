import pytest
from devices.device_automation import DeviceAutomation

@pytest.fixture
def automation():
    return DeviceAutomation()

def test_automate_ac(automation):
    assert automation.automate_ac(30) == "AC turned on."
    assert automation.automate_ac(20) == "AC remains off."

def test_automate_light(automation):
    assert automation.automate_light(True) == "Light turned on."
    assert automation.automate_light(False) == "Light turned off."
