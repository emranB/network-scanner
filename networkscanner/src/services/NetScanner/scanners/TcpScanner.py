from ..NetScanner import NetScanner
import socket

class TcpScanner(NetScanner):
    def __init__(self, config_manager, logger):
        super().__init__(config_manager, logger)

    def scan(self):
        self._craft_packets()
        self._transmit_packets()
        self._output_results()

    def _craft_packets(self):
        self.target_ip_range = self.config_manager.get_ip_range().split("-")
        self.target_ports_range = range(*map(int, self.config_manager.get_port_range().split("-")))
        self.logger.info(f"Crafting TCP packets to {self.target_ip_range} on ports {self.target_ports_range}...")

    def _transmit_packets(self):
        for ip in self._generate_ip_addresses():
            for port in self.target_ports_range:
                self._send_packet(ip, port)

    def _output_results(self):
        self.logger.info("Outputting TCP scan results...")

    def _generate_ip_addresses(self):
        start_ip, end_ip = self.target_ip_range[0], self.target_ip_range[1]
        start, end = list(map(int, start_ip.split("."))), list(map(int, end_ip.split(".")))
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                for k in range(start[2], end[2] + 1):
                    for l in range(start[3], end[3] + 1):
                        yield f"{i}.{j}.{k}.{l}"

    def _send_packet(self, ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                self.logger.info(f"Port {port} is open on {ip}")
                self.alive_hosts.append(ip)
            else:
                self.logger.info(f"Port {port} is closed on {ip}")
            sock.close()
        except Exception as e:
            self.logger.error(f"Error occurred during TCP transmission: {e}")
