import context

from pyevsim.behavior_model_executor import BehaviorModelExecutor
from pyevsim.system_simulator import SystemSimulator
from pyevsim.definition import *
from instance.config import MONGODB_URL

from ation.fetch_model import FetchModel
from ation.print_model import PrintModel
import pymongo


client = pymongo.MongoClient(MONGODB_URL)
db = client["simulverse"]

ss = SystemSimulator()
engine = ss.register_engine("load_test", "REAL_TIME", 0.1)
fm = FetchModel(0, Infinite, 'fm', "load_test", 3, db, "users", {})
pm = PrintModel(0, Infinite, 'fm', "load_test")

engine.register_entity(fm)
engine.register_entity(pm)

engine.insert_input_port("start")
engine.coupling_relation(None, engine.start, fm, fm.start)
engine.coupling_relation(fm, fm.info, pm, pm.info)

engine.insert_input_port("stop")
engine.coupling_relation(None, engine.stop, fm, fm.stop)

engine.insert_external_event(engine.start, None)
engine.simulate()

#loop = client.get_io_loop()
#loop.run_until_complete(do_check(db, ['users', 'space', 'scenes', 'links']))