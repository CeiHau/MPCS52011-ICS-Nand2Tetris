class Row:
    def __init__(self, name, type, kind, num):
        self.name = name
        self.type = type
        self.kind = kind
        self.num = num


class SymbolTable:
    static_num = 0
    static_rows = {}

    def __init__(self):
        self.table = {}
        self.nums = {
            "static": self.static_num,
            "filed": 0,
            "argument": 0,
            "local": 0
        }

    def add(self, name, type, kind):
        num = self.nums[kind]
        self.nums[kind] += 1
        r = Row(name, type, kind, num)
        if kind != 'static':
            self.table[name] = r
        else:
            self.static_rows[name] = r

    def new_scope(self):
        self.table = {}
        self.nums['argument'] = 0
        self.nums['local'] = 0

    def get_num(self, kind):
        return self.nums[kind]

    def get_row(self, name):
        if name in self.static_rows.keys():
            return self.static_rows[name]
        elif name in self.table.keys():
            return self.table[name]
        else:
            return None

