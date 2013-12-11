#!/usr/bin/env python
# This hacky script iterates over your starbound log file and prints a list of
# of connected clients. This will work until some update changes log format

# Set this to be the full path to your log file
STARBOUND_LOGFILE = "/home/starbound/linux64/starbound_server.log"

# Log keywords
# connected disconnected = duh
# connection = reaped ... we delete these keys from the dict
# " " = loading ship world received from client


def main():
    clients = {}
    with open(STARBOUND_LOGFILE, 'r') as log:
        for line in log:
            # Chat begins with two spaces in the log and contains a caret.
            # Find it and strip it as we don't want to count chat
            status = line.split(':  ')
            if len(status) > 1:
                status = ""
            # Now we can detect carets as connection messages
            status = line.split('Client <')
            if len(status) > 1:
                # Strip new lines and ending carets
                status = status[1].replace("\n", "").replace(">", "")
                # Detect client number and set their status
                if status.split(" ")[0].isdigit():
                    if len(status.split(" ")) > 1:
                        clients[status.split(" ")[0]] = status.split(" ")[2]

    # Clean reaped players from dictionary
    for player, status in clients.items():
        # Player's connection has been reaped, keyword connection
        if status == 'connection':
            del clients[player]

    print "Total Connected Players: %s" % len(clients.keys())
    for player, status in clients.iteritems():
        print "[client %s = %s]" % (player, status)


if __name__ == '__main__':
    main()


