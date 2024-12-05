import sys


def solution(input_file_path: str):
    with open(input_file_path, "r") as input:
        for line in input:
            pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Pass a test input argument")
        sys.exit(1)

    solution(sys.argv[1])
