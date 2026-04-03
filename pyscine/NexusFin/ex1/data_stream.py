"""Data Stream Processing System."""
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Interface for data streams."""

    def __init__(self, stream_id: str) -> None:
        """Initialize the data stream with an ID."""
        self.stream_id = stream_id
        self.processed_count: str = ""
        self.high_priority: bool = False

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on basic validity."""
        filtered: List = []
        try:
            filtered = [data for data in data_batch if isinstance(data, Dict)
                        and len(data) == 1]
            for data in data_batch:
                if len(data) > 1 and isinstance(data, dict):
                    for valid_data in [{k: v} for k, v in data.items()]:
                        filtered.append(valid_data)
            filtered = [data for data in filtered
                        if isinstance([*data][0], str)
                        and isinstance([*data.values()][0], int | None)]
        except (Exception, ValueError, TypeError) as e:
            print('Prime filter failed', e)
        finally:
            return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        try:
            return {
                "stream_id": self.stream_id,
                "processed_count": str(self.processed_count),
                "high_priority": self.high_priority
            }
        except (ValueError, TypeError) as e:
            print(e)
            return {}


class SensorStream(DataStream):
    """Filter Environmental Data."""

    def __init__(self, stream_id: str) -> None:
        """Initialize Sensor Stream."""
        super().__init__(stream_id)
        self.avg_temp: str = ""
        self.keys = {"temp", "humidity", "pressure", "air_quality", "max_temp"}
        self.max_temps: List = []

    def process_batch(self, data_batch: List[Dict[str, int]]) -> str:
        """Process a batch of data."""
        try:
            filtered = self.filter_data(data_batch)
            self.processed_count += str(len(filtered))
            avg_temp = sum(d["temp"] for d in filtered
                           if 'temp' in [*d]) / sum(1 for d in filtered
                                                    if 'temp' in d)
            self.avg_temp = f"{avg_temp:.1f}"
            return (f"{len(filtered)} readings processed, "
                    + f"avg temp: {avg_temp:.1f}°C")
        except (ZeroDivisionError, TypeError, Exception) as e:
            print(e)
            return "No valid sensor data to process."

    def filter_data(self, data_batch: List[Dict[str, int]],
                    criteria: Optional[str] = None) -> List[Dict[str, int]]:
        """Filter data based on sensor keys."""
        filtered: List[Dict] = []
        try:
            filtered = super().filter_data(data_batch)
            if isinstance(criteria, str) and criteria.isdigit():
                self.max_temps = [temp for temp in filtered
                                  if temp.get('temp')
                                  and temp['temp'] > int(criteria)]
                self.high_priority = True
            else:
                raise TypeError("Exemple of max temp : '100'")
            return [data for data in filtered
                    if set(data).intersection(self.keys)]
        except (Exception):
            return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        stats = super().get_stats()
        stats["processed_count"] = self.processed_count + " readings"
        stats["Type"] = "Environmental Data"
        stats["avg_temp"] = self.avg_temp
        if self.high_priority:
            stats['critical'] = (f"{len(self.max_temps)} "
                                 + "critical sensor alerts")
        return stats


class TransactionStream(DataStream):
    """Filter Transaction Data."""

    def __init__(self, stream_id: str) -> None:
        """Initialize Transaction Stream."""
        super().__init__(stream_id)
        self.net_flow: int = 0
        self.keys = {"buy", "sell", "benefits"}
        self.critical: List = []

    def process_batch(self, data_batch: List[Dict[str, int]]) -> str:
        """Process a batch of data."""
        try:
            filtered = self.filter_data(data_batch)
            self.processed_count = str(filtered.__len__())
            self.net_flow = sum(data['buy'] for data in filtered
                                if 'buy' in data.keys())
            self.net_flow -= sum(data['sell'] for data in filtered
                                 if 'sell' in data.keys())
            return (f"{self.processed_count} operations, "
                    f"{self.net_flow:+} units")
        except (KeyError, TypeError) as e:
            print(e)
            return "No valid transaction data to process."

    def filter_data(self, data_batch: List[Dict[str, int]],
                    criteria: Optional[str] = None) -> List[Dict[str, int]]:
        """Filter data based on transaction keys."""
        filtered: List[Dict] = []
        try:
            filtered = super().filter_data(data_batch, criteria)
            filtered = [data for data in filtered
                        if {*data.keys()}.intersection(self.keys)]
            if criteria and isinstance(criteria, str) and criteria.isdigit():
                self.critical = [data for data in filtered
                                 if [*data.values()][0] >= int(criteria)]
                self.high_priority = True
            return filtered
        except (Exception, TypeError) as e:
            print(e)
            return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return all stream statistics associated with transaction data."""
        stats = super().get_stats()
        stats["processed_count"] = self.processed_count + " operations"
        stats["Type"] = "Financial Data"
        stats["net_flow"] = self.net_flow
        if self.high_priority:
            stats['critical'] = (f"{len(self.critical)} "
                                 + "large transactions")
        return stats


class EventStream(DataStream):
    """Filter Transaction Data."""

    def __init__(self, stream_id: str) -> None:
        """Initialize Event Stream."""
        super().__init__(stream_id)
        self.error_count: int = 0
        self.keys = {"login", "error", "logout"}
        self.critical: List = []

    def process_batch(self, data_batch: List[str]) -> str:
        """Process a batch of data."""
        try:
            filtered = self.filter_data(data_batch)
            self.processed_count = str(len(filtered))
            self.error_count = sum(1 for data in filtered
                                   if data == 'error')
            return (f"{self.processed_count} events, "
                    + f"{self.error_count} errors detected")
        except (KeyError, TypeError) as e:
            print(e)
            return "No valid transaction data to process."

    def filter_data(self, data_batch: List[str],
                    criteria: Optional[str] = None) -> List[str]:
        """Filter data based on event keys."""
        filtered: List = []
        try:
            filtered = data_batch if isinstance(data_batch, list) else []
            filtered = data_batch if all(isinstance(data, str)
                                         for data in data_batch) else []
            filtered = [data for data in filtered
                        if data in self.keys]
            if criteria and isinstance(criteria, str):
                self.critical = [data for data in filtered
                                 if data == criteria.lower()]
                self.high_priority = True
            elif criteria and not isinstance(criteria, str):
                raise TypeError("The filter need a str type for criteria !")
        except (Exception, TypeError) as e:
            print(e)
        finally:
            return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return all stream statistics associated with event data."""
        stats = super().get_stats()
        stats["processed_count"] = self.processed_count + " events"
        stats["Type"] = "System Events"
        stats["errors"] = self.error_count
        if self.high_priority:
            stats["critical"] = (f"{len(self.critical)} "
                                 + "critical events")
        return stats


def StreamProcessor(stream: DataStream,
                    data_batch: List[Any]) -> None:
    """Process mixed stream types through unified interface."""
    stream.process_batch(data_batch)
    analysis = stream.get_stats()
    result = f"{analysis["processed_count"]} processed"
    if analysis["Type"] == "Environmental Data":
        print(f"Sensor data: {result}")
    if analysis["Type"] == "Financial Data":
        print(f"Transaction data: {result}")
    if analysis["Type"] == "System Events":
        print(f"Event data: {result}")


if __name__ == "__main__":
    print("\n=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    Sensor = SensorStream("SENSOR_001")

    Transactions = TransactionStream("TRANS_001")

    Events = EventStream("EVENT_001")

    data_sets: List[Any] = [
        [{"temp": 22}, {"temp": 25, "humidity": 50},
            {(5, 2): "high"}, {"humidity": 15}, {"invalid": 5}],

        [{"buy": 200}, {"sell": 80}, {"buy": 50}],

        ["login", "error",
            "logout", "invalid_event", "error", "login"]
    ]
    streams_set = [Sensor, Transactions, Events]
    for stream, data in zip(streams_set, data_sets):
        print("Initializing Stream...")
        print(f"Stream ID : {stream.get_stats()['stream_id']}, "
              + f"Type : {stream.get_stats()['Type']}")
        print("Processing batch : "
              + f"{stream.filter_data(data)}")
        print(f"Analysis: {stream.process_batch(data)}\n")

    data_sets = [
        [{"temp": 22}, {"temp": 25, "humidity": 50},
            {(5, 2): "high"}, {"humidity": 15}, {"invalid": 5}],
        [{"buy": 200}, {"sell": 80}, {"buy": 50}],
        ["login", "error",
            "logout", "invalid_event", "error", "login"]
    ]

    streams_set_2 = [
        SensorStream("SENSOR_002"),
        TransactionStream("TRANS_002"),
        EventStream("EVENT_002")
        ]
    print("=== Polymorphic Stream Processing ===\n")
    print('Processing mixed stream types through unified interface...')
    streamprocessor = zip(streams_set_2, data_sets)
    for stream, set in streamprocessor:
        StreamProcessor(stream, set)

    print("\n=== Stream filtering active: High-priority data only ===")

    Sensor_filter = SensorStream("SENSOR_003")
    Transactions_filter = TransactionStream("TRANS_003")
    Event_filter = EventStream("EVENT_003")

    sensor_set = [
        {"temp": 22}, {"temp": 25, "humidity": 50},
        {"temp": 30}, {"temp": 18}, {"temp": 27}
        ]
    transact_set = [
        {"buy": 200}, {"sell": 80}, {"buy": 50}
        ]
    event_set = ["login", "error", "error", "invalid_event", "error", "login"]
    filter_sets = [sensor_set, transact_set, event_set]
    data_streams = [
        Sensor_filter,
        Transactions_filter,
        Event_filter
        ]
    set_criteria = ['26', '150', 'error']

    for stream, data, criteria in zip(data_streams, filter_sets, set_criteria):
        print(f"Filter activation {stream.get_stats()['Type']}: ...")
        stream.filter_data(data, criteria)
        print(f"-- {stream.get_stats()["critical"]} --")

    print("\nAll streams processed successfully. Nexus throughput optimal.")
