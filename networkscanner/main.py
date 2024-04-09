import sys
from src.utils.Logger import Logger
from src.utils.ConfigManager import ConfigManager
from src.services.NetScanner.NetScanner import NetScanner
from src.services.NetScanner.scanners.TcpScanner import TcpScanner
from src.services.NetScanner.scanners.IcmpScanner import IcmpScanner


def main(root_path):
    config_manager = ConfigManager(root_path)
    logger = Logger(config_manager.get("logger"), root_path)

    mode = config_manager.get("netscanner").get("mode")

    scanner: NetScanner
    if mode == "tcp":
        scanner = TcpScanner(config_manager, logger)
    elif mode == "icmp":
        scanner = IcmpScanner(config_manager, logger)
    else:
        logger.error("Invalid scanning mode specified in configuration.")
        exit(1)

    scanner.scan()
    scanner.exit()

if __name__ == "__main__":
    root_path = sys.argv[1] if len(sys.argv) > 1 else "."
    main(root_path)