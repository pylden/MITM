from module.protocol.network.messages.LockableStateUpdateAbstractMessage import LockableStateUpdateAbstractMessage


class LockableStateUpdateStorageMessage(LockableStateUpdateAbstractMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        LockableStateUpdateAbstractMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2174
        self.mapId = {"type": "Number", "value": ""}
        self.elementId = {"type": "uint", "value": ""}
