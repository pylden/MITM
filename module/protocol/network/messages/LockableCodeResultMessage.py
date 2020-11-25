from module.protocol.network.message import Message


class LockableCodeResultMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 302
        self.result = {"type": "uint", "value": ""}
