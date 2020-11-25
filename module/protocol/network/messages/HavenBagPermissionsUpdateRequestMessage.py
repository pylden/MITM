from module.protocol.network.message import Message


class HavenBagPermissionsUpdateRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4834
        self.permissions = {"type": "uint", "value": ""}
