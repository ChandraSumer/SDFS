# time stamp format in this program
TIME_FORMAT_STRING = '%H:%M:%S'

# static introducer addr
INTRODUCER_HOST = '13.235.243.174'

# made for introducer
ALL_HOSTS = [
    '35.154.147.113',  # 01
    '13.235.243.174',  # 02
    '13.235.49.182',  # 03
]

# default socket port
DEFAULT_PORT_FD = 52333
DEFAULT_PORT_SDFS = 53222

# topology of 3 VMs
# {source: [dest_1, dest_2, ...]}
CONNECTIONS = {
    '13.235.243.174': [
        '35.154.147.113',
        '13.235.49.182',
    ],
    '35.154.147.113': [
        '13.235.243.174',
        '13.235.49.182',
    ],
    '13.235.49.182': [
        '35.154.147.113',
        '13.235.243.174',
    ]    
}
