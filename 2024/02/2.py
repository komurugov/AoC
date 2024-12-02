def IsDifferenceOk(difference, increasing):
    if increasing:
        return difference in (1, 2, 3)
    else:
        return difference in (-1, -2, -3)

def IsReportSafe(report):
    if len(report) < 2:
        return True
    increasing = report[1] > report[0]
    for i in range(1, len(report)):
        if not IsDifferenceOk(report[i] - report[i - 1], increasing):
            return False
    return True

def IsReportAlmostSafe(report):
    if IsReportSafe(report):
        return True
    for i in range(0, len(report)):
        if IsReportSafe(report[:i] + report[i + 1:]):
            return True
    return False

import sys

Reports = []

for line in sys.stdin:
    Reports.append([int(level) for level in line.split()])

AlmostSafeReportsCount = 0

for report in Reports:
    if IsReportAlmostSafe(report):
        AlmostSafeReportsCount += 1

print(AlmostSafeReportsCount)