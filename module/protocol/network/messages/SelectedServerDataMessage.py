from module.protocol.network.messages.NetworkMessage import NetworkMessage
from module.io.bytes_reader import BytesReader


class  SelectedServerDataMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6182
        self.serverId = {"type": "uint", "value": ""}
        self.address = {"type": "String", "value": ""}
        self.ports = {"type": "Vector.<uint>", "value": []}
        self.canCreateNewCharacter = {"type": "Boolean", "value": ""}
        self.ticket = {"type": "Vector.<int>", "value": []}

    def deserialize(self):
        self.serverId = self.buffer_reader.read_var_short()
        self.address = self.buffer_reader.read_utf()
        ports_length = self.buffer_reader.read_ushort()
        for i in range(0, ports_length):
            self.ports.append(self.buffer_reader.read_var_short())
        self.canCreateNewCharacter = self.buffer_reader.read_boolean()
        ticket_length = self.buffer_reader.read_var_int()
        for i in range(0, ticket_length):
            self.ticket.append(self.buffer_reader.read_byte())

    def serialize(self):
        br = BytesReader()
        br.write_var_short(len(self.address))
        br.write_utf(self.address)
        br.write_ushort(len(self.ports))
        for port in self.ports:
            br.write_var_short(port)
        br.write_bool(self.canCreateNewCharacter)
        br.write_var_int(len(self.ticket))
        for t in self.ticket:
            br.write_byte(t)
        self.buffer_reader = br
