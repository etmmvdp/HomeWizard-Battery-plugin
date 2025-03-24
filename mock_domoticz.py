#
#   Mock Domoticz - Domoticz Python plugin mock
#
#   With thanks to Frank Fesevur, 2017
#
#   Very simple module to make local testing easier
#   It mocks Domoticz.Log(), Domoticz.Error and Domoticz.Debug()
#   It also mocks the Device and Unit from the Ex framework
#

class DomoticzMock:
    def __init__(self):
        self.Units = []
        self.Devices = dict()
        self.heartbeat = 1
        print("using Mock Domoticz")
        return

    def Log(self, s):
        print(s)

    def Status(self, s):
        print(s)

    def Error(self, s):
        print(s)

    def Debug(self, s):
        print(s)

    def Debugging(self, s):
        print(s)

    def Heartbeat(self, heartbeat):
        self.heartbeat = heartbeat

    def Device(self, Name, Unit, Type, Subtype=1, Switchtype=None, Options=None):
        Devices[Unit] = Device(name=Name, id=Unit, type=Type, sub_type=Subtype, switch_type=Switchtype)
        return Devices[Unit]

    def runPlugin(self, plugin, timeout):
        import time

        plugin.onStart()

        start_time = time.time()
        while time.time() - start_time < timeout:
            time.sleep(self.heartbeat)
            plugin.onHeartbeat()

class Device():
    def __init__(self, id, name, type, sub_type, switch_type=None, n_value=0, n_value_string="", s_value="", last_update=None):
        self.id = id
        self.ID = self.id
        self.name = name
        self.Name = self.name
        self.type = type
        self.sub_type = sub_type
        self.switch_type = switch_type
        self.n_value = n_value
        self.nValue = self.n_value
        self.n_value_string = n_value_string
        self.s_value = s_value
        self.sValue = self.s_value
        self.last_update_string = last_update
        self.LastLevel = float('nan')

    def __str__(self):
        return f"Device({self.id}, '{self.name}', {self.n_value}, '{self.s_value}')"

    def __repr__(self):
        return f"Device({self.id}, '{self.name}', {self.n_value}, '{self.s_value}')"

    def Create(self):
        print(f"Created {self}")

    def Update(self, nValue, sValue, SignalLevel):
        self.n_value = nValue
        self.nValue = self.n_value
        self.s_value = sValue
        self.sValue = self.s_value
        print(f"Updated {self}")

Parameters = {f"Mode{i}": "" for i in range(1, 7)}
Devices = {}
Domoticz = DomoticzMock()