import datetime
import os

from storm.database import create_database
from storm.properties import Int, Unicode
from storm.store import Store


class TestCase:
    __storm_table__ ="testCase"
    id = Int(primary=True)
    id_t42 = Unicode()
    t42ObjectId = Unicode()
    t42ObjectVersionId = Unicode()
    name = Unicode()
    version = Unicode()
    creationDate = Unicode()
    doorsId = Unicode()
    automation = Unicode()
    testObjectCategory = Unicode()
    testType = Unicode()
    testDepth = Unicode()
    specialFeature = Unicode()
    testEnvironmentTypes = Unicode()
    updatedDate = Unicode(default=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))


