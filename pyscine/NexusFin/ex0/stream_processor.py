#!/usr/bin/env python3
"""Stream Process."""
from abc import ABC, abstractmethod
from typing import Any


class ValidateError(Exception):
    """Built Validate Error."""


class DataProcessor(ABC):
    """Abstract a class."""

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return result string."""

    def format_output(self, result: str) -> str:
        """Format the output string."""
        try:
            if result is None:
                raise ValueError("None input")
            else:
                return (f"OUTPOUT: {result}\n")
        except ValueError as e:
            print(e)
            return ("No Outpout\n")


class NumericProcessor(DataProcessor):
    """Numeric Processor."""

    error: Any = None

    def validate(self, data: list[int]) -> bool:
        """Validate if data is appropriate for this processor."""
        if type(data) is not list:
            return False
        for ele in data:
            if type(ele) is not int:
                self.error = ele
                return False
        if len(data) == 0:
            return False
        else:
            return True

    def process(self, data: list[int]) -> str:
        """Process the data and return result string."""
        try:
            if not self.validate(data):
                raise ValidateError(f"\033[1m{self.error}\033[0m is"
                                    + " an invalid type data")
            data_len = len(data)
            data_sum = sum(data)
            data_avg = data_sum/data_len
            return (f"Processed {data_len} numeric values,"
                    + f" sum = {data_sum}, avg = {data_avg}")
        except (TypeError, ValueError, Exception, ValidateError) as e:
            print(e)
            return ("Invalid Process")


class TextProcessor(DataProcessor):
    """Text Processor."""

    def validate(self, data: str) -> bool:
        """Validate if data is appropriate for this processor."""
        if type(data) is not str:
            return False
        if len(data) == 0:
            return False
        else:
            return True

    def process(self, data: str) -> str:
        """Process the data and return result string."""
        try:
            if not self.validate(data):
                raise ValidateError(f"'{data}' is an invalid type data")
            data_len = len(data)
            words = len(data.split(" "))
            return (f"Processed text: {data_len} character(s),"
                    + f" {words} word(s).")
        except (TypeError, ValueError, ValidateError, Exception) as e:
            print(e)
            return ("Invalid Process")


class LogProcessor(DataProcessor):
    """Text Formater Processor for Log."""

    def validate(self, data: str) -> bool:
        """Validate if data is appropriate for this processor."""
        if type(data) is not str:
            return False
        if data[:5] != "ERROR" and data[:7] != "SUCCESS" and \
           data[:4] != "INFO":
            return False
        else:
            return True

    def process(self, data: str) -> str:
        """Process the data and return result string."""
        try:
            if not self.validate(data):
                raise ValidateError(f"'{data}' is an invalid type data")
            else:
                if data[:5] == "ERROR":
                    return f"[ALERT] Error level detected {data[6:]}"
                elif data[:7] == "SUCCESS":
                    return f"[LOG] SUCCESS level detected: {data[8:]}"
                else:
                    return f"[INFO] INFO level detected: {data[5:]}"
        except (TypeError, ValueError, ValidateError, Exception) as e:
            print(e)
            return ("Invalid Process")


def polymorphism_process(process: DataProcessor, data: Any) -> str:
    """Demonstrate polymorphisme processing."""
    result = process.process(data)
    outpout = process.format_output(result)
    return (outpout[8:])


if __name__ == "__main__":
    num = NumericProcessor()
    test_1 = [2, 3, 5, 7, 11]
    print("Initializing Text Processor...")
    print(f"Processing data: {test_1}")
    if num.validate(test_1):
        print("Validation: Numeric data verified")
    result = num.process(test_1)
    print(num.format_output(result))

    text = TextProcessor()
    test_2 = "Hello Nexus World"
    print("Initializing Text Processor...")
    print("Processing data: 'Hello Nexus World'")
    if text.validate(test_2):
        print("Validation: Text data verified")
    result = text.process(test_2)
    print(text.format_output(result))

    log = LogProcessor()
    test_3 = "ERROR: Connection timeout"
    print("Initializing Text Processor...")
    print("Processing data: 'ERROR: Connection timeout'")
    if log.validate(test_3):
        print("Validation: Log entry verified")
    result = log.process(test_3)
    print(log.format_output(result))

    print("=== Polymorphic Processing Demo ===\n")
    processors = [
        (NumericProcessor(), [1, 2, 3]),
        (TextProcessor(), "HelloWord"),
        (LogProcessor(), "INF: System ready")
        ]
    result_num = 0
    for process in processors:
        result_num += 1
        intro = f"Result {result_num}:"
        print(intro + polymorphism_process(*process))
