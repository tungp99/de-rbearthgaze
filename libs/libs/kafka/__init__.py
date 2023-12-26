__all__ = ["MessageProducer"]

import atexit
import json
from datetime import date, datetime
from typing import Generic, TypeVar

from confluent_kafka import Producer
from munch import Munch

from libs.configuration import configure
from libs.logging.Logging import Logging

T = TypeVar("T", bound=Munch)


class MessageProducer(Logging, Generic[T]):
    def __init__(self, topic: str, error_topic: str = None) -> None:
        unique_index = f"{self.__class__.__name__}#{topic}"
        super().__init__(unique_index)

        config = configure()

        self._client = Producer(
            {
                "client.id": unique_index,
                "bootstrap.servers": config.kafka.bootstrap_servers,
                # "security.protocol": config.kafka.security_protocol,
                # "sasl.mechanism": config.kafka.sasl_mechanism,
                # "sasl.username": config.kafka.sasl_username,
                # "sasl.password": config.kafka.sasl_password,
                "schema.registry.url": config.kafka.schema_registry_url,
                # "basic.auth.credentials.source": config.kafka.basic_auth_credentials_source,
                # "basic.auth.user.info": config.kafka.basic_auth_user_info,
            }
        )
        self._topic = topic
        self._dead_letter_topic = (
            error_topic if error_topic is not None else f"{topic}_delivery_error"
        )

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

    def __json_serialize(self, obj):
        """JSON serializer for objects not serializable by default json code"""
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        raise TypeError(f"Type {type(obj)} not serializable")

    def __serialize(self, data: T):
        """private method"""
        return json.dumps(data, default=self.__json_serialize).encode()

    def __delivery_callback(self, err, msg):
        """private method"""
        if err:
            # TODO: dead lettering here instead
            self.logger.error(err)
        else:
            self.logger.info(
                json.dumps(
                    {
                        "topic": msg.topic(),
                        "key": msg.key().decode("utf-8"),
                        "value": msg.value().decode("utf-8"),
                    }
                )
            )

    def produce(self, data: T):
        message = self.__serialize(data)
        self.logger.debug(message)

        self._client.produce(self.topic, message, callback=self.__delivery_callback)
        self._client.poll(0)


# class MessageConsumer(Logging, Generic[T]):
#     def __init__(self, topic: str) -> None:
#         unique_index = f"{self.__class__.__name__}#{topic}"
#         super().__init__(unique_index)

#         config = configure()

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
