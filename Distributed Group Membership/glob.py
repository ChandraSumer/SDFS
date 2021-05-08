# time stamp format in this program
TIME_FORMAT_STRING = '%H:%M:%S'

# static introducer addr
INTRODUCER_HOST = '13.233.99.230'

# made for introducer
ALL_HOSTS = [
    '13.233.99.230',  # 01
    '13.233.106.125',  # 02
    '65.0.168.138',  # 03
    '3.7.45.153',  # 04
    '13.235.48.31',  # 05
]

# default socket port
DEFAULT_PORT = 55343

# topology of 3 VMs
# {source: [dest_1, dest_2, ...]}
CONNECTIONS = {
    '13.233.99.230': [
        '13.233.106.125',
        '165.0.168.138',
    ],
    '13.233.106.125': [
        '65.0.168.138',
        '3.7.45.153',
    ],
    '65.0.168.138': [
        '3.7.45.153',
        '13.235.48.31',
    ],
    '3.7.45.153': [
        '13.235.48.31',
        '13.233.99.230',
    ],
    '13.235.48.31': [
        '13.233.99.230',
        '13.233.106.125',
    ] 
}
