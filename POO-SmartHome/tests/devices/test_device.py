import pytest
from devices.device import Device

@pytest.fixture
def device():
    return Device("Light", "Philips", "Hue123")

def test_turn_on(device):
    assert device.turn_on() == "Device turned on."
    assert device.get_state() is True

def test_turn_off(device):
    device.turn_on()
    assert device.turn_off() == "Device turned off."
    assert device.get_state() is False

def test_check_state(device):
    assert device.check_state() == "Off"
    device.turn_on()
    assert device.check_state() == "On"
