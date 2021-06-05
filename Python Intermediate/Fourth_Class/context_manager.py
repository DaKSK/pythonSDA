from contextlib import contextmanager
# contextlib the easiest way to implement

# context manager by class


class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


with File("filename", "w") as f:
    pass

# WITH CONTEXT MANAGER


@contextmanager
def open_file(name):
    file = open(name, 'w')
    try:
        yield f
    finally:
        file.close()


with open_file("filename") as opened_file:
    pass
