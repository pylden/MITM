from module.protocol.network.message import Message


class GameRolePlayPlayerLifeStatusMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2514
        self.state = {"type": "uint", "value": ""}
        self.phenixMapId = {"type": "Number", "value": ""}
