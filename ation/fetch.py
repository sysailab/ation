from pyevsim.behavior_model_executor import BehaviorModelExecutor
from pyevsim.system_message import SysMessage
from pyevsim.definition import *

class FetchModel(BehaviorModelExecutor):
    def __init__(self, instance_time, destruct_time, name, engine_name):
        BehaviorModelExecutor.__init__(self, instance_time, destruct_time,
                                       name, engine_name)
        

    def ext_trans(self, port, msg):
        #실선
        pass

    def output(self):

        pass

    def int_trans(self):
        #점선
        if self._cur_state == "WORK_CHECK":
            self._cur_state = "IDLE"
