#!/usr/bin/env python3
"""
Space mission validation module.

Defines data models for crew members and space missions with
advanced validation rules using Pydantic.
"""
from enum import Enum
from sys import exit
try:
    from data_generator import CrewMissionGenerator, DataConfig
except ImportError:
    print("You need data_generator.py from ressources in ex2")
    exit(1)
from pydantic import BaseModel, Field, ValidationError, model_validator
from pydantic_core import PydanticCustomError
from datetime import datetime
from typing_extensions import Self


class Rank(str, Enum):
    """Enumeration of possible crew ranks."""

    CADET = 'cadet'
    OFFICIER = 'officier'
    LIEUTENANT = 'lieutenant'
    CAPTAIN = 'captain'
    COMMANDER = 'commander'


class CrewMember(BaseModel):
    """Represent a crew member participating in a space mission."""
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    """Represent a space mission with validation constraints on crew."""
    mission_id: str = Field(min_length=3, max_length=30)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def multi_validator(self) -> Self:
        """Validate mission consistency and crew requirements.

        Ensures:
        - Mission ID starts with 'M'
        - Crew contains at least one captain
        - Long missions have enough experienced crew members
        - All crew members are active
        """
        if self.mission_id[0] != 'M':
            raise ValidationError.from_exception_data(
                title='Space Crew',
                line_errors=[
                    {
                        'type': 'value_error',
                        'ctx': {'error': 'lala'},
                        'loc': ('mission_id',),
                        'input': self.mission_id
                    }
                ],
            )

        crew_ranks: set = {rank.rank for rank in self.crew}
        if 'captain' not in crew_ranks:
            raise ValidationError.from_exception_data(
                title='Space Crew',
                line_errors=[
                    {
                        'type': 'value_error',
                        'ctx': {'error': ('Your crew needs: '
                                          + f'{
                                               {'captain', 'commander'}
                                               .difference(crew_ranks)
                                               }'
                                          )},
                        'loc': ('crew',),
                        'input': f'You have only {', '.join([*crew_ranks])}.'
                    }
                ],
                hide_input=True
            )

        freq_exp_crew = (sum(1 for p in self.crew if p.years_experience >= 5)
                         /
                         len(self.crew))
        if self.duration_days > 365 and freq_exp_crew < 0.5:
            raise ValidationError.from_exception_data(
                title='Space Crew',
                line_errors=[
                    {
                        'type': PydanticCustomError(
                            'Unexperimented_crew',
                            (f'{freq_exp_crew:.2f} of'
                                + ' the crew is experienced (+ 5 years)')
                            ),
                        'loc': ('crew', 'years_experience',),
                        'input': f'Years of experience: {
                            [p.years_experience for p in self.crew]}'
                    }
                ]
            )

        not_activ_p = [p.name for p in self.crew if not p.is_active]
        if len(not_activ_p) > 0:
            raise ValidationError.from_exception_data(
                title='Space Crew',
                line_errors=[
                    {
                        'type': PydanticCustomError(
                            'Activation_error',
                            f'{len(not_activ_p)} passenger(s) not activated.'
                        ),
                        'loc': ('crew', 'CrewMember.is_activate'),
                        'input': '; '.join(not_activ_p)
                    }
                ]
            )
        return self


# Datas to test errors
try:
    datas: list = CrewMissionGenerator(DataConfig()).generate_mission_data()

    crew = [
        CrewMember(
            member_id='X51',
            name='Untel',
            rank=Rank.COMMANDER,
            age=25,
            specialization='pilot',
            years_experience=6),
        CrewMember(
            member_id='X50',
            name='Intel',
            rank=Rank.CAPTAIN,
            age=20,
            specialization='logistic',
            years_experience=5,
            is_active=False),
        CrewMember(
            member_id='X49',
            name='Antel',
            rank=Rank.OFFICIER,
            age=30,
            specialization='blabla',
            years_experience=2)
        ]

    datas.append({
            'mission_id': 'M51',
            'mission_name': 'Name',
            'destination': 'error',
            'launch_date': datetime.now(),
            'duration_days': 500,
            'crew': [*crew],
            'budget_millions': 1.5
            })
except ValidationError as e:
    print(e)


def main() -> None:
    """Run mission validation on generated datasets.

    Iterates through generated mission data, validates each mission,
    and prints either a success message or validation errors.
    """
    i = 0
    for d in datas:
        i += 1
        print("\n=====================================")
        try:
            mission = SpaceMission(**d)
            print("\033[2m\033[32mValid mission created:\033[0m\033[0m")
            print("Mission:", mission.mission_name)
            print("ID:", mission.mission_id)
            print("Destination:", mission.destination)
            print("Duration:", mission.duration_days, 'days')
            print("Budget:", f'${mission.budget_millions:.2f}M')
            print("Crew size:", len(mission.crew))
            print("Crew members:")
            for p in mission.crew:
                print(f'- {p.name} - {p.specialization.capitalize()}')

        except (ValidationError) as e:
            print(f'\033[1m\033[31mUnvalid mission (n_{i})\033[0m\033[0m')
            for msg in e.errors():
                m = '; '.join([x for x in msg['loc'] if isinstance(x, str)])
                print(f"\033[31m{m}\033[0m")
                print(msg.get('msg'))
                print('Input:', msg['input'])


if __name__ == "__main__":
    print("Space Mission Crew Validation")
    main()
