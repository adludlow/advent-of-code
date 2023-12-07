def get_first_digit(s: str) -> str:
    for c in s:
        if c.isdigit():
            return c

def get_last_digit(s: str) -> str:
    return get_first_digit(reversed(s))

def solution():
    result = 0
    with open("input.txt", "r") as input:
        lines = [line.rstrip() for line in input]
        for l in lines:
            val = int(f"{get_first_digit(l)}{get_last_digit(l)}")
            result = result + val
        
        print(result)

if __name__ == "__main__":
    solution()