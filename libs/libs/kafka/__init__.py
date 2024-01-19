__all__ = ["MessageProducer"]

import atexit
import json
from datetime import date, datetime
from typing import Callable, Generic, TypeVar
from uuid import uuid4

from confluent_kafka import Producer
from munch import Munch

from libs.configuration import configure
from libs.logging import Logging

T = TypeVar("T", bound=Munch)


class MessageProducer(Logging, Generic[T]):
    def __init__(
        self,
        topic: str,
        key_serializer: Callable[[], str],
        value_serializer: Callable[[T], bytes],
        error_topic: str = None,
    ) -> None:
        unique_index = f"{self.__class__.__name__}#{topic}"
        super().__init__(unique_index)

        env = configure()

        self._client = Producer(
            {
                "client.id": unique_index,
                "bootstrap.servers": env.KAFKA_BOOTSTRAP_SERVERS,
                # "security.protocol": env.kafka.security_protocol,
                # "sasl.mechanism": env.kafka.sasl_mechanism,
                # "sasl.username": env.kafka.sasl_username,
                # "sasl.password": env.kafka.sasl_password,
            }
        )
        self._topic = topic
        self._dead_letter_topic = (
            error_topic if error_topic is not None else f"{topic}_delivery_error"
        )

        self._key_serializer = key_serializer
        self._value_serializer = value_serializer

        atexit.register(self.__cleanup)

    def __cleanup(self):
        self._client.flush()

    @property
    def topic(self):
        """read-only property"""
        return self._topic

    @property
    def dead_letter_topic(self):
        """read-only property"""
        return self._dead_letter_topic

    def __delivery_callback(self, err, msg):
        """private method"""
        if err is not None:
            # TODO: dead lettering here instead
            self.logger.error(err)
        else:
            self.logger.info(
                {
                    "topic": msg.topic(),
                    "key": msg.key(),
                    "value": msg.value(),
                }
            )

    def produce(self, data: T):
        key = self._key_serializer(str(uuid4()))
        value = self._value_serializer(data)
        # self.logger.info(data)

        self._client.produce(
            topic=self.topic,
            key=key,
            value=value,
            on_delivery=self.__delivery_callback,
        )
        self._client.poll(0)


# class MessageConsumer(Logging, Generic[T]):
#     def __init__(self, topic: str) -> None:
#         unique_index = f"{self.__class__.__name__}#{topic}"
#         super().__init__(unique_index)

#         env = configure()

#         self._client = Consumer(
#             {
#                 "client.id": unique_index,
#                 "bootstrap.servers": config.kafka.bootstrap_servers,
#                 # "security.protocol": config.kafka.security_protocol,
#                 # "sasl.mechanism": config.kafka.sasl_mechanism,
#                 # "sasl.username": config.kafka.sasl_username,
#                 # "sasl.password": config.kafka.sasl_password,
#                 "session.timeout.ms": config.kafka.session_timeout_ms,
#             }
#         )
#         self._client.subscribe([topic])

#         atexit.register(self.__cleanup)

#     def __cleanup(self):
#         self._client.close()

#     def __deserialize(self, data: bytes):
#         try:
#             return json.loads(data.decode())
#         except json.JSONDecodeError:
#             self.logger.error(data.decode())

#     def consume(self) -> T:
#         raise NotImplementedError()
#         # while True:
#         #     msg = self._client.poll(1.0)

#         #     if msg is not None and msg.error() is None:
#         #         self.logger.info(
#         #             json.dumps(
#         #                 {
#         #                     "key": msg.key().decode("utf-8"),
#         #                     "value": msg.value().decode("utf-8"),
#         #                 }
#         #             )
#         #         )
