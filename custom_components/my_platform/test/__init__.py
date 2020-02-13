class FakeBtle:
    def Peripheral(uuid):
        print("Fake "+uuid)
        return FakeBtlePeripheral()

    def UUID(uuid):
        print("Fake "+uuid)

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
        print("MOCK: Writing to characteristic")
        print(value)


