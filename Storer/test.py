import unittest

import os
from Storer import Storer
import shutil

PATH_DUMPS        = "./data/"
PATH_DUMPS_BACKUP = PATH_DUMPS + "backup/"
DUMP_NAME         = "test_case"


class TestInitialization(unittest.TestCase):
    def test_creating_pkl(self):
        """
        Test paths of the created instance (PKL)
        """
        s = Storer(path_dumps=PATH_DUMPS, dump_name=DUMP_NAME, verbose=False, compressed=False)
        s.put(1, name="one")
        s.dump()
        assert os.path.exists(os.path.expanduser(PATH_DUMPS) + DUMP_NAME + ".pkl")
        s._cleanup()

    def test_creating_pbz2(self):
        """
        Test paths of the created instance (PBZ2)
        """
        s = Storer(path_dumps=PATH_DUMPS, dump_name=DUMP_NAME, verbose=False)
        s.put(1, name="one")
        s.dump()
        assert os.path.exists(os.path.expanduser(PATH_DUMPS) + DUMP_NAME + ".pbz2")
        s._cleanup()
    
    def test_backup_dumb_pkl(self):
        """
        Test backup creating
        """
        s = Storer(path_dumps=PATH_DUMPS, dump_name=DUMP_NAME, verbose=False, compressed=False)
        s.put(1, name="one")
        s.backup()
        assert os.path.exists(os.path.expanduser(PATH_DUMPS_BACKUP) + DUMP_NAME + ".pkl")
        s._cleanup()
    
    def test_backup_dumb_pbz2(self):
        """
        Test backup creating
        """
        s = Storer(path_dumps=PATH_DUMPS, dump_name=DUMP_NAME, verbose=False,)
        s.put(1, name="one")
        s.backup()
        assert os.path.exists(os.path.expanduser(PATH_DUMPS_BACKUP) + DUMP_NAME + ".pbz2")
        s._cleanup()
    
    def test_get_item_pkl(self):
        """
        Test get item procedure
        """
        s = Storer(path_dumps=PATH_DUMPS, dump_name=DUMP_NAME, verbose=False, compressed=False)
        s.put(1, name="one")
        s.put(2, name="two")
        three = s.get("three")
        assert three == False #  "Should be False!"
        s.put(3, name="three")
        s.dump()
        # here is new data in storer
        three = s.get("three")
        assert three == 3  # "Should be 3!"
        s._cleanup()
    
    def test_get_item_bpz2(self):
        """
        Test get item procedure
        """
        s = Storer(path_dumps=PATH_DUMPS, dump_name=DUMP_NAME, verbose=False)
        s.put(1, name="one")
        s.put(2, name="two")
        three = s.get("three")
        assert three == False #  "Should be False!"
        s.put(3, name="three")
        s.dump()
        # here is new data in storer
        three = s.get("three")
        assert three == 3  # "Should be 3!"
        s._cleanup()
    
    def test_initialization_pkl(self):
        """
        Test initialization procedure
        Expected one backup file after dump procedure
        """
        s = Storer(path_dumps=PATH_DUMPS, dump_name=DUMP_NAME, verbose=False, compressed=False)
        s.put(1, name="one")
        s.dump()
        s2 = Storer(path_dumps=PATH_DUMPS, dump_name=DUMP_NAME, verbose=False, compressed=False)
        one = len(s2._backup_list)
        assert one == 1
        s._cleanup()
    
    def test_initialization_pbz2(self):
        """
        Test initialization procedure
        Expected one backup file after dump procedure
        """
        s = Storer(path_dumps=PATH_DUMPS, dump_name=DUMP_NAME, verbose=False)
        s.put(1, name="one")
        s.dump()
        s2 = Storer(path_dumps=PATH_DUMPS, dump_name=DUMP_NAME, verbose=False)
        one = len(s2._backup_list)
        assert one == 1
        s._cleanup()

if __name__ == "__main__":
    unittest.main()
