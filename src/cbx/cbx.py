import zipfile
import rarfile
from natsort import os_sorted
import filetype as filetype


def load_archive(path_archive):
    kind = filetype.guess(path_archive)
    print(kind.extension)
    if kind.extension == "zip":
        return "zip", zipfile.ZipFile(path_archive, "a")
    elif kind.extension == "rar":
        return "rar", rarfile.RarFile(path_archive, 'r')


class Cbx:
    archive = None

    def __init__(self, path_archive):
        (self.extension, self.archive) = load_archive(path_archive)

    def count_folder(self):
        count_folder = 0
        for name in self.archive.namelist():
            if self.archive.getinfo(name).is_dir():
                count_folder = count_folder + 1
        return count_folder

    def load_cover(self):
        cbx = self.archive
        for name in os_sorted(cbx.namelist(), key=str.casefold):
            if not cbx.getinfo(name).is_dir():
                data_image = cbx.open(cbx.getinfo(name))
                kind = filetype.guess(data_image)
                if kind is not None and kind.mime.startswith("image"):
                    return data_image