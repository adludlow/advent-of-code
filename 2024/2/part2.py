def check_safe(report: list[int]) -> bool:
    if report[0] < report[1]:
        # increasing
        for i in range(len(report) - 1):
            diff = report[i+1] - report[i] 
            if diff >= 1 and diff <= 3:
                continue
            else:
                return False
    elif report[0] > report[1]:
        for i in range(len(report) - 1):
            # decreasing
            diff = report[i] - report[i+1] 
            if diff >= 1 and diff <= 3:
                continue
            else:
                return False
    else:
        return False
    return True

def check_safe_level_removed(report: list[int]) -> bool:
    if check_safe(report):
        return True

    tmp_report = report.copy()
    for i in range(len(report)):
        del tmp_report[i]
        if check_safe(tmp_report):
            return True
        tmp_report = report.copy()
    return False

with open("input.txt", "r") as f:
    reports = [[int(level) for level in l.split(" ")] for l in f]
    safe_reports = [r for r in reports if check_safe_level_removed(r)]
    print(len(safe_reports))

