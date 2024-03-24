from bot.helper.ext_utils.bot_utils import MirrorStatus, get_readable_file_size, get_readable_time
from bot.helper.ext_utils.fs_utils import get_path_size
from time import time

class MetadataStatus:
    def __init__(self, name, size, listener):
        self.__name = name
        self.__size = size
        self.__listener = listener
        self.__start_time = time()

    def speed_raw(self):
        return self.processed_raw() / (time() - self.__start_time)

    def progress_raw(self):
        try:
            return self.processed_raw() / self.__size * 100
        except ZeroDivisionError:
            return 0

    def progress(self):
        return f'{round(self.progress_raw(), 2)}%'

    def speed(self):
        return f'{get_readable_file_size(self.speed_raw())}/s'

    def name(self):
        return self.__name

    def size(self):
        return get_readable_file_size(self.__size)

    def eta(self):
        try:
            seconds = (self.__size - self.processed_raw()) / self.speed_raw()
            return get_readable_time(seconds)
        except ZeroDivisionError:
            return '-'

    def status(self):
        return MirrorStatus.STATUS_METADATA

    def processed_bytes(self):
        return get_readable_file_size(self.processed_raw())

    def processed_raw(self):
        # Implement the logic to calculate the processed raw data size
        return 0  # Placeholder, replace with actual calculation if available
        
