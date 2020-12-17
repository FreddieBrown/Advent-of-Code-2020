from collections import Counter


def validity(data):
    valid_tickets = []
    not_valid = []
    rules = data[0].split("\n")
    your_ticket = data[1].split("\n")[1]
    your_ticket = [int(x) for x in your_ticket.split(",")]
    nearby = data[2].split("\n")
    rule_book = dict()
    # Build rules
    for rule in rules:
        rule = rule.split(": ")
        ranges = rule[1].split(" or ")
        valid = set()
        for r in ranges:
            r = [int(x) for x in r.split("-")]
            for elem in range(r[0], r[1]+1):
                valid.add(elem)
        rule_book[rule[0]] = valid

    # inspect nearby tickets
    for ticket in nearby:
        if ticket == "nearby tickets:":
            continue
        ticket = [int(x) for x in ticket.split(",")]
        valid_ticket = True
        for value in ticket:
            flag = True
            for rule in rule_book.keys():
                if value in rule_book[rule]:
                    flag = False
            if flag:
                not_valid.append(value)
                valid_ticket = False
        if valid_ticket:
            valid_tickets.append(ticket)

    return [sum(not_valid), valid_tickets, rule_book, your_ticket]


def p2(data):
    rules = data[1]
    valid_tickets = data[0]
    your_ticket = data[2]
    magnitude = len(valid_tickets)
    positions = dict()
    for key in rules.keys():
        positions[key] = []
    # print("Rules: {}".format(rules))
    # print("Valid Tickets: {}".format(valid_tickets))
    # print("Your Ticket: {}".format(your_ticket))
    for ticket in valid_tickets:
        for key in rules.keys():
            for i, v in enumerate(ticket):
                if v in rules[key]:
                    positions[key].append(i)

    indexes = set([i for i in range(0, len(your_ticket))])

    for key, value in positions.items():
        positions[key] = [k for k, v in Counter(
            value).items() if (v == magnitude) and (k in indexes)]
        if len(positions[key]) == 1:
            indexes.remove(positions[key][0])

    for i in range(0, len(your_ticket)):
        if len(indexes) == 0:
            break
        for key in positions.keys():
            if len(positions[key]) == 1:
                continue

            positions[key] = [x for x in positions[key] if x in indexes]
            if len(positions[key]) == 1:
                indexes.remove(positions[key][0])

    total = 1
    for key, value in positions.items():
        if "departure" in key:
            total = total * your_ticket[value[0]]

    return total


data = open('data/day16.txt', 'r').read().split("\n\n")

results = validity(data)

print("Part 1: "+str(results[0]))
print("Part 2: "+str(p2(results[1:])))
