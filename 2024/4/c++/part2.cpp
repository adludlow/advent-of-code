#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

int STRING_LENGTH = 4;
const std::string MAS = "MAS";

std::vector<std::pair<int, int>> generate_string(int start_x, int x_add, int start_y, int y_add) {
    std::vector<std::pair<int, int>> str;
    int curr_x = start_x;
    int curr_y = start_y;
    for (int i = 1, j = 1; i <= STRING_LENGTH && j <= STRING_LENGTH; curr_x = curr_x + x_add, curr_y = curr_y + y_add, i++, j++) {
        str.push_back(std::pair<int, int>(curr_x, curr_y));
    }
    return str;
}

std::vector<std::vector<std::pair<int, int>>> generate_strings(int x, int y) {
    std::vector<std::vector<std::pair<int, int>>> strings;
    // up
    strings.push_back(generate_string(x, 0, y, -1));
    // diagonal right up
    strings.push_back(generate_string(x, 1, y, -1));
    // right
    strings.push_back(generate_string(x, 1, y, 0));
    // diagonal right down
    strings.push_back(generate_string(x, 1, y, 1));
    // down
    strings.push_back(generate_string(x, 0, y, 1));
    // diagonal left down
    strings.push_back(generate_string(x, -1, y, 1));
    // left
    strings.push_back(generate_string(x, -1, y, 0));
    // diagonal left up
    strings.push_back(generate_string(x, -1, y, -1));

    return strings;
}

std::pair<std::vector<std::pair<int, int>>, std::vector<std::pair<int, int>>> generate_x(int start_x, int start_y) {
    std::vector<std::pair<int, int>> x_1 = {
        {start_x, start_y},
        {start_x + 1, start_y + 1},
        {start_x + 2, start_y + 2},
    };
    std::vector<std::pair<int, int>> x_2 = {
        {start_x + 2, start_y},
        {start_x + 1, start_y + 1},
        {start_x + 0, start_y + 2},
    };

    return {x_1, x_2};
}

bool valid_string(std::vector<std::pair<int, int>> str, int max_x, int max_y) {
    for (std::pair<int, int> coords : str) {
        if (coords.first < 0 || coords.first >= max_x || coords.second < 0 || coords.second >= max_y) {
            return false;
        }
    }
    return true;
}

bool check_mas(std::vector<std::pair<int, int>> str, std::vector<std::vector<char>> matrix) {
    std::string candidate = "";
    for (std::pair<int, int> coords : str) {
        candidate += matrix[coords.second][coords.first];
        //std::cout << "(" << coords.first << "," << coords.second << "), ";
    }
    std::string candidate_2 = candidate;
    std::reverse(candidate_2.begin(), candidate_2.end());
    if (candidate == MAS || candidate_2 == MAS) {
        return true;
    }
    return false;

}

int main(int argc, char** argv) {
    std::vector<std::vector<char>> matrix;

    std::ifstream input("input.txt");
    
    std::string line;
    int i = 0;
    while (std::getline(input, line)) {
        std::istringstream iss(line);
        std::vector<char> chars;
        for (int j = 0; j < line.size(); j++) {
            chars.push_back(line[j]);

        }
        matrix.push_back(chars);
        i++;
    }
    int num_rows = matrix.size();
    int num_cols = matrix.front().size();

    std::vector<std::pair<std::vector<std::pair<int, int>>, std::vector<std::pair<int, int>>>> x_mas;
    for (int i = 0; i < num_rows; i++) {
        for (int j = 0; j < num_cols; j++) {
            std::pair<std::vector<std::pair<int, int>>, std::vector<std::pair<int, int>>> new_x_mas = generate_x(j, i);
            x_mas.push_back(new_x_mas);
        }
    }

    int match_count = 0;
    for (std::pair<std::vector<std::pair<int, int>>, std::vector<std::pair<int, int>>> str_pair: x_mas) {
        if (valid_string(str_pair.first, num_cols, num_rows) && valid_string(str_pair.second, num_cols, num_rows)) {
            if (check_mas(str_pair.first, matrix) && check_mas(str_pair.second, matrix)) {
                match_count++;
            }
        }
    }

    std::cout << match_count << std::endl;
}