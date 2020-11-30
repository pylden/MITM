class Version:
    protocolId = 7207

    def __init__(self):
        self.major = 0
        self.minor = 0
        self.code = 0
        self.build = 0
        self.buildType = 0

    def deserialize(self, buffer):
        self.major = int.from_bytes(buffer.read_byte(), "big")
        self.minor = int.from_bytes(buffer.read_byte(), "big")
        self.code = int.from_bytes(buffer.read_byte(), "big")
        self.build = buffer.read_int()
        self.buildType = int.from_bytes(buffer.read_byte(), "big")
        return {
            "major": self.major,
            "minor": self.minor,
            "code": self.code,
            "build": self.build,
            "buildType": self.buildType
        }