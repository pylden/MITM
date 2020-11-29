from module.protocol.network.messages.LockableStateUpdateAbstractMessage import LockableStateUpdateAbstractMessage


class LockableStateUpdateStorageMessage(LockableStateUpdateAbstractMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        LockableStateUpdateAbstractMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2174
        self.vars.append({"name": "mapId", "type": "Number", "value": ""})
        self.vars.append({"name": "elementId", "type": "uint", "value": ""})
