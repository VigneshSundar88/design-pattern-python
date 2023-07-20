from distutils.log import info
from sqlite3 import connect
import logging
import os
import uuid

class Driver:
   
    layer = ""
    datasource = ""
    pipeline = ""
    tablename = ""
    env = ""
    sPipeline = ""
    
    def get_dbutils(spark):
        from pyspark.dbutils import DBUtils
        return DBUtils(spark)

    layer = get_dbutils.widgets.get("layer")
    datasource = get_dbutils.widgets.get("datasource")
    pipeline = get_dbutils.widgets.get("pipeline")
    tablename = get_dbutils.widgets.get("tablename")
    env = os.environ["env"]

    def parse_args(self):
        sPipeline = f"{self.layer}.{self.datasource}.\
                                   {self.pipeline}.{self.env}"

        random_uuid = str(uuid.uuid4()).replace("-", "")

        sessionName = f"{sPipeline}_{random_uuid}"
        logger.log(f"New Session Name Created {sessionName}", level=info)
        logger.log(f"Pipeline - Starting {sPipeline}", level=info)

if __name__ == '__main__':
    driver_obj = Driver()
    driver_obj.parse_args()
    logger = logging.getLogger(driver_obj.__class__.__name__)

    