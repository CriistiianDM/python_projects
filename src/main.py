import os
import argparse

# Local Librarys
from manager.manager import Manager
from cli.cli import CLI

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Gestor de archivos')

    parser.add_argument('action', type=str, help="Acción a realizar")
    parser.add_argument('target', type=str, help="Nombre del archivo o directorio objetivo")

    args = parser.parse_args()


    manager = Manager()
    cli = CLI(manager)

    cli.execute(args.action, args.target)