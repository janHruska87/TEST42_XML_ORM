import datetime

from storm.properties import Unicode, Int


class TestCaseEntry:
    __storm_table__ = "testCaseEntry"
    id = Int(primary=True)
    indexAttribute = Int()
    textAttribute = Unicode()
    testCaseId = Unicode()
    updatedDate = Unicode(default=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
    pass