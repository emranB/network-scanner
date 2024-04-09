import os

class NetScanner:
    def __init__(self, config_manager, logger):
        self.config_manager = config_manager
        self.logger = logger
        self.root_path = self.config_manager.root_path
        self.alive_hosts = []

    def scan(self):
        raise NotImplementedError("Subclasses must implement scan method.")

    def exit(self):
        print_to_screen = self.config_manager.get("netscanner", {}).get("print_to_screen")
        write_to_file = self.config_manager.get("netscanner", {}).get("write_to_file")

        if print_to_screen:
            self._print_results()

        if write_to_file:
            self._save_results()

    def _print_results(self):
        for host in self.alive_hosts:
            self.logger.info(f"Result: {host}")

    def _save_results(self):
        output_file = os.path.join(self.root_path, self.config_manager.get("netscanner", {}).get("output_file", "scan_results.txt"))
        with open(output_file, "a") as output:
            for host in self.alive_hosts:
                output.write(host + "\n")

        self.logger.info(f"Scan completed. Results saved to {output_file}")
        print("----------------------------------------------------")
        print("Alive hosts: ", self.alive_hosts)
        print("----------------------------------------------------")
