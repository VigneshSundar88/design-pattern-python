from pyhocon import ConfigFactory

obj_config = None

def initialize():
    global obj_config 
    obj_config = ConfigFactory.parse_file("/dbfs/FileStore/python_uf/application.conf")

def get_my_config(sPipeline):
    try:
        initialize()
        #return obj_config[sPipeline]
        return obj_config
    except Exception as e:
        print(e)
        raise Exception(e)