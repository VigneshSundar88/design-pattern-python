from abc import ABC, abstractmethod
from pyspark.sql import SparkSession
from pyspark import SparkContext

class job_module(ABC):
    def getSpark():
        spark = SparkSession.Builder().appName("unified_framework").getOrCreate()
        return spark