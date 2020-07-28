import tkinter
from tkinter import *


class CloudBackupWindowFactory:
    backup_ignore_file_label = None
    backup_ignore_file_button = None
    project_directory_label = None
    project_directory_button = None
    cloud_directory_label = None
    cloud_directory_button = None

    def get_window(self, window_manager):
        width = 800
        height = 800
        window_resolution = str(width) + "x" + str(height)
        x = 100
        y = 100
        window_position = str(x) + "+" + str(y)
        window = tkinter.Tk()

        window.geometry(window_resolution + "+" + window_position)
        window.title("Unity GDrive Backup")
        self.create_gui_elements(window, window_manager)
        return window

    def create_gui_elements(self, window, window_manager):
        google_drive_row = 1
        data_initial_column = 0
        button_offset = 1

        # Cloud
        self.cloud_directory_label = Label(window,
                                           text="Cloud backup folder",
                                           fg="blue",
                                           justify=LEFT)
        self.cloud_directory_label.grid(column=data_initial_column, row=google_drive_row)

        self.cloud_directory_button = Button(window,
                                             text="Browse Files",
                                             command=window_manager.select_cloud_dir)
        self.cloud_directory_button.grid(column=data_initial_column + button_offset, row=google_drive_row)

        # Project
        project_row = 3
        self.project_directory_label = Label(window,
                                             text="Project folder",
                                             fg="blue",
                                             justify=LEFT)
        self.project_directory_label.grid(column=data_initial_column, row=project_row)

        self.project_directory_button = Button(window,
                                               text="Browse Files",
                                               command=window_manager.select_project_dir)
        self.project_directory_button.grid(column=data_initial_column + button_offset, row=project_row)

        # Backup ignore
        backup_ignore_row = 5
        self.backup_ignore_file_label = Label(window,
                                              text="Backup ignore file",
                                              fg="blue",
                                              justify=LEFT)
        self.backup_ignore_file_label.grid(column=data_initial_column, row=backup_ignore_row)

        self.backup_ignore_file_button = Button(window,
                                                text="Browse Files",
                                                command=window_manager.select_backup_ignore_file)
        self.backup_ignore_file_button.grid(column=data_initial_column + button_offset, row=backup_ignore_row)
