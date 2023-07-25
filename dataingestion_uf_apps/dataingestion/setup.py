from setuptools import setup, find_packages
from io_module import *
from job_module import *
from audit_package import *
from constants_package import *
#from config import AppConfig

import Pipeline_Builder

setup(
   name='Pipeline_Builder',
   version='1.0',
   description='Module to fetch the arguments',
   author='Vignesh Sundar',
   author_email='vignesh.sundar@cummins.com',
   #packages=find_packages(include=['Pipeline_Builder']),  #same as name
   packages=["config", "resources", "constants_package", "Pipeline_Builder"],
   entry_points={
    'group_1': 'run=Pipeline_Builder.Driver:PipelineBuilder.main'
  },
   install_requires=['uuid', 'databricks-connect'] #external packages as dependencies
)