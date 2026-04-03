#!/usr/bin/env python3
from enum import Enum
from sys import exit
try:
    from ex2.data_generator import AlienContactGenerator, DataConfig
except ImportError:
    print("You need data_generator.py from ressources in ex1")
    exit(1)
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional
from typing_extensions import Self


class ContactType(str, Enum):

    RADIO = 'radio'
    VISUAL = 'visual'
    PHYSICAL = 'physical'
    TELEPATHIC = 'telepathic'


test = AlienContactGenerator(DataConfig())
datas: list = test.generate_contact_data(1)
datas.append(
    {
        'contact_id': 'AC_2024_001',
        'timestamp': "2016-12-07T10:30:00",
        'location': 'Wite House',
        'contact_type': 'radio',
        'signal_strength': 8.5,
        'duration_minutes': 1,
        'witness_count': 5,
        'message_received': 'Surprise !'
    }
)
datas.append(
    {
        'contact_id': 'AC_2024_001',
        'timestamp': "2016-12-07T10:30:00",
        'location': 'blabla',
        'contact_type': 'telepathic',
        'signal_strength': 8.5,
        'duration_minutes': 50,
        'witness_count': 1,
        'message_received': 'error'
    }
)


class AlienContact(BaseModel):

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] | None = Field(default=None,
                                                   max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_ID(self) -> Self:
        """
        Validate that the contact ID starts with the expected prefix.

        The contact ID must begin with 'AC'. Raises a ValidationError
        if the condition is not met.

        Returns:
            Self: The validated model instance.
        """
        if self.contact_id[:2] != 'AC':
            raise ValidationError.from_exception_data(
                title="AlienContact",
                line_errors=[
                    {
                        'type': 'value_error',
                        'loc': ('contact_id',),
                        'ctx': {'error': "ID name has to start with 'AC...'"},
                        'input': self.contact_id
                    }
                ],
                hide_input=True
            )
        else:
            return self

    @model_validator(mode='after')
    def contact_type_rules(self) -> Self:
        """
        Apply validation rules depending on the contact type.

        Rules:
        - 'physical' contacts must be verified.
        - 'telepathic' contacts require at least 3 witnesses.

        Raises:
            ValidationError: If any rule is violated.

        Returns:
            Self: The validated model instance.
        """
        if self.contact_type == 'physical':
            if not self.is_verified:
                raise ValidationError.from_exception_data(
                    title="AlienContact",
                    line_errors=[
                        {
                            'type': 'value_error',
                            'loc': ('is_verified',),
                            'ctx': {'error': 'The report must be verified'},
                            'input': f'Verified: {self.is_verified}',
                        }
                    ],
                    )
            else:
                return self
        if self.contact_type == 'telepathic':
            if self.witness_count < 3:
                raise ValidationError.from_exception_data(
                    title="AlienContact",
                    line_errors=[
                        {
                            'type': 'value_error',
                            'loc': ('witness_count',),
                            'ctx': {'error': 'You need at least 3 witnesses'},
                            'input': f"{self.witness_count} witness(es)",
                        }
                    ],
                )
            else:
                return self
        else:
            return self

    @model_validator(mode='after')
    def verif_signal_strength(self) -> Self:
        """
        Ensure strong signals are associated with a message.

        If the signal strength is greater than 7.0, a message must
        be provided. Raises a ValueError otherwise.

        Returns:
            Self: The validated model instance.
        """
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("A message is not an option for " +
                             "strong signals (>7.0)")
        else:
            return self


def main(datas: list[dict]) -> None:
    """
    Process and validate a list of alien contact reports.

    Each dictionary in the input list is used to instantiate an
    AlienContact model. Valid entries are displayed with formatted
    output, while invalid ones print detailed validation errors.

    Args:
        datas (list[dict]): List of raw contact data dictionaries.

    Returns:
        None
    """
    i: int = 0
    for d in datas:
        i += 1
        try:
            print("\n===================================")
            contact = AlienContact(**d)
            print("\033[2m\033[32mValid contact report:\033[0m\033[0m")
            print("ID:", contact.contact_id.upper())
            print("Type:", contact.contact_type._value_)
            print("Location:", contact.location)
            print(f"Signal: {contact.signal_strength}/10")
            print("Duration:", contact.duration_minutes, "minutes")
            message = ("Message: " + contact.message_received
                       if contact.message_received is not None
                       else "No message")
            print(message)
        except (ValidationError) as e:
            print(f'\033[1m\033[31mUnvalid contact (n_{i})\033[0m\033[0m')
            for msg in e.errors():
                m = msg['loc'][0] if len(msg['loc']) == 1 else msg.get('type')
                print(f"\033[31m{m}\033[0m")
                print(msg.get('msg'))
                print('Input:', msg['input'])


if __name__ == "__main__":
    main(datas)
