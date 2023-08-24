import json
import os


class Settings:
    _settings = dict()

    def read_config(self, filepath: str) -> None:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File '{filepath}' not found.")

        with open(filepath, 'r') as file:
            try:
                self._settings = json.load(file)
            except json.JSONDecodeError:
                raise ValueError(f"File '{filepath}' is not a valid JSON file.")

    def get(self, key: str, default=None):
        return self._settings.get(key, default)
