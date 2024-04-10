# Network Scanner
---
### Network Scanner is able to send:
- TCP requests to a range of IPs and Ports (configurable, see below)
- ICMP requests to a range of IPs (configurable, see below)

### Usage:
- Using bash:
```
1. From root of project, run: `sh run.sh`
OR
2. run: `sh run.sh <path_to_root_of_project>`
```

- Using docker:
```
- From root of project, build using: `sh docker_build.sh`
- From root of project, run using: `sh docker_run.sh`
```

### After scanning the channels, the scanner checks for alive hosts and:
- Prints the alive hosts on screen (configurable, see below)
```
Sample log:
---
Crafting ICMP packets to network ['127.0.0.1', '127.0.0.5']...
Host 127.0.0.1 is alive
Host 127.0.0.2 is alive
Host 127.0.0.3 is alive
Host 127.0.0.4 is alive
Host 127.0.0.5 is alive
Outputting ICMP scan results...
Result: 127.0.0.1
Result: 127.0.0.2
Result: 127.0.0.3
Result: 127.0.0.4
Result: 127.0.0.5
Scan completed. Results saved to <output_file_path>
----------------------------------------------------
Alive hosts:  ['127.0.0.1', '127.0.0.2', '127.0.0.3', '127.0.0.4', '127.0.0.5']
----------------------------------------------------

```
- Saves the alive hosts in an external file (configurable, see below)
```
Sample file output:
---
127.0.0.1
127.0.0.2
127.0.0.3
127.0.0.4
127.0.0.5
```
### The scanner supports a logging system
- Logs are printed based on severity level
- Colored for improved visibility
```
Sample log:
---
2024-04-09 13:18:16,101 - src.utils.Logger - INFO - Crafting ICMP packets to network ['127.0.0.1', '127.0.0.5']...
2024-04-09 13:18:19,204 - src.utils.Logger - INFO - Host 127.0.0.1 is alive
2024-04-09 13:18:22,262 - src.utils.Logger - INFO - Host 127.0.0.2 is alive
2024-04-09 13:18:25,332 - src.utils.Logger - INFO - Host 127.0.0.3 is alive
2024-04-09 13:18:28,422 - src.utils.Logger - INFO - Host 127.0.0.4 is alive
2024-04-09 13:18:31,495 - src.utils.Logger - INFO - Host 127.0.0.5 is alive
2024-04-09 13:18:31,495 - src.utils.Logger - INFO - Outputting ICMP scan results...
2024-04-09 13:18:31,495 - src.utils.Logger - INFO - Result: 127.0.0.1
2024-04-09 13:18:31,495 - src.utils.Logger - INFO - Result: 127.0.0.2
2024-04-09 13:18:31,495 - src.utils.Logger - INFO - Result: 127.0.0.3
2024-04-09 13:18:31,495 - src.utils.Logger - INFO - Result: 127.0.0.4
2024-04-09 13:18:31,495 - src.utils.Logger - INFO - Result: 127.0.0.5
2024-04-09 13:18:31,495 - src.utils.Logger - INFO - Scan completed. Results saved to <external file name>
```

### The config is compiled as:
```
Sample config:
---
{
    "logger": {
        "log_to_screen": false,
        "log_to_file": true,
        "log_file": "scanner.log",
        "debug": true
    },

    "netscanner": {
        "mode": "icmp",
        "ip_range": "127.0.0.1-127.0.0.5",
        "port_range": "139-140",
        "output_file": "scan_results.txt",
        "print_to_screen": true,
        "write_to_file": true
    }
}
---

Note: netscanner/mode: Supported modes: `["tcp" | "icmp"]`
```
---

# Philosophy
---
### The use of Internet Control Message Protocol (ICMP) and Transmission Control Protocol (TCP) for scanning to identify active hosts is based on their inherent functionalities within the network protocol stack, each offering unique advantages for this purpose:

## ICMP (Internet Control Message Protocol)
<pre>
- `Diagnostic and Control Messaging`: Tailored for sending network diagnostic or control messages, facilitating error reporting and status inquiries.
- `Echo Request/Reply`: Utilizes simple echo mechanisms (ping) for host reachability checks, making it straightforward to ascertain if a host is active.
- `Efficiency`: Offers minimal overhead with its lightweight messages, ideal for broad scanning operations.
</pre>

## TCP (Transmission Control Protocol)
<pre>
- `Three-way Handshake`: Leverages the SYN, SYN-ACK, ACK handshake for connection establishment, allowing for the detection of open ports without completing a connection. This method, known as SYN scanning, is stealthy and often evades certain firewall protections.
- `Port Scanning Capabilities`: Essential for determining the open ports on a host, as it directly tries to establish connections, providing clear insights into the services running on a host.
</pre>

Both protocols are chosen for their specific roles in network management and communication, with ICMP being optimal for quick, broad checks of host availability, and TCP providing detailed insights into available services and port statuses. Their combined use in scanning operations ensures a comprehensive view of network host activity and service availability.