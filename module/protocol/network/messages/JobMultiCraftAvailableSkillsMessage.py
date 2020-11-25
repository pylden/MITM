from module.protocol.network.message import Message


class JobMultiCraftAvailableSkillsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 834
        self.playerId = {"type": "Number", "value": ""}
        self.skills = {"type": "Vector.<uint>", "value": ""}
