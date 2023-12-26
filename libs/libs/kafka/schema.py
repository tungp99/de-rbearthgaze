from abc import ABC, abstractmethod

from confluent_kafka.schema_registry import SchemaRegistryClient

from libs.configuration import configure


class AbstractSchemaRegistry(ABC):
    def __init__(self) -> None:
        config = configure()

        self._client = SchemaRegistryClient({"url": config.KAFKA_SCHEMA_REGISTRY_URL})

    @property
    def client(self):
        return self._client

    @property
    @abstractmethod
    def raw_schema(self) -> str:
        raise NotImplementedError()

    @property
    @abstractmethod
    def t1_schema(self) -> str:
        raise NotImplementedError()

    @property
    @abstractmethod
    def t2_schema(self) -> str:
        raise NotImplementedError()
