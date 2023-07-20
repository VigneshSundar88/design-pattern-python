from distutils.log import info
from . import ApplicationProperties
import uuid
import sys
from io_package import io_module, job_module
from pyspark.sql import SparkSession
from config import AppConfig

class PipelineBuilder:
    def main():
        spark: SparkSession =  job_module.job_module.getSpark()

        driver_obj = PipelineBuilder()
        logger = io_module.LoggerProvider.get_logger(spark, driver_obj.__class__.__name__)
        input_args = sys.argv

        applicationProperties = ApplicationProperties.ApplicationProperties(input_args)
        applicationProperties.parse_args()
    
        random_uuid = str(uuid.uuid4()).replace("-", "")

        if len(applicationProperties.LAYER) == 0 or len(applicationProperties.DATASOURCE) == 0 \
            or len(applicationProperties.PIPELINE) == 0 or len(applicationProperties.ENV) == 0:
                raise Exception("Mandatory parameters should be passed!!!")

        applicationProperties.sPipeline = "{}.{}.{}.{}".format(applicationProperties.LAYER[0],
                                              applicationProperties.DATASOURCE[0],
                                              applicationProperties.PIPELINE[0],
                                              applicationProperties.ENV)

        print("applicationProperties.sPipeline: "+applicationProperties.sPipeline)

        #driver_obj = PipelineBuilder()
        #logger = logging.getLogger(driver_obj.__class__.__name__)
        #logger.setLevel(logging.INFO)

        applicationProperties.sessionName = f"{applicationProperties.sPipeline}_{random_uuid}"
        logger.info(f"New Session Name Created {applicationProperties.sessionName}")
        logger.info(f"Pipeline - Starting {applicationProperties.sPipeline}")

        print("applicationProperties.sessionName: "+applicationProperties.sessionName)

        driver_obj._parse_job_config(logger, applicationProperties)

    def _parse_job_config(self, logger, applicationProperties):
        obj_job_config = AppConfig.get_my_config(applicationProperties.sPipeline)
        logger.info("Config obtained for the pipeline key: {} - {}".format(applicationProperties.sPipeline), obj_job_config)

    

