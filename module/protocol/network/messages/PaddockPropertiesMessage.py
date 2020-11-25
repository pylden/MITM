from module.protocol.network.message import Message


class PaddockPropertiesMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7932
        self.properties = {"type": "PaddockInstancesInformations", "value": ""}
