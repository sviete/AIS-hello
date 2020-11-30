"""ais hello sensor"""
from homeassistant.const import ENERGY_KILO_WATT_HOUR
from homeassistant.helpers.entity import Entity
from time import time
import logging

_LOGGER = logging.getLogger(__name__)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Konfiguracja za pomocą yaml - sposób przestarzały"""
    return


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Konfiguracja za pomcą przepływu konfiguracji."""
    _LOGGER.warning(str(config_entry.data))
    liczniki = [1, 2, 3]

    for x in liczniki:
        async_add_entities([AisHelloSensor(x, "licznik" + str(x))])


class AisHelloSensor(Entity):
    """Reprezentacja sensora AisHelloSensor."""

    def __init__(self, id, name):
        """Inicjalizacja sensora."""
        self._id = id
        self._name = name
        self._state = None

    @property
    def name(self):
        """Funkcja zwracająca nazwę sensora."""
        return self._name

    @property
    def state(self):
        """Funkcja zwracająca status sensora."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Funkcja zwracająca jednostkę miary sensora."""
        return ENERGY_KILO_WATT_HOUR

    @property
    def icon(self):
        return "mdi:counter"

    def update(self):
        """Pobranie aktualnego statusu sensora
        """
        # epoch time in seconds
        self._state = int(time()) * self._id
