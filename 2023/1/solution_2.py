digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def get_first_digit(s: str) -> str:
    for i in range(0, len(s)):
        if s[i].isdigit():
            return s[i]
        for name, d in digits.items():
            if s[i:i+len(name)] == name or s[i:i+len(name)] == name[::-1]:
                return d

def get_last_digit(s: str) -> str:
    return get_first_digit(s[::-1])

def solution():
    result = 0
    with open("input.txt", "r") as input:
        lines = [line.rstrip() for line in input]
        for l in lines:
            val = int(f"{get_first_digit(l)}{get_last_digit(l)}")
            print(val)
            result = result + val
        
        print(result)

if __name__ == "__main__":
    solution()