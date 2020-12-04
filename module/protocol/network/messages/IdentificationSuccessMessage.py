from module.protocol.network.messages.NetworkMessage import NetworkMessage
from module.protocol.network.utils.boolean_byte_wrapper import BooleanByteWrapper


class IdentificationSuccessMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8394
        self.login = {"type": "String", "value": ""}
        self.nickname = {"type": "String", "value": ""}
        self.accountId = {"type": "uint", "value": ""}
        self.communityId = {"type": "uint", "value": ""}
        self.hasRights = {"type": "Boolean", "value": ""}
        self.hasConsoleRight = {"type": "Boolean", "value": ""}
        self.secretQuestion = {"type": "String", "value": ""}
        self.accountCreation = {"type": "Number", "value": ""}
        self.subscriptionElapsedDuration = {"type": "Number", "value": ""}
        self.subscriptionEndDate = {"type": "Number", "value": ""}
        self.wasAlreadyConnected = {"type": "Boolean", "value": ""}
        self.havenbagAvailableRoom = {"type": "uint", "value": ""}

    def deserialize(self):
        box = self.buffer_reader.read_uchar()
        self.hasRights["value"] = BooleanByteWrapper.get_flag(box, 0)
        self.hasConsoleRight["value"] = BooleanByteWrapper.get_flag(box, 1)
        self.wasAlreadyConnected["value"] = BooleanByteWrapper.get_flag(box, 2)
        self.login["value"] = self.buffer_reader.read_utf()
        self.nickname["value"] = self.buffer_reader.read_utf()
        self.accountId["value"] = self.buffer_reader.read_int()
        self.communityId["value"] = self.buffer_reader.read_char()
        self.secretQuestion["value"] = self.buffer_reader.read_utf()
        self.accountCreation["value"] = self.buffer_reader.read_double()
        self.subscriptionElapsedDuration["value"] = self.buffer_reader.read_double()
        self.subscriptionEndDate["value"] = self.buffer_reader.read_double()
        self.havenbagAvailableRoom["value"] = self.buffer_reader.read_uchar()
