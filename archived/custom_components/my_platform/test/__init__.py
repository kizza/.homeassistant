class FakeBtle:
    def Peripheral(uuid):
        return FakeBtlePeripheral()

    def UUID(uuid):
        pass

class FakeBtlePeripheral:
    @property
    def services(self):
        return []

    def getServiceByUUID(self, uuid):
        return FakeBtleService()

class FakeBtleService:
    def getCharacteristics(self):
        return [FakeBtleCharacteristic()]

class FakeBtleCharacteristic:
    def write(self, value, require_response):
        pass
