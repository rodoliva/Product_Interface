import pickle
import datetime
import openpyxl as o
import copy

min_prod_id, max_prod_id= 1000, 2000
prod_dir, prod_bck= 'Database/configp.dta', 'Backup/backupp.bkp'

def notemp(st):
    if st == "":
        return False
    return True

def isnum(num):
    try:
        num+1
        return True
    except TypeError:
        return False

def check_id(id, min, max):
    if isnum(id) and int(min) <= id < int(max):
        return True
    return False

def check_dup_id(id, li):
    if not li == []:
        for p in li:
            if p.id == id:
                return False
    return True

def prod_type(li):
    ptype = []
    for product in li:
        ptype.append(product.prod_type)
    return list(dict.fromkeys(ptype).keys())

class BaseData():

    def __init__(self, id, name, min, max, directory):

        if check_id(id, min, max):
            self.__id, self.min, self.max = int(id), int(min), int(max)
        else:
            raise TypeError

        if notemp(name) and notemp(directory):
            self.name, self.directory = name, directory
        else:
            raise TypeError
        self.all_freight = {}

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, data):
            self.__id = data

    def update(self, mod, data):
        # mod = id, name
        if mod == 'id':
            self.id = data
        elif mod == 'name' and notemp(data):
            self.name = data

class Product(BaseData):

    def __init__(self, id, name, short_name, prod_type, reference_price):

        super().__init__(id, name, min_prod_id, max_prod_id, prod_dir)

        if notemp(short_name) and notemp(prod_type) and notemp(reference_price):
            self.short_name, self.prod_type, self.reference_price = short_name, prod_type, reference_price
        else:
            raise TypeError

    def update(self, mod, data):
        # mod = (id, name, short_name, prod_type,reference_price)
        if mod == 'id' or mod == 'name':
            super().update(mod, data)
        elif notemp(data):
            if mod == 'short_name':
                self.short_name = data
            elif mod == 'prod_type':
                self.prod_type = data
            elif mod == 'reference_price':
                self.reference_price = data

class UndoRedoManager(object):

    def __init__(self, li):
        self.undo_list = []
        self.undo_list.append(li)
        self.redo_list = []

    def push_undo_command(self, action):  # function for do_new_action function
        self.undo_list.append(action)

    def pop_undo_command(self):  # function for undo function
        if not len(self.undo_list) <= 1:
            last_undo = self.undo_list.pop()
            return last_undo

    def push_redo_command(self, action):  # function for undo function
        self.redo_list.append(action)

    def pop_redo_command(self):
        if not len(self.redo_list) == 0:
            last_redo = self.redo_list.pop()  # function for undo function
            return last_redo

    def do_new_action(self, action):  # use this function for each action
        self.redo_list = []  # clear redo with every new command
        self.push_undo_command(action)  # add new element

    def undo(self):  # function undo
        if not len(self.undo_list) <= 1:
            action = self.pop_undo_command()
            self.push_redo_command(action)
            return self.clone_li(self.undo_list[len(self.undo_list) - 1])
        else:
            return self.clone_li(self.undo_list[0])

    def redo(self):  # function redo
        if not len(self.redo_list) == 0:
            action = self.pop_redo_command()
            self.push_undo_command(action)
            return self.clone_li(action)
        else:
            return self.clone_li(self.undo_list[len(self.undo_list) - 1])


    def clone_li(self, li):
        auxli = []
        if not li == []:
            copyli = copy.deepcopy(li)
            for prod in copyli:
                auxli.append(copy.deepcopy(prod))
            return auxli

def openerli(directory):
    li = []
    try:
        with open(directory, 'rb') as input:
            li = pickle.load(input)
            input.close()
            return li
    except FileNotFoundError or ModuleNotFoundError:
        return li

def openerback(directory):
    li = []
    try:
        with open(directory, 'rb') as input:
            li = pickle.load(input)
            return li
    except FileNotFoundError:
        return li

def save_data(dir, bck, li):
    saverli(dir, li)
    saverback(bck, li)

def saverli(directory, li):
    with open(directory, 'wb') as output:
        pickle.dump(li, output, pickle.HIGHEST_PROTOCOL)
        output.close()

def saverback(directory, back):
    li = []
    try:
        li = openerback(directory)
        li.append([back, datetime.datetime.now()])
        li.sort(key=lambda x: x[1], reverse=True)
        with open(directory, 'wb') as output:
            pickle.dump(li, output, pickle.HIGHEST_PROTOCOL)
    except FileNotFoundError:
        li.append([back, datetime.datetime.now()])
        li.sort(key=lambda x: x[1], reverse=True)
        with open(directory, 'wb') as output:
                pickle.dump(li, output, pickle.HIGHEST_PROTOCOL)

def open_excel(name):
    wb = o.load_workbook(name)
    ws = wb.active
    li = []
    for row in ws.values:
        aux = []
        for value in row:
            aux.append(value)
        li.append(aux)
    li.pop(0)
    return li
