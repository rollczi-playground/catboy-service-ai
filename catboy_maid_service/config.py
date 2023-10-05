## config.py

from typing import Any, Dict

class Config:
    """Configuration class for Flask, SQLAlchemy, OrangeHRM, and Mautic."""

    def __init__(self):
        self._config: Dict[str, Any] = {
            'FLASK': {
                'DEBUG': False,
                'TESTING': False,
                'SECRET_KEY': 'secret_key',
                'JSON_SORT_KEYS': False,
            },
            'SQLALCHEMY': {
                'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
                'SQLALCHEMY_TRACK_MODIFICATIONS': False,
            },
            'ORANGEHRM': {
                'API_BASE_URL': 'http://localhost:8000',
                'API_USERNAME': 'admin',
                'API_PASSWORD': 'admin',
            },
            'MAUTIC': {
                'API_BASE_URL': 'http://localhost:8000',
                'API_USERNAME': 'admin',
                'API_PASSWORD': 'admin',
            },
        }

    def get(self, package: str, key: str) -> Any:
        """Get a configuration value.

        Args:
            package: The package to get the configuration for.
            key: The configuration key.

        Returns:
            The configuration value.
        """
        return self._config.get(package, {}).get(key)

    def set(self, package: str, key: str, value: Any) -> None:
        """Set a configuration value.

        Args:
            package: The package to set the configuration for.
            key: The configuration key.
            value: The configuration value.
        """
        if package not in self._config:
            self._config[package] = {}
        self._config[package][key] = value
