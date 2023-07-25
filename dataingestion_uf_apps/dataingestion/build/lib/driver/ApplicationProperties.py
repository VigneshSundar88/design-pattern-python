import sys

class ApplicationProperties:
    DATASOURCE, LAYER, PIPELINE = []
    BATCH_LIMIT, INTERVAL, START_POSITION = ""
    TABLE_NAME = ""
    
    sPipeline = ""
    sessionName = ""
    env = sys.env.get().get.toUpperCase()

    def __init__(self, *args) -> None:
        self.input_args = args

    def parse_args(self):
        if len(self.input_args) == 0:
            raise Exception("Incorrect Arguments passed!!!")
        
        for arg_val in self.input_args:
            args_split = arg_val.split("=")

            pref_arg = args_split[0]
            posf_arg = list(map(lambda x: x.upper(), args_split[1].split(",")))

            if pref_arg == "datasource":
                DATASOURCE = posf_arg
            elif pref_arg == "layer":
                LAYER = posf_arg
            elif pref_arg == "pipeline":
                PIPELINE = posf_arg
            elif pref_arg == "tablename":
                TABLE_NAME = posf_arg
            elif pref_arg == "batch_limit":
                BATCH_LIMIT = posf_arg
            elif pref_arg == "interval":
                INTERVAL = posf_arg
            elif pref_arg == "start_position":
                START_POSITION = posf_arg
            else:
                raise Exception("Value does not match with any argument key!!!")

    # Stop if mandatory parameters are not passed
    if len(DATASOURCE) == 0 or len(LAYER) == 0 or len(PIPELINE) == 0:
        raise Exception("Mandatory parameters should be passed!!!")
            