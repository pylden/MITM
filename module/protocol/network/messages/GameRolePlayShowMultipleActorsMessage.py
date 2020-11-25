from module.protocol.network.message import Message


class GameRolePlayShowMultipleActorsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4416
        self.informationsList = {"type": "Vector.<GameRolePlayActorInformations>", "value": ""}
