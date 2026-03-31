#!/usr/bin/env python3

import sys

from plugin import BasePlugin
from mock_domoticz import Domoticz, Parameters

def main():
    Parameters["Address"] = "192.168.X.X"
    Parameters["Port"] = 443
    Parameters["Mode1"] = 10
    Parameters["Mode2"] = "XXX"
    Parameters["Mode3"] = "Yes"
    Parameters["Mode6"] = ""

    plugin = BasePlugin()
    Domoticz.runPlugin(plugin, 60)

    print("\n\nstarting again, now with existing devices\n\n")
    Domoticz.runPlugin(plugin, 60)

    sys.exit(0)

if __name__ == "__main__":
    main()
