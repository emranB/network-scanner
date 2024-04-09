from ..NetScanner import NetScanner
import subprocess


class IcmpScanner(NetScanner):
    def __init__(self, config_manager, logger):
        super().__init__(config_manager, logger)

    def scan(self):
        self._craft_packets()
        self._transmit_packets()
        self._output_results()

    def _craft_packets(self):
        self.target_ip_range = self.config_manager.get_ip_range().split("-")
        self.logger.info(f"Crafting ICMP packets to network {self.target_ip_range}...")

    def _transmit_packets(self):
        for ip in self._generate_ip_addresses():
                self._send_ping_request(ip)

    def _output_results(self):
        self.logger.info("Outputting ICMP scan results...")

    def _generate_ip_addresses(self):
        start_ip, end_ip = self.target_ip_range[0], self.target_ip_range[1]
        start, end = list(map(int, start_ip.split("."))), list(map(int, end_ip.split(".")))
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                for k in range(start[2], end[2] + 1):
                    for l in range(start[3], end[3] + 1):
                        yield f"{i}.{j}.{k}.{l}"

    def _send_ping_request(self, ip):
        try: # Run the ping command with -c 1 option to ping only once
            result = subprocess.check_output(["ping", ip]).decode()
            is_alive = "TTL" in result or "ttl" in result
            if is_alive:
                self.logger.info(f"Host {ip} is alive")
                self.alive_hosts.append(ip)
            else:
                self.logger.info(f"Host {ip} is unreachable")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred during ICMP transmission: {e}")