from io_package import io_module

class audit_logger:
    def __init__(self, **kwargs):
        self._class_name = kwargs.get("class_name", "")
        self._obj_config = kwargs.get("obj_config", "")
        self.spark = kwargs.get("spark", "")
        audit_logger_obj = audit_logger
        self.logger = io_module.LoggerProvider.get_logger(self.spark, audit_logger_obj.__class__.__name__)

    @property
    def class_name(self):
        self.logger.info(f"Get class name in {self._class_name}")
        return self._class_name

    @property
    def obj_config(self):
        self.logger.info(f"Get Job Config in {self._obj_config}")
        return self._obj_config

    # @class_name.setter
    # def class_name(self):
    #     self._class_name

    # @obj_config.setter
    # def obj_config(self):
    #     self._obj_config