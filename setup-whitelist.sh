#!/usr/bin/env sh
# Starbound Whitelist
# Execute with sudo or as root

# Insert IP addresses followed by a linebreak for each IP you want
# whitelisted. Remove the IPs below and insert your own list
WHITELIST=\
"
49.38.189.211
123.123.123.123
"
# The port you're hosting on. Default=21025
STARBOUND_PORT=21025


# Note for the noob:
# The following command will wipe out any existing iptables rules
iptables --flush

# We need to have ACCEPT rules before DROP
for ip_addr in $WHITELIST; do
    iptables -A INPUT -s $ip_addr -p tcp --destination-port $STARBOUND_PORT -j ACCEPT
done

# Accept all local traffic from/to anywhere
iptables -A INPUT -i lo -j ACCEPT

# Deny all other traffic from anyone to the starbound port
iptables -A INPUT -s 0.0.0.0/0 -p tcp --destination-port $STARBOUND_PORT -j DROP

