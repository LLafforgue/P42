#!/usr/bin/env python3
from pydantic import BaseModel, Field, ValidationError
from sys import exit
from datetime import datetime
from typing import Optional
try:
    import ex2.data_generator as data_generator
except ImportError:
    print("You need data_generator.py from ressources in ex0")
    exit(1)


class SpaceStation(BaseModel):
    """Represents a space station with validated operational data."""

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] | None = Field(default=None, max_length=200)


def main() -> None:
    """Generates and validates space station data for demonstration."""
    data_gen = data_generator.SpaceStationGenerator(
        data_generator.DataConfig())
    datas: dict[str, dict] = {
        'goods': {
            'station_id': 'ISS001',
            'name': 'International Space Station',
            'crew_size': 6,
            'power_level': 85.5,
            'oxygen_level': 92.3,
            'last_maintenance': "1984-04-01T10:30:00"
        },

        'wrongs': {
            'station_id': 'ISS002',
            'name': 'Venus Delirium Station',
            'crew_size': 1000,
            'power_level': 120.2,
            'oxygen_level': 10,
            'last_maintenance': "2020-03-18T14:30:00"
        },
        'generate': data_gen.generate_station_data(1)[0]
    }
    for d in datas.values():
        try:
            print("\n========================================\n")
            station = SpaceStation(**d)
            print('valid station created:')
            print("ID:", station.station_id)
            print("Name:", station.name)
            print("Crew:", station.crew_size, "peoples")
            print("Power:", station.power_level)
            print("oxygen_level", station.oxygen_level)
            print("Status:", "Operational" if station.is_operational
                  else "dysfunctional")
        except (ValidationError) as e:
            print('Unvalid station')
            for msg in e.errors():
                m = msg['loc'][0]
                print(f"\033[31m{m}\033[0m")
                print(msg.get('msg'))


if __name__ == "__main__":
    """Entry point for space station data validation."""
    print("Space Station Data Validation")
    main()
