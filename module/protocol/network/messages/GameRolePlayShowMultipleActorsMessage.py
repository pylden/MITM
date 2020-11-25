from module.protocol.network.message import Message


class GameRolePlayShowMultipleActorsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4416
        self.informationsList = {"type": "Vector.<GameRolePlayActorInformations>", "value": ""}
