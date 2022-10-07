from pyevsim.behavior_model_executor import BehaviorModelExecutor
from pyevsim.system_message import SysMessage
from pyevsim.definition import *

import pprint

class FetchModel(BehaviorModelExecutor):
    def __init__(self, instance_time, destruct_time, name, engine_name, fetch_freq, db, col_name, query):
        BehaviorModelExecutor.__init__(self, instance_time, destruct_time,
                                       name, engine_name)

        self.init_state("IDLE")
        self.insert_state("IDLE", Infinite)
        self.insert_state("FETCH", fetch_freq)

        self.insert_input_port("start")
        self.insert_input_port("stop")

        self.insert_output_port("info")
        
        self.db = db
        self.collection = col_name
        self.query = query

    def ext_trans(self, port, msg):
        if port == "start":
            self._cur_state = "FETCH"
        elif port == "stop":
            self._cur_state = "IDLE"
            pass
    
    def output(self):
        cursor = self.db[self.collection].find(self.query)
        msg = SysMessage(self.get_name(), self.info)

        for document in cursor:
            msg.insert(document)
        return msg

    def int_trans(self):
        #점선
        if self._cur_state == "Fetch":
            self._cur_state = "Fetch"

    # Utility Functions
    def set_collection(self, col_name):
        self.collection = col_name

    def get_collection(self):
        return self.collection

'''
class FetchMongoModel(FetchModel):
    def __init__(self, instance_time, destruct_time, name, engine_name, fetch_freq, db, col_name, query):
        FetchModel.__init__(self, instance_time, destruct_time,
                                       name, engine_name, fetch_freq)

    def output(self):
        msg = SysMessage(self.get_name(), self.info)

        cursor = self.db[self.collection].find(self.query)
        for document in cursor:
            msg.insert(document)
        return msg
'''