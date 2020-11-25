from module.protocol.network.message import Message


class NpcGenericActionRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3595
        self.npcId = {"type": "int", "value": ""}
        self.npcActionId = {"type": "uint", "value": ""}
        self.npcMapId = {"type": "Number", "value": ""}
