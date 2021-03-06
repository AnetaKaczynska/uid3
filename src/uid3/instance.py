# AUTOGENERATED! DO NOT EDIT! File to edit: src/instance.ipynb (unless otherwise specified).

__all__ = ['Instance']

# Cell
from typing import List

from .reading import Reading

# Cell
class Instance:
    def __init__(self, readings: List[Reading] = None):
        self.readings = readings
        if not readings:
            self.readings = []

    def get_readings(self) -> List[Reading]:
        return self.readings

    def get_reading_for_attribute(self, att_name: str) -> Reading:
        for r in self.readings:
            if r.get_base_att().get_name() == att_name:
                return r
        return None

    def set_readings(self, readings: List[Reading]):
        self.readings = readings

    def add_reading(self, reading: Reading):
        self.readings.append(reading)

    def to_arff(self) -> str:
        result = ''
        for reading in self.readings:
            result += str(reading) + ','
        result = result[:-1]  # delete the last coma ','
        result += '\n'
        return result
