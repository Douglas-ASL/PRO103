import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Definindo o caminho do diretório para rastrear alterações
from_dir = "<Defina o caminho para rastrear eventos do sistema de arquivos>"

# Classe para lidar com eventos do sistema de arquivos
class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Arquivo/Diretório criado: {event.src_path}")
    
    def on_modified(self, event):
        print(f"Arquivo/Diretório modificado: {event.src_path}")
    
    def on_moved(self, event):
        print(f"Arquivo/Diretório movido/renomeado de {event.src_path} para {event.dest_path}")
    
    def on_deleted(self, event):
        print(f"Arquivo/Diretório excluído: {event.src_path}")

# Criando o observer
event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, path=from_dir, recursive=True)
observer.start()

# Aguardando a entrada do usuário para parar o observer
try:
    print("Pressione qualquer tecla para sair...")
    while True:
        if sys.stdin.read(1):
            break
except KeyboardInterrupt:
    observer.stop()

observer.join()
