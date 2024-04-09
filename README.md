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
Scan completed. Results saved to C:/Users/omega/Desktop/Code/Cybersecurity - Skills For Hire - 2024/Assignment 2/NetworkScanner\scan_results.txt
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
```