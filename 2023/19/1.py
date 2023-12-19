import sys

categs = {
'x': 0,
'm': 1,
'a': 2,
's': 3
}

workflows = {}
summ = 0

for line in sys.stdin:
    if len(line) > 2:
        ps = line.find('{')
        if ps > 0:
            wf = line[:ps]
            rules = []
            for rule in line[ps + 1, len(line) - 1].split(','):
                ps = rule.find(':')
                if ps == -1:
                    rules.append((lambda rates: rates[0] > -1, rule))
                else:
                    if rule[1] == '<':
                        rules.append((lambda rates: rates[categs[rule[0]]] < int(rule[2:]), rule[ps + 1:]))
                    else:
                        rules.append((lambda rates: rates[categs[rule[0]]] > int(rule[2:]), rule[ps + 1:]))
            workflows[wf] = rules
        else:
            rates = line[1:-1].split(',')
            part = [0] * 4
            for rate in rates:
                part[categs[rate[0]]] = int(rate[2:])
            wf = 'in'
            while not wf in ['A', 'R']:
                rules = workflows[wf]
                for rule in rules:
                    if rule[0](part):
                        wf = rule[1]
                        break
            if wf == 'A':
                summ += sum(part)
                
print(summ)