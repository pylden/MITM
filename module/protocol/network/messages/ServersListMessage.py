from module.protocol.network.message import Message


class ServersListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8688
        self.servers = {"type": "Vector.<GameServerInformations>", "value": ""}
        self.alreadyConnectedToServerId = {"type": "uint", "value": ""}
        self.canCreateNewCharacter = {"type": "Boolean", "value": ""}
