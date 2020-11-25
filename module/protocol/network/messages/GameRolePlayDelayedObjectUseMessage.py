from module.protocol.network.message import Message


class GameRolePlayDelayedObjectUseMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1711
        self.objectGID = {"type": "uint", "value": ""}
