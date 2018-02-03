'''
This is example configuration for Stratum server.
Please rename it to config.py and fill correct values.
'''

# ******************** GENERAL SETTINGS ***************

# Enable some verbose debug (logging requests and responses).
DEBUG = True

# Destination for application logs, files rotated once per day.
LOGDIR = 'log/'

# Main application log file.
LOGFILE = None #'stratum.log'

# Possible values: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOGLEVEL = 'DEBUG'

# How many threads use for synchronous methods (services).
# 30 is enough for small installation, for real usage
# it should be slightly more, say 100-300.
THREAD_POOL_SIZE = 30

# RPC call throws TimeoutServiceException once total time since request has been
# placed (time to delivery to client + time for processing on the client)
# crosses _TOTAL (in second).
# _TOTAL reflects the fact that not all transports deliver RPC requests to the clients
# instantly, so request can wait some time in the buffer on server side.
# NOT IMPLEMENTED YET
#RPC_TIMEOUT_TOTAL = 600

# RPC call throws TimeoutServiceException once client is processing request longer
# than _PROCESS (in second)
# NOT IMPLEMENTED YET
#RPC_TIMEOUT_PROCESS = 30

# Do you want to expose "example" service in server?
# Useful for learning the server,you probably want to disable
# this on production
ENABLE_EXAMPLE_SERVICE = True

# ******************** TRANSPORTS *********************

# Hostname or external IP to expose
HOSTNAME = '192.168.1.30'

# Port used for Socket transport. Use 'None' for disabling the transport.
LISTEN_SOCKET_TRANSPORT = 3333

# Port used for HTTP Poll transport. Use 'None' for disabling the transport
LISTEN_HTTP_TRANSPORT = 8000

# Port used for HTTPS Poll transport
LISTEN_HTTPS_TRANSPORT = 8001

# Port used for WebSocket transport, 'None' for disabling WS
LISTEN_WS_TRANSPORT = 8002

# Port used for secure WebSocket, 'None' for disabling WSS
LISTEN_WSS_TRANSPORT = 8003

# ******************** SSL SETTINGS ******************

# Private key and certification file for SSL protected transports
# You can find howto for generating self-signed certificate in README file
SSL_PRIVKEY = 'MIICXAIBAAKBgQC7xCHYVXhjsj6kq5KsLbDGZF7TueXo8kNsWzz4aQYPq414Qog2a5hf9takoeo62DHE48jCijz1ecMhS0oyRvs7FZGhm4EaQwqQiySoj4pTLuNawwrrmK+h0OwVCZi35cvpVDnj1KEQNueURUykczUQfO5SWw3EXiZKj6zwYswIDAQABAoGAEXcc7tKEcEGUMh0Dd6CIYOvVJjyUdiaSvvF9ql2agrqiXh1SLj29W7RY4wPeOogqaFoZZlj7ljKWxrIKJMMVcRBj1wGd1yDlMEsxyZJ8VkZegZLzohp2n5AffR9sZSyeLY2sixdI57JEVWHbWYta3HJhCpOWt3Xvf0CiaywECQQD6EqRGNKpBZYmgQb5O6lNaU3IcRnV1kKEeKm2JQ0R6LfDx34Ln1RoIC5InRRX2LJkq9I7jQJftelftIj6T127rAkEAwDdvNYsE7LGORxUTvfXPryY7vg4iLuRTWPqrR24PtzBnAf9fMDRu8zcF96XmtsDpe890fKS+p3xTsg3KcntbWQJBAJkqCcumPhFH639oRPN4ugy8x0tiLFcRel1Lh0NnG+3pbYX3a+oqr4L181JyEf1xW27f0xSFX4hoQqpPKxzJ+nkCQHztCmhAPCkhlRj5x+T0N9DcBoQVZ34Wg10XPe6kx64F1UzlDpaj3WBRaJ11w6cPZjBDuq+v2wG7uiHE+MjDB7ECQGB7qOMr5TIn7RvjrENCU95CXml8XeFHwyCp6jIrYlwSRM0TaeubzxEraNUt8f76rND0cju8u4IVmaENpyCok'
SSL_CACERT = 'b23ea4ab92ac2db0c6645ed3b9e5e8f2436c5b3cf869060fab8d784288366bfe617fdb5a9287a8eb60c7138f230a28f3d5e70c852d28c91becec5646866e04690c2a422cbf4a88f8a532ee35ac3fc2bae62be8743b0542662df972fa550e78f528440db9e51153291ccd441f3b9496c371178992a3eb3c18b30203010001'

# ******************** TCP SETTINGS ******************

# Enables support for socket encapsulation, which is compatible
# with haproxy 1.5+. By enabling this, first line of received
# data will represent some metadata about proxied stream:
# PROXY <TCP4 or TCP6> <source IP> <dest IP> <source port> </dest port>\n
#
# Full specification: http://haproxy.1wt.eu/download/1.5/doc/proxy-protocol.txt
TCP_PROXY_PROTOCOL = False

# ******************** HTTP SETTINGS *****************

# Keepalive for HTTP transport sessions (at this time for both poll and push)
# High value leads to higher memory usage (all sessions are stored in memory ATM).
# Low value leads to more frequent session reinitializing (like downloading address history).
HTTP_SESSION_TIMEOUT = 3600 # in seconds

# Maximum number of messages (notifications, responses) waiting to delivery to HTTP Poll clients.
# Buffer length is PER CONNECTION. High value will consume a lot of RAM,
# short history will cause that in some edge cases clients won't receive older events.
HTTP_BUFFER_LIMIT = 10000

# User agent used in HTTP requests (for both HTTP transports and for proxy calls from services)
USER_AGENT = 'Stratum/0.1'

# Provide human-friendly user interface on HTTP transports for browsing exposed services.
BROWSER_ENABLE = True

# ******************** BITCOIND SETTINGS ************

# Hostname and credentials for one trusted Bitcoin node ("Satoshi's client").
# Stratum uses both P2P port (which is 8333 everytime) and RPC port
BITCOIN_TRUSTED_HOST = '127.0.0.1'
BITCOIN_TRUSTED_PORT = 35422 # RPC port
BITCOIN_TRUSTED_USER = 'androidcoin'
BITCOIN_TRUSTED_PASSWORD = '1111'

# ******************** OTHER CORE SETTINGS *********************
# Use "echo -n '<yourpassword>' | sha256sum | cut -f1 -d' ' "
# for calculating SHA256 of your preferred password
ADMIN_PASSWORD_SHA256 = None # Admin functionality is disabled
#ADMIN_PASSWORD_SHA256 = '9e6c0c1db1e0dfb3fa5159deb4ecd9715b3c8cd6b06bd4a3ad77e9a8c5694219' # SHA256 of the password

# IP from which admin calls are allowed.
# Set None to allow admin calls from all IPs
ADMIN_RESTRICT_INTERFACE = '127.0.0.1'

# Use "./signature.py > signing_key.pem" to generate unique signing key for your server
SIGNING_KEY = None # Message signing is disabled
#SIGNING_KEY = 'signing_key.pem'

# Origin of signed messages. Provide some unique string,
# ideally URL where users can find some information about your identity
SIGNING_ID = None
#SIGNING_ID = 'stratum.somedomain.com' # Use custom string
#SIGNING_ID = HOSTNAME # Use hostname as the signing ID

# *********************** IRC / PEER CONFIGURATION *************

IRC_NICK = None # Skip IRC registration
#IRC_NICK = "stratum" # Use nickname of your choice

# Which hostname / external IP expose in IRC room
# This should be official HOSTNAME for normal operation.
IRC_HOSTNAME = HOSTNAME

# Don't change this unless you're creating private Stratum cloud.
IRC_SERVER = 'irc.freenode.net'
IRC_ROOM = '#stratum-nodes'
IRC_PORT = 6667

# Hardcoded list of Stratum nodes for clients to switch when this node is not available.
PEERS = [
    {
        'hostname': '',
        'trusted': True, # This node is trustworthy
        'weight': -1, # Higher number means higher priority for selection.
                      # -1 will work mostly as a backup when other servers won't work.
                      # (IRC peers have weight=0 automatically).
    },
]


'''
DATABASE_DRIVER = 'MySQL'
DATABASE_HOST = 'localhost'
DATABASE_DBNAME = 'mpos'
DATABASE_USER = 'root'
DATABASE_PASSWORD = 'kris1to2'
'''
