import os
import threading
import time
from tkinter import filedialog
from CloudBackupWindowFactory import CloudBackupWindowFactory
from FileExplorer import FileExplorer


class CloudBackupWindow:
    # Constants
    BACKUP_INTERVAL = 5

    # Vars
    cloud_backup_dir = None
    project_dir = None
    backup_ignore_contents = None
    file_explorer = None

    def __init__(self):
        window_factory = CloudBackupWindowFactory()
        window = window_factory.get_window(self)
        backup_thread = threading.Thread(target=self.process_backups, args=(), daemon=True)
        backup_thread.start()
        window.mainloop()

    def process_backups(self):
        while True:
            time.sleep(self.BACKUP_INTERVAL)
            if self.ready_to_backup():
                print("Cloud backup dir: " + self.cloud_backup_dir)
                print("Project dir: " + self.project_dir)
            else:
                print("Waiting for directories to be set before backing up")

    def ready_to_backup(self):
        return self.project_dir is not None \
               and self.cloud_backup_dir is not None \
               and self.project_dir != self.cloud_backup_dir \
               and self.backup_ignore_contents is not None \
               and len(self.backup_ignore_contents) != 0

    def perform_initial_backup(self):
        if self.ready_to_backup():
            self.file_explorer = FileExplorer(cloud_backup_dir=self.cloud_backup_dir,
                                              project_backup_dir=self.project_dir,
                                              ignorable_files=self.backup_ignore_contents)
            self.file_explorer.populate_backup_lists("")

    def select_cloud_dir(self):
        self.cloud_backup_dir = filedialog.askdirectory()
        self.perform_initial_backup()

    def select_project_dir(self):
        self.project_dir = filedialog.askdirectory()
        if os.path.exists(self.project_dir + "/.backupignore"):
            with open(self.project_dir + "/.backupignore", "r") as f:
                self.backup_ignore_contents = self.parse_backupignore(f.read())
                print("Backupignore file was located in same directory as project.")
        self.perform_initial_backup()

    def select_backup_ignore_file(self):
        default_dir = "/"
        if self.project_dir is not None:
            default_dir = self.project_dir
        with filedialog.askopenfile(mode="r", initialdir=default_dir, title="Select .backupignore file",
                                    filetypes=(("backupignore files", "*.backupignore"), ("all files", "*.*"))) as f:
            self.backup_ignore_contents = self.parse_backupignore(f.read())
        self.perform_initial_backup()

    @staticmethod
    def parse_backupignore(contents):
        return list(filter(lambda a: a != "", contents.split("\n")))
