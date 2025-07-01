#!/usr/bin/env python3

import sys

from plugin import BasePlugin
from mock_domoticz import Domoticz, Parameters

def main():
    Parameters["Address"] = "192.168.1.18"
    Parameters["Port"] = 443
    Parameters["Mode1"] = 10
    Parameters["Mode2"] = "F9AFAB2CEF1A999F55AFD72946E3E647"
    Parameters["Mode3"] = "Yes"
    Parameters["Mode6"] = "Debug"

    plugin = BasePlugin()
    Domoticz.runPlugin(plugin, 60)

    print("\n\nstarting again, now with existing devices\n\n")
    Domoticz.runPlugin(plugin, 60)

    sys.exit(0)

if __name__ == "__main__":
    main()
