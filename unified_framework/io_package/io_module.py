from typing import Optional
from io_package.job_module import job_module
from pyspark.sql import SparkSession


class LoggerProvider:
    def get_logger(spark:SparkSession, custom_prefix: Optional[str] = ""):
        log4j_logger = spark._jvm.org.apache.log4j
        return log4j_logger.LogManager.getLogger(custom_prefix)


