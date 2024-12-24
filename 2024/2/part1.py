def check_safe(report: list[int]) -> bool:
    print(report)
    if report[0] < report[1]:
        print("increasing")
        # increasing
        for i in range(len(report) - 1):
            diff = report[i+1] - report[i] 
            if diff >= 1 and diff <= 3:
                print(f"{diff} safe diff")
                continue
            else:
                return False
    elif report[0] > report[1]:
        print("decreasing")
        for i in range(len(report) - 1):
            # decreasing
            diff = report[i] - report[i+1] 
            if diff >= 1 and diff <= 3:
                print(f"{diff} safe diff")
                continue
            else:
                return False
    else:
        return False
    return True

with open("input.txt", "r") as f:
    reports = [[int(level) for level in l.split(" ")] for l in f]
    safe_reports = [r for r in reports if check_safe(r)]
    print(safe_reports)
    print(len(safe_reports))

