from module.protocol.network.message import Message


class GameActionFightTeleportOnSameMapMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2698
        self.targetId = {"type": "Number", "value": ""}
        self.cellId = {"type": "int", "value": ""}
