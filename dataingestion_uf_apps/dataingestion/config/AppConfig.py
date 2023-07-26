from pyhocon import ConfigFactory
import pkg_resources

obj_config = None

def initialize():
    global obj_config 
    #obj_config = ConfigFactory.parse_file("/dbfs/FileStore/python_uf/application.conf")
    file_name = pkg_resources.resource_filename('resources', 'application.conf')
    obj_config = ConfigFactory.parse_file(file_name)

def get_my_config(sPipeline):
    try:
        initialize()
        #return obj_config[sPipeline]
        return obj_config
    except Exception as e:
        print(e)
        raise Exception(e)