from module.protocol.network.message import Message


class UpdateMapPlayersAgressableStatusMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2994
        self.playerIds = {"type": "Vector.<Number>", "value": ""}
        self.enable = {"type": "Vector.<uint>", "value": ""}
