from dataclasses import dataclass, field
from pathlib import Path
import os
import pickle
import shutil
import bz2
from typing import Any

@dataclass
class Storer:
    __version__ = "0.9.0 [20]"
    internal_name:  str  = "[Storer]"
    dump_name:      str  = "noname"
    path_dumps:     str  = Path(os.path.expanduser(os.path.dirname(__file__)))
    verbose:        bool = False
    data:           dict = field(default_factory=dict)
    default_dir:    str  = "data"
    compressed:     bool = True
    _backup_dir:    str  = "backup"
    _backup_list:   list = field(default_factory=list)

    def __post_init__(self):
        if self.verbose: print(f"[Storer v.{self.__version__ }] is initialized!")
        if self.path_dumps == Path(os.path.expanduser(os.path.dirname(__file__))) or self.path_dumps == "." :
            self.path_dumps = Path(os.path.expanduser(os.path.dirname(__file__))) / "data"
        else: self.path_dumps = Path(self.path_dumps)

        if self.verbose: print(f"Dump folder: [{self.path_dumps}]")
        os.makedirs(self.path_dumps, exist_ok=True)
        self.initialization()  # creating _backup_list
    
    def initialization(self:object) -> None:
        """ Splitting project """
        self._backup_list = [p for p in self.path_dumps.iterdir() if p.is_file()]

    def put(self, what=None, name: str = None) -> None:
        self.data[name] = what

    def get(self, name: str = None) -> Any :
        """
        Get an item from
        """
        if name in self.data: return self.data[name]
        else:
            # no data in current data dict
            # loading it from backup
            self.load()
            # try to give the item again if not return False
            if name in self.data: return self.data[name]
            else: return False

    def dump(self:object, backup:bool = False) -> None:
        if backup: path_dumps = self.path_dumps / self._backup_dir
        else:      path_dumps = self.path_dumps
                    
        if self.verbose: print(self.internal_name, self.path_dumps, self.dump_name, "dumping...")
        
        if not self.compressed:
            with open(path_dumps / (self.dump_name + ".pkl"), 'wb') as f: pickle.dump(self.data, f)
        else:
            with bz2.BZ2File(path_dumps / (self.dump_name + ".pbz2"), 'wb') as f: pickle.dump(self.data, f)

    def load(self:object) -> None:
        if self.verbose: print(self.internal_name, self.path_dumps,  "loading...")
        
        if not self.compressed:
            if os.path.exists(self.path_dumps / (self.dump_name + ".pkl") ):
                with open(self.path_dumps / (self.dump_name + ".pkl"), 'rb') as f: self.data = pickle.load(f)
            else:
                if self.verbose: print(self.internal_name, "No data is available for loading...")
        else:
            if os.path.exists(self.path_dumps / (self.dump_name + ".pbz2") ):
                with open(self.path_dumps / (self.dump_name + ".pbz2"), 'rb') as f: 
                    data = bz2.BZ2File(f, 'rb'); self.data = pickle.load(data)
            else:
                if self.verbose: print(self.internal_name, "No data is available for loading...")
        return self.data

    def show(self, get_string = False) -> Any:
        string = ""
        for name in self.data:
            string += "key: {0:10} | value:  {1:4}; ".format(name, str(self.data[name]))
        if get_string: return string
        else: print(string)
    
    def backup(self:object) -> None:
        """
        Backuping the current dump_name in separate folder [<path_dumps> / backup ]
        """
        if self.verbose: print(f"Backup...")
        os.makedirs(self.path_dumps / self._backup_dir, exist_ok=True)
        self.dump(backup=True)

    def _cleanup(self:object) -> None:
        """
        Cleanup the path_dumps directory fully: including all folders and files. 
        Assuming the folder is used only for Storer purposes.
        """
        if self.verbose: print(f"Cleaning...[{self.path_dumps}]")
        shutil.rmtree(self.path_dumps)
        

if __name__ == "__main__":
    s = Storer(path_dumps=".")
    s.put(what="string", name="mystring")
    s.put(what=1, name="myint")
    s.put(what=[i for i in range(10)],     name="myrange")
    s.put(what={v:v*2 for v in range(10)}, name="mydict")
    s.show()
    s.dump()

    print("\n Now we creating new storer instance...\n")
    s1 = Storer(path_dumps=".", verbose=False)
    s1.load()
    s1.show()

