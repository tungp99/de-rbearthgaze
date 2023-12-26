# Development

1. Install [poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)
2. Run in terminal: `$ poetry install`
3. `$ poetry run boom <module>`, ex. `M1_Producers.aircraft:run`

There will be `.secrets/env.yaml`, you can create `.secrets/env.local.yaml` and tailor some variables on your own interest.

# Technologies

1. Apache Kafka: message broker
2. Apache Spark: data processing
3. Apache Iceberg + Nessie: warehouse and metastore
4. React + OpenLayers/OpenStreetMap/Google Maps: showcase
5. (Optional) Prefect: job scheduling
6. (Optional) Bitwarden: secret manager
