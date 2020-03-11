from io import BytesIO


class BytesReader(BytesIO):
    def __init__(self, buffer):
        super().__init__(buffer)
        self._current_buffer = buffer

    def get_current_buffer(self):
        return self.getbuffer()[self.tell():]
