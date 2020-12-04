from module.protocol.network.messages.NetworkMessage import NetworkMessage
from module.protocol.network.utils.boolean_byte_wrapper import BooleanByteWrapper
from module.protocol.network.types.version import Version


class IdentificationMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5833
        self.version = {"type": "Version", "value": ""}
        self.lang = {"type": "String", "value": ""}
        self.credentials = {"type": "Vector.<int>", "value": []}
        self.serverId = {"type": "int", "value": ""}
        self.autoconnect = {"type": "Boolean", "value": ""}
        self.useCertificate = {"type": "Boolean", "value": ""}
        self.useLoginToken = {"type": "Boolean", "value": ""}
        self.sessionOptionalSalt = {"type": "Number", "value": ""}
        self.failedAttempts = {"type": "Vector.<uint>", "value": []}

    def deserialize(self):
        box = self.buffer_reader.read_uchar()
        self.autoconnect["value"] = BooleanByteWrapper.get_flag(box, 0)
        self.useCertificate["value"] = BooleanByteWrapper.get_flag(box, 1)
        self.useLoginToken["value"] = BooleanByteWrapper.get_flag(box, 2)
        self.version["value"] = Version()
        self.version["value"].deserialize(self.buffer_reader)
        self.lang = self.buffer_reader.read_utf()
        credentials_length = self.buffer_reader.read_var_int()
        for i in range(credentials_length):
            self.credentials["value"].append(int.from_bytes(self.buffer_reader.read_byte(), "big"))
        self.serverId = self.buffer_reader.read_short()
        self.sessionOptionalSalt = self.buffer_reader.read_var_long()
        failed_attempts_length = self.buffer_reader.read_ushort()
        for i in range(failed_attempts_length):
            self.failedAttempts["value"].append(self.buffer_reader.read_read_var_uh_short())
