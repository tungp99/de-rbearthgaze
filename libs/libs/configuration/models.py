__all__ = ["Configuration"]

from enum import Enum

from munch import DefaultMunch

from libs.core import SingletonMeta

# from typing import NewType


class Environment(Enum):
    DEVELOPMENT = "DEVELOPMENT"
    TESTING = "TESTING"
    PRODUCTION = "PRODUCTION"


# ENV = NewType("Environment", Environment)


class Configuration(DefaultMunch, metaclass=SingletonMeta):
    # env: ENV
    DATASTORAGE_AZURE_ACCOUNTNAME: str
    DATASTORAGE_AZURE_ACCESSKEY: str

    SPARK_MASTER_URL: str

    KAFKA_BOOTSTRAP_SERVERS: str
    KAFKA_SESSION_TIMEOUT_MS: str
    KAFKA_SCHEMA_REGISTRY_URL: str

    KAFKA_TOPIC_RAW_AIRCRAFT: str
    KAFKA_TOPIC_T1_AIRCRAFT: str
    KAFKA_TOPIC_T2_AIRCRAFT: str
    KAFKA_TOPIC_RAW_AIRPORT: str
    KAFKA_TOPIC_T1_AIRPORT: str
    KAFKA_TOPIC_T2_AIRPORT: str
    KAFKA_TOPIC_RAW_AIRLINE: str
    KAFKA_TOPIC_T1_AIRLINE: str
    KAFKA_TOPIC_T2_AIRLINE: str
    KAFKA_TOPIC_RAW_FLIGHT_SIGNAL: str
    KAFKA_TOPIC_T1_FLIGHT_SIGNAL: str
    KAFKA_TOPIC_T2_FLIGHT_SIGNAL: str

    POSTGRE_JDBC_URL: str
    POSTGRE_USER: str
    POSTGRE_PASSWORD: str
