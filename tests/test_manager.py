import os
import pytest
import shutil

# Local
from src.manager.manager import Manager

TEST_DIR = 'test_assets/'

@pytest.fixture
def manager():
    return Manager(FILE=f"{TEST_DIR}")

# Limpiar los archivos y directorios después de cada prueba
@pytest.fixture(autouse=True)
def cleanup():
    if os.path.exists(TEST_DIR):
        for file in os.listdir(TEST_DIR):
            file_path = os.path.join(TEST_DIR, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
            else:
                os.rmdir(file_path)
    yield
    # Eliminar directorio de prueba
    if os.path.exists(TEST_DIR):
        shutil.rmtree(TEST_DIR)

def test_create_file(manager):
    filename = os.path.join(f"{TEST_DIR}", 'testfile.txt')
    print(filename,"aaaaa")
    manager.create_file("testfile.txt")

    assert os.path.exists(filename)

def test_read_file(manager):
    filename = os.path.join(TEST_DIR, 'testfile.txt')
    manager.create_file(filename)
    
    try:
        manager.read_file(filename)
    except Exception:
        pytest.fail("read_file lanzó una excepción inesperada")

def test_delete_file(manager):
    filename = os.path.join(TEST_DIR, 'testfile.txt')
    manager.create_file(filename)
    manager.delete_file(filename)

    assert not os.path.exists(filename)

def test_create_directory(manager):
    dirname = os.path.join(f"{TEST_DIR}", 'testdir')
    manager.create_directory("testdir")

    assert os.path.isdir(dirname)

def test_delete_directory(manager):
    dirname = os.path.join(TEST_DIR, 'testdir')
    manager.create_directory(dirname)
    manager.delete_directory(dirname)

    assert not os.path.exists(dirname)

def test_list_directory(manager):
    dirname = os.path.join(f"../{TEST_DIR}", 'testdir')
    manager.create_directory(dirname)
    
    files = manager.list_directory(dirname)
    manager.delete_directory(dirname)
    assert len(files) == 0
