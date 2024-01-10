import logging

from libs.configuration import configure
from pyspark.sql import SparkSession

from shared.spark_config import create_spark_config

__MODULE = "M2_Processors.aircraft.raw"
logger = logging.getLogger("notebook")
env = configure()
conf = create_spark_config().setAppName(__MODULE)

spark = SparkSession.builder.config(conf=conf).getOrCreate()

spark.sql("SHOW CATALOGS").show()
