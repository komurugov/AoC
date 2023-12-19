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
            for rule in line[ps + 1:-2].split(','):
                ps = rule.find(':')
                if ps == -1:
                    rules.append((0, '>', -1, rule))
                else:
                    rules.append((categs[rule[0]],
                                rule[1],
                                int(rule[2:ps]),
                                rule[ps + 1:]
                    ))
            workflows[wf] = rules
        else:
            rates = line[1:-2].split(',')
            part = [0] * 4
            for rate in rates:
                part[categs[rate[0]]] = int(rate[2:])
            print(part)
            wf = 'in'
            while not wf in ['A', 'R']:
                rules = workflows[wf]
                for rule in rules:
                    if (rule[1] == '<' and part[rule[0]] < rule[2]) or (rule[1] == '>' and part[rule[0]] > rule[2]):
                        wf = rule[3]
                        print(wf)
                        break
            if wf == 'A':
                print(part[0])
                summ += sum(part)
                
print(workflows['rfg'])
                
print(summ)
# < 791714