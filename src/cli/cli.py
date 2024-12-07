import argparse
from manager.manager import Manager

class CLI:
    def __init__(self, manager):
        self.manager = manager

    def execute(self, action, target):
        try:
            actions = {
                'create_file': self.manager.create_file,
                'read_file': self.manager.read_file,
                'delete_file': self.manager.delete_file,
                'create_directory': self.manager.create_directory,
                'delete_directory': self.manager.delete_directory,
                'list_directory': self.manager.list_directory,
            }

            if action in actions:
                actions[action](target)
            else:
                print(f"Acción '{action}' no válida.")
        except Exception as e:
            print(f"Error al ejecutar la acción '{action}': {e}")