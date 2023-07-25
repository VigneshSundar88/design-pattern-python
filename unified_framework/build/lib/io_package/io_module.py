from typing import Optional
from io_package.job_module import job_module
from pyspark.sql import SparkSession


class LoggerProvider:
    def get_logger(spark:SparkSession, custom_prefix: Optional[str] = ""):
        print(type(spark))
        print(type(custom_prefix))
        log4j_logger = spark._jvm.org.apache.log4j
        return log4j_logger.LogManager.getLogger(custom_prefix)

    # def __full_name__(self):
    #     klass = self.__class__
    #     module = klass.__module__
    #     if module == "__builtin__":
    #         return klass.__name__
    #     return module + "." + klass.__name__
