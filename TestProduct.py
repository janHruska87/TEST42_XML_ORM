import datetime

from storm.database import create_database
from storm.properties import Int, Unicode
from storm.store import Store


class TestProduct:
    __storm_table__="testProduct"
    id = Int(primary=True)
    name = Unicode()
    testCaseId = Int()
    updatedDate = Unicode(default=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
