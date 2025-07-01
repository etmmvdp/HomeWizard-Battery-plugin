#!env python3
import logging
from zeroconf import ServiceBrowser, ServiceListener, Zeroconf, IPVersion


class MyListener(ServiceListener):
    def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        print(f"Service {name} updated")

    def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        print(f"Service {name} removed")

    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        info = zc.get_service_info(type_, name)
        version = "v1" if "hwenergy" in name else "v2"
        print(f"Device {info.properties.get('product_name'.encode('ascii'), 'unknown').decode('ascii')} " +
            f"with name {name} on api {version} available at ip {info.parsed_addresses(version=IPVersion.V4Only)}")
        # print(f"info is  {info}")

def main():
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("zeroconf").setLevel(logging.INFO)

    zeroconf = Zeroconf()
    listener = MyListener()
    ServiceBrowser(zeroconf, "_homewizard._tcp.local.", listener)
    ServiceBrowser(zeroconf, "_hwenergy._tcp.local.", listener)

    try:
        input("Waiting for zeroconf browser result. This can take up to 20 seconds. Press enter to exit...\n")
    finally:
        zeroconf.close()


if __name__ == "__main__":
    main()
