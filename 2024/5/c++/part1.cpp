#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

bool validate_update(std::vector<std::string> update, const std::map<std::string, std::string> &ordering_map) {

}

int main(int argc, char** argv) {
    std::ifstream input("test_input.txt");
    
    std::string line;
    std::vector<std::string> ordering_segs;
    std::map<std::string, std::string> ordering_map;
    std::vector<std::vector<std::string>> update_segs;
    bool ordering = true;
    while (std::getline(input, line)) {
        std::string seg;
        std::stringstream line_stream(line);
        if (line.size() == 0) {
            ordering = false;
        }

        if (ordering) {
            while (std::getline(line_stream, seg, '|')) {
                ordering_segs.push_back(seg);
            }
            ordering_map = {ordering_segs[0], ordering_segs[1]};
        } else {
            std::vector<std::string> update;
            while (std::getline(line_stream, seg, ',')) {
                update.push_back(seg);
            }
            update_segs.push_back(update);
        }
    }

    for (std::vector<std::string> update : update_segs) {

    }
}