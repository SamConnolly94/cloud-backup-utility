import os


class FileExplorer:
    cloud_backup_dir = None
    project_backup_dir = None
    ignorable_files = None

    directories_to_add_to_cloud = []
    files_to_add_to_cloud = None

    def __init__(self, cloud_backup_dir, project_backup_dir, ignorable_files):
        self.cloud_backup_dir = cloud_backup_dir
        self.project_backup_dir = project_backup_dir
        self.ignorable_files = ignorable_files

    def populate_backup_lists(self, path_extension):
        folders_to_create = list()
        path_extension += "/"
        sub_directories = [f.path for f in os.scandir(self.project_backup_dir + path_extension) if f.is_dir()]

        cloud_subdirectories = []
        if os.path.isdir(self.cloud_backup_dir + path_extension):
            cloud_subdirectories = [f.path for f in os.scandir(self.cloud_backup_dir + path_extension) if f.is_dir()]

        for directory in sub_directories:
            directory_name = os.path.split(directory)[1]
            if directory_name not in [os.path.split(f)[1] for f in cloud_subdirectories] \
                    and path_extension + directory_name + "/" not in self.ignorable_files:
                current_folder = os.path.join(path_extension, directory_name)
                folders_to_create.append(current_folder)
                self.populate_backup_lists(current_folder)
        self.directories_to_add_to_cloud.append(folders_to_create)
        print(self.directories_to_add_to_cloud)
