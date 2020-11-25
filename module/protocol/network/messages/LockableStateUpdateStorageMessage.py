from module.protocol.network.message import Message


class LockableStateUpdateStorageMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2174
        self.mapId = {"type": "Number", "value": ""}
        self.elementId = {"type": "uint", "value": ""}
