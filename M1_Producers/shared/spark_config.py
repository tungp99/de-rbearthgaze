from libs.configuration import configure
from pyspark import SparkConf


def create_spark_config(app_name: str):
    env = configure()

    return (
        SparkConf()
        .setAppName(app_name)
        .setMaster(env.SPARK_MASTER_URL)
        .set(
            "spark.jars.packages",
            ",".join(
                (
                    "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0",
                    "org.apache.spark:spark-avro_2.12:3.5.0",
                    "org.apache.hadoop:hadoop-common:3.3.6",
                    "org.apache.hadoop:hadoop-azure:3.3.6",
                    "com.azure:azure-storage-blob:12.25.1",
                )
            ),
        )
        .set("spark.hadoop.fs.adl.impl", "org.apache.hadoop.fs.adl.AdlFileSystem")
        .set("spark.fs.AbstractFileSystem.adl.impl", "org.apache.hadoop.fs.adl.Adl")
        .set(
            f"fs.azure.account.auth.type.{env.DATASTORAGE_AZURE_ACCOUNTNAME}.dfs.core.windows.net",
            "SharedKey",
        )
        .set(
            f"fs.azure.account.key.{env.DATASTORAGE_AZURE_ACCOUNTNAME}.dfs.core.windows.net",
            env.DATASTORAGE_AZURE_ACCESSKEY,
        )
        .set("spark.streaming.stopGracefullyOnShutdown", "true")
    )
