from module.protocol.network.message import Message


class ServersListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8688
        self.servers = {"type": "Vector.<GameServerInformations>", "value": ""}
        self.alreadyConnectedToServerId = {"type": "uint", "value": ""}
        self.canCreateNewCharacter = {"type": "Boolean", "value": ""}
