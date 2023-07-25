import os
import re

class ApplicationProperties:
    DATASOURCE = []
    LAYER = []
    PIPELINE = []
    BATCH_LIMIT = ""
    INTERVAL = ""
    START_POSITION = ""
    TABLE_NAME = ""

    sPipeline = ""
    sessionName = ""
    ENV = os.environ["env"]

    def __init__(self, *args) -> None:
        self.input_args = args[0]

    def parse_args(self):
        if len(self.input_args) == 0:
            raise Exception("Incorrect Arguments passed!!!")
        
        for arg_val in self.input_args[1:]:
            print("arg_val: "+arg_val)
            final_arg = re.sub(r'[^\w=]', '', arg_val)
        
            args_split = final_arg.split("=")

            pref_arg = args_split[0]
            
            posf_arg = list(map(lambda x: x.upper(), args_split[1].split(",")))

            if pref_arg == "datasource":
                self.DATASOURCE = posf_arg
            elif pref_arg == "layer":
                self.LAYER = posf_arg
            elif pref_arg == "pipeline":
                self.PIPELINE = posf_arg
            elif pref_arg == "tablename":
                self.TABLE_NAME = posf_arg
            elif pref_arg == "batch_limit":
                self.BATCH_LIMIT = posf_arg
            elif pref_arg == "interval":
                self.INTERVAL = posf_arg
            elif pref_arg == "start_position":
                self.START_POSITION = posf_arg
            else:
                raise Exception("Value does not match with any argument key!!!")
            