from pyevsim import BehaviorModelExecutor
from pyevsim import SysMessage
from pyevsim.definition import *
import datetime
class Generator(BehaviorModelExecutor):
    def __init__(self, instance_time, destruct_time, name, engine_name):
        BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name, engine_name)

        self.init_state("IDLE")
        self.insert_state("IDLE", Infinite)
        self.insert_state("MOVE", 1)

        self.insert_input_port("start")
        self.insert_output_port("process")
        self.msg_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def ext_trans(self,port, msg):
        if port == "start":
            print(f"[{self.get_name()}][IN]: {datetime.datetime.now()}")
            self._cur_state = "MOVE"

    def output(self):
        msg = SysMessage(self.get_name(), "process")
        print(f"[{self.get_name()}][OUT]: {datetime.datetime.now()}")
        msg.insert(self.msg_list.pop(0))
        return msg
        
    def int_trans(self):
        if self._cur_state == "MOVE" and not self.msg_list:
            self._cur_state = "IDLE"
        else:
            self._cur_state = "MOVE"