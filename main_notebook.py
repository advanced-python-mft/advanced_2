import json
import os

class Note:
    def __init__(self, id, title, context):
        self.id = id
        self.title = title
        self.context = context

class Repository:
    def __init__(self):
        self.json_name = 'notes.json'
        self.notebook = None
        self.create()
        self.note = Note()

    def create(self):
        if not os.path.exists(self.json_name):    
            with open(self.json_name, 'w') as f:
                json.dump({'0':'23'}, f)

        with open('notes.json') as f:
            self.notebook = json.load(f)

    def get_all(self):
        pass

    def get_by_id(self, id):
        pass

    def save_file(self):
        pass

class View:
    def __init__(self):
        pass
    def show_all(self):
        pass
    def get_command(self):
        command = input('ye chi bede')

class Notebook:
    def __init__(self):
        self.repo = Repository()
        self.view = View()
        
    def run(self):
        while True:
            self.view.get_command()

class Notebooks:
    pass

if __name__ == '__main__':
    nb = Notebook()
    nb.run()
