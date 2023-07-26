from setuptools import setup, find_packages

setup(
   name='uf_package',
   version='1.0',
   description='Package with UF functionalities',
   author='Vignesh Sundar',
   author_email='vignesh.sundar@cummins.com',
   packages=['audit_package', 'io_package'],  #same as name
   entry_points={
    'group_1': 'run=io_package.io_module:LoggerProvider'
  },
   install_requires=['uuid', 'databricks-connect'], #external packages as dependencies
)