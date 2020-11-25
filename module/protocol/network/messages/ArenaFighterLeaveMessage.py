from module.protocol.network.message import Message


class ArenaFighterLeaveMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8113
        self.leaver = {"type": "CharacterBasicMinimalInformations", "value": ""}
