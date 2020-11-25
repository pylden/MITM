from module.protocol.network.message import Message


class UpdateMapPlayersAgressableStatusMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2994
        self.playerIds = {"type": "Vector.<Number>", "value": ""}
        self.enable = {"type": "Vector.<uint>", "value": ""}
