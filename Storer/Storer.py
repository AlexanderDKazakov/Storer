import os
import pickle

class Storer:
    def __init__(self, name4file=None, path4dumbs=None, internal_name=None, verbose=True):
        __version__ = "0.0.7 [13]"
        self.internal_name = "[Storer]"
        self.name4file = "noname.pkl"
        self.path4dumbs = os.path.expanduser(os.path.dirname(__file__))
        self.data = dict()
        self.verbose = verbose

        if internal_name: self.internal_name = "[" + str(internal_name) + "]"
        if name4file: self.name4file = str(name4file)
        if path4dumbs:
            self.path4dumbs = str(path4dumbs)
            if self.path4dumbs[-1] != "/": self.path4dumbs += "/"
            self.path4dumbs = os.path.expanduser(self.path4dumbs)
            os.makedirs(self.path4dumbs, exist_ok=True)
        if self.verbose: print(f"[Storer v.{__version__ }] is initialized!")

    def put(self, what=None, name: str = None) -> None:
        self.data[name] = what

    def get(self, name: str = None):
        if name in self.data: return self.data[name]
        else: return False

    def dumb(self):
        if self.verbose: print(self.internal_name, self.path4dumbs + self.name4file + " dumping...")
        with open(self.path4dumbs + self.name4file, 'wb') as f:
            pickle.dump(self.data, f)

    def load(self):
        if self.verbose: print(self.internal_name, self.path4dumbs + self.name4file + " loading...")
        if os.path.exists(self.path4dumbs + self.name4file):
            with open(self.path4dumbs + self.name4file, 'rb') as f:
                     self.data = pickle.load(f)
        else:
            if self.verbose: print(self.internal_name, "No data is available for loading...")
        return self.data

    def show(self, get_string = False):
        string = ""
        for name in self.data:
            string += "key: {0:10} | value:  {1:4}; ".format(name, str(self.data[name]))
        if get_string: return string
        else: print(string)

if __name__ == "__main__":
    s = Storer(path4dumbs='./test')
    s.put(what="string", name="mystring")
    s.put(what=1, name="myint")
    s.put(what=[i for i in range(10)], name="myrange")
    s.put(what={v:v*2 for v in range(10)}, name="mydict")
    s.show()
    s.dumb()

    print("\n Now we creating new storer instance...\n")
    s1 = Storer(internal_name="Storer1", path4dumbs='./test', verbose=False)
    s1.load()
    s1.show()

