from pyevsim import BehaviorModelExecutor
from pyevsim import SysMessage
from pyevsim.definition import *

class InsertModel(BehaviorModelExecutor):
    def __init__(self, instance_time, destruct_time, name, engine_name, db, col_name, validation_rule):
        BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name, engine_name)

        self.init_state("IDLE")
        self.insert_state("IDLE", Infinite)

        self.insert_input_port("info")
        self.insert_output_port("result")

        self.db = db
        self.collection = col_name
        self.query = validation_rule

    def ext_trans(self,port, msg):
        if port == self.info:
            collection = msg.retrieve()

            for item in collection:
                # check item type
                # item should be dictionary
                res = self.db[self.collection].insert_one(item)
            pass

    def output(self):
        return None
        
    def int_trans(self):
        if self._cur_state == "IDLE":
            self._cur_state = "IDLE"

class UpdateModel(BehaviorModelExecutor):
    pass


class Generator(BehaviorModelExecutor):
    def __init__(self, instance_time, destruct_time, name, engine_name):
        BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name, engine_name)

        self.init_state("IDLE")
        self.insert_state("IDLE", Infinite)
        self.insert_state("MOVE", 1)

        self.insert_input_port("start")
        self.insert_output_port("data")

        self.msg_list = [{"degree":"phd", "alias":"BakSaRi", "name":"jaiyun lee"},
                         {"degree":"phd", "alias":"1130K", "name":"seyoung han"},
                         {"degree":"ms", "alias":"ceo", "name":"kyusik ham"}, ]

    def ext_trans(self,port, msg):
        if port == "start":
            self._cur_state = "MOVE"

    def output(self):
        msg = SysMessage(self.get_name(), "data")
        msg.insert(self.msg_list.pop(0))
        return msg
        
    def int_trans(self):
        if self._cur_state == "MOVE" and not self.msg_list:
            self._cur_state = "IDLE"
        else:
            self._cur_state = "MOVE"