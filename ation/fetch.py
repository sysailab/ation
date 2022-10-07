from pyevsim.behavior_model_executor import BehaviorModelExecutor
from pyevsim.system_message import SysMessage
from pyevsim.definition import *

class FetchModel(BehaviorModelExecutor):
    def __init__(self, instance_time, destruct_time, name, engine_name):
        BehaviorModelExecutor.__init__(self, instance_time, destruct_time,
                                       name, engine_name)

        self.init_state("IDLE")
        self.insert_state("IDLE", Infinite)
        self.insert_state("WORK_CHECK", 0)

        self.insert_input_port("info")
        self.recv_info = None

    def ext_trans(self, port, msg):
        #실선
        if port == "info":
            info = msg.retrieve()[0]

            if info[0] == self.hid:
                self._cur_state = "WORK_CHECK"
                self.recv_info = info[1]
            else:
                self._cur_state = self._cur_state
    def output(self):

        if self.recv_info == "blue":
            #print(f"\n?blue: {datetime.datetime.now()}")
            self.health_obj.human.health_score = self.health_obj.assess_health(
                "blue")
            #print(f"\nHuman[{self.hid}]!blue - > rest")
        elif self.recv_info == "red":
            #print("\n?red")
            self.health_obj.human.health_score = self.health_obj.assess_health(
                "red")
            #print(f"\nHuman[{self.hid}]red - > rest")

    def int_trans(self):
        #점선
        if self._cur_state == "WORK_CHECK":
            self._cur_state = "IDLE"
