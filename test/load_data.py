from pyevsim.system_simulator import SystemSimulator
from pyevsim.definition import *
from instance.config import MONGODB_URL
import pprint

import motor.motor_asyncio
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client["simulverse"]

async def do_check(db, collections:list):
    for item in collections:
        print(f"============= {item}")
        cursor = db[item].find({})
        for document in await cursor.to_list(length=100):
            pprint.pprint(document)

ss = SystemSimulator()
engine = ss.register_engine("load_test", "REAL_TIME", 0.1)

loop = client.get_io_loop()
loop.run_until_complete(do_check(db, ['users', 'space', 'scenes', 'links']))