import os

FILE_ROOT = 'assets/'

class Manager:
    def __init__(self, FILE=None):
        self.file_path = FILE if FILE else FILE_ROOT
        os.makedirs(self.file_path, exist_ok=True)

    def _resolve_path(self, path):
        return os.path.join(self.file_path, path)

    def create_file(self, filename):
        path = self._resolve_path(filename)
        print(filename)
        try:
            with open(path, 'w') as f: 
                print(f"Archivo '{path}' creado con éxito.")
        except Exception as e:
            print(f"Error al crear el archivo: {e}")

    def read_file(self, filename):
        path = self._resolve_path(filename)
        try:
            with open(path, 'r') as f:
                content = f.read()
                print(content)
        except FileNotFoundError:
            print(f"Error: El archivo '{path}' no existe.")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

    def delete_file(self, filename):
        path = self._resolve_path(filename)
        try:
            os.remove(path)
        except FileNotFoundError:
            print(f"Error: El archivo '{path}' no existe.")
        except Exception as e:
            print(f"Error al eliminar el archivo: {e}")

    def create_directory(self, dirname):
        path = self._resolve_path(dirname)
        try:
            os.makedirs(path, exist_ok=True)
        except Exception as e:
            print(f"Error al crear el directorio: {e}")

    def delete_directory(self, dirname):
        path = self._resolve_path(dirname)
        try:
            os.rmdir(path)
        except FileNotFoundError:
            print(f"Error: El directorio")

    def list_directory(self, dirname):
        path = self._resolve_path(dirname)
        try:
            files = os.listdir(path)
            print(f"Contenido del directorio '{path}':")
            return files
        except FileNotFoundError:
            print(f"Error: El directorio '{path}' no existe.")
        except Exception as e:
            print(f"Error al listar el directorio: {e}")
