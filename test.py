#!env python
import sys

from plugin import BasePlugin
from mock_domoticz import Domoticz, Parameters

def main():
    Parameters["Address"] = "192.168.1.100"
    Parameters["Port"] = 443
    Parameters["Mode1"] = 10
    Parameters["Mode2"] = "99F1B745E01A2239E7B78E65E95FB888"
    Parameters["Mode3"] = "Yes"
    Parameters["Mode6"] = "Debug"

    plugin = BasePlugin()
    Domoticz.runPlugin(plugin, 60)

    print("\n\nstarting again, now with existing devices\n\n")
    Domoticz.runPlugin(plugin, 60)

    sys.exit(0)

if __name__ == "__main__":
    main()
