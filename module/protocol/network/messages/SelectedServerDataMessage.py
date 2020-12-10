from module.protocol.network.messages.NetworkMessage import NetworkMessage
from module.io.bytes_reader import BytesReader


class SelectedServerDataMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6182
        self.serverId = {"type": "uint", "value": ""}
        self.address = {"type": "String", "value": ""}
        self.ports = {"type": "Vector.<uint>", "value": []}
        self.canCreateNewCharacter = {"type": "Boolean", "value": ""}
        self.ticket = {"type": "Vector.<int>", "value": []}

    def deserialize(self):
        self.serverId["value"] = self.buffer_reader.read_var_short()
        self.address["value"] = self.buffer_reader.read_utf()
        ports_length = self.buffer_reader.read_ushort()
        for i in range(0, ports_length):
            self.ports["value"].append(self.buffer_reader.read_var_short())
        self.canCreateNewCharacter["value"] = self.buffer_reader.read_boolean()
        ticket_length = self.buffer_reader.read_var_int()
        for i in range(0, ticket_length):
            self.ticket["value"].append(self.buffer_reader.read_byte())

    def serialize(self):
        br = BytesReader()
        br.write_var_short(len(self.address["value"]))
        br.write_utf(self.address["value"])
        br.write_ushort(len(self.ports["value"]))
        for port in self.ports["value"]:
            br.write_var_short(port)
        br.write_bool(self.canCreateNewCharacter["value"])
        br.write_var_int(len(self.ticket["value"]))
        for t in self.ticket["value"]:
            br.write_byte(t)
        self.buffer_reader = br
