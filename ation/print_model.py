from pyevsim.behavior_model_executor import BehaviorModelExecutor
from pyevsim.system_message import SysMessage
from pyevsim.definition import *

import pprint

class PrintModel(BehaviorModelExecutor):
    def __init__(self, instance_time, destruct_time, name, engine_name):
        BehaviorModelExecutor.__init__(self, instance_time, destruct_time,
                                       name, engine_name)

        self.init_state("IDLE")
        self.insert_state("IDLE", Infinite)

        self.insert_input_port("info")

    def ext_trans(self, port, msg):
        if port == self.info:
            data = msg.retrieve()

            for item in data:
                pprint.pprint(item)
            print("--------")
    
    def output(self):
        return None

    def int_trans(self):
        #점선
        if self._cur_state == "IDLE":
            self._cur_state = "IDLE"
