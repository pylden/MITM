from module.protocol.network.messages.LockableStateUpdateAbstractMessage import LockableStateUpdateAbstractMessage


class LockableStateUpdateHouseDoorMessage(LockableStateUpdateAbstractMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        LockableStateUpdateAbstractMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3227
        self.vars.append({"name": "houseId", "type": "uint", "value": ""})
        self.vars.append({"name": "instanceId", "type": "uint", "value": ""})
        self.vars.append({"name": "secondHand", "type": "Boolean", "value": ""})
