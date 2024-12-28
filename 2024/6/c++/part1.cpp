#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>


typedef std::pair<int, int> position;

enum position_type {
    empty,
    obstacle,
};

std::map<char, position_type> position_type_map = {
    {'.', empty},
    {'^', empty},
    {'>', empty},
    {'V', empty},
    {'<', empty},
    {'#', obstacle}
};

std::string directions = "^>V<";
std::map<char, std::pair<int, int>> direction_map = {
    {'^', {0, -1}},
    {'>', {1, 0}},
    {'V', {0, 1}},
    {'<', {-1, 0}}
};

std::map<std::pair<int, int>, std::pair<int, int>> next_direction_map = {
    {{0, -1}, {1, 0}},
    {{1, 0}, {0, 1}},
    {{0, 1}, {-1, 0}},
    {{-1, 0}, {0, -1}}
};

struct guard_position {
    position pos;
    std::pair<int, int> direction;
};

std::vector<std::vector<position_type>> game_map;
int main(int argc, char** argv) {
    std::ifstream input("input.txt");
    
    std::string line;
    bool ordering = true;
    int y = 0;
    guard_position curr_guard_pos;
    while (std::getline(input, line)) {
        if (game_map.size() == y) {
            game_map.push_back(std::vector<position_type>());
        }
        for (int x = 0; x < line.size(); x++) {
            char chr = line[x];
            game_map[y].push_back(position_type_map[chr]);
            if (directions.find(chr) != std::string::npos) {
                curr_guard_pos = {
                    {x, y},
                    direction_map[chr]
                };
            }
        }
        y++;
    }
    int max_y = game_map.size();
    int max_x = game_map.front().size();
    bool in_room = true;
    std::set<position> positions_visited = {curr_guard_pos.pos};
    while (in_room) {
        position next_pos = {
            curr_guard_pos.pos.first + curr_guard_pos.direction.first,
            curr_guard_pos.pos.second + curr_guard_pos.direction.second
        };
        
        // Check in room
        if (next_pos.first < 0 || next_pos.second < 0 || next_pos.first >= max_x || next_pos.second >= max_y) {
            in_room = false;
            break;
        }

        position_type next_pos_type = game_map[next_pos.second][next_pos.first];
        guard_position next_guard_pos = {
            next_pos,
            curr_guard_pos.direction
        };
        if (next_pos_type == obstacle) {
            next_guard_pos.direction = next_direction_map[next_guard_pos.direction];
            next_guard_pos.pos = curr_guard_pos.pos;
        }
        curr_guard_pos = next_guard_pos;

        positions_visited.insert(curr_guard_pos.pos);
    }
    std::cout << positions_visited.size() << std::endl;
}