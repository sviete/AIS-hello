from homeassistant import config_entries
import voluptuous as vol
import logging

_LOGGER = logging.getLogger(__name__)


class AisHelloConfigFlow(config_entries.ConfigFlow, domain="ais_hello"):
    """Przykład przepływu konfiguracji w integracji."""

    async def async_step_user(self, user_input=None):
        """Uruchomienie konfiguracji przez użytkownika"""
        # przejście do kroku potwierdzenia dodania integracji
        return self.async_show_form(step_id="confirm")

    async def async_step_confirm(self, user_input=None):
        """Obsługa kroku potwierdzenia przez użytkownika."""
        if user_input is not None:
            # Przejście do kroku logowanie
            return self.async_show_form(step_id="login", data_schema=vol.Schema(
                {vol.Required("username"): str, vol.Required("password"): str}
            ))

        return self.async_show_form(step_id="confirm")

    async def async_step_login(self, user_input=None):
        """Krok logowania"""
        if user_input is not None:
            # TODO logowanie do serwisu
            _LOGGER.info("User input: " + str(user_input))
            #

            # Zakończenie i zapis konfiguracji
            return self.async_create_entry(title="Przykładowa integracja AIS", data=user_input)

        return self.async_show_form(step_id="confirm")
