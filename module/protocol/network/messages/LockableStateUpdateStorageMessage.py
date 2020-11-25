from module.protocol.network.message import Message


class LockableStateUpdateStorageMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2174
        self.mapId = {"type": "Number", "value": ""}
        self.elementId = {"type": "uint", "value": ""}
