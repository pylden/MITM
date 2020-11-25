from module.protocol.network.message import Message


class NpcGenericActionRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3595
        self.npcId = {"type": "int", "value": ""}
        self.npcActionId = {"type": "uint", "value": ""}
        self.npcMapId = {"type": "Number", "value": ""}
