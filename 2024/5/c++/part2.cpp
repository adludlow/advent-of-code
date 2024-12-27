#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <utility>
#include <vector>


struct update_order {
    std::vector<int> before;
    std::vector<int> after;
};

std::map<int, update_order> order_map;


bool validate_update(const std::vector<int> &update, const std::map<int, update_order> &order_map) {
    for (int i = 0; i < update.size(); i++) {
        try {
            update_order uo = order_map.at(update[i]);
            for (int j = i+1; j < update.size(); j++) {
                if (std::find(uo.before.begin(), uo.before.end(), update[j]) != uo.before.end()) {
                    continue;
                }
                return false;
            }
        }
        catch(const std::out_of_range& ex) {
            std::cout << update[i] << " not found" << std::endl;
        }
    }
    std::vector<int> update_ = update;
    std::reverse(update_.begin(), update_.end());
    for (int i = 0; i < update_.size(); i++) {
        try {
            update_order uo = order_map.at(update_[i]);
            for (int j = i+1; j < update_.size(); j++) {
                if (std::find(uo.after.begin(), uo.after.end(), update_[j]) != uo.after.end()) {
                    continue;
                }
                return false;
            }
        }
        catch(const std::out_of_range& ex) {
            std::cout << update_[i] << " not found" << std::endl;
        }
    }

    return true;
}

void print_update(const std::vector<int>& update) {
    for (int val : update) {
        std::cout << val << ",";
    }
    std::cout << std::endl;
}

std::vector<int> fix_update(const std::vector<int>& update) {
    std::vector<int> update_ = update;
    for (int i = 0; i < update_.size(); i++) {
        update_order uo = order_map.at(update_[i]);
        int val = update_[i];
        for (int j = i+1; j < update_.size(); j++) {
            int check_val = update_[j];
            if (std::find(uo.after.begin(), uo.after.end(), check_val) != uo.after.end()) {
                update_[i] = check_val;
                update_[j] = val;
                break;
            }
        }
    }
    return update_;
}

int main(int argc, char** argv) {
    std::ifstream input("input.txt");
    
    std::string line;
    std::vector<std::vector<int>> updates;
    std::vector<std::vector<int>> valid_updates;
    std::vector<std::vector<int>> invalid_updates;
    bool ordering = true;
    while (std::getline(input, line)) {
        std::string seg;
        std::stringstream line_stream(line);
        if (line.size() == 0) {
            ordering = false;
        }

        if (ordering) {
            std::vector<int> ordering_segs;
            while (std::getline(line_stream, seg, '|')) {
                ordering_segs.push_back(std::stoi(seg));
            }
            int key = ordering_segs[0];
            int value = ordering_segs[1];
            // Before
            if (order_map.find(key) != order_map.end()) {
                order_map[key].before.push_back(value);
            } else {
                order_map[key] = {
                    {value},
                    {}
                };
            }
            // After
            if (order_map.find(value) != order_map.end()) {
                order_map[value].after.push_back(key);
            } else {
                order_map[value] = {
                    {},
                    {key}
                };
            }
        } else if (line.size() == 0) {
            continue;
        } else {
            std::vector<int> update;
            while (std::getline(line_stream, seg, ',')) {
                update.push_back(std::stoi(seg));
            }
            updates.push_back(update);
        }
    }
    int mid_sum = 0;
    for (std::vector<int> update : updates) {
        if (validate_update(update, order_map)) {
            valid_updates.push_back(update);
            int mid = update[std::ceil(update.size()/2)];
            mid_sum += mid;
        } else {
            invalid_updates.push_back(update);
        }
    }
    
    mid_sum = 0;
    for (std::vector<int> update : invalid_updates) {
        while (!validate_update(update, order_map)) {
            update = fix_update(update);
        }
        int mid = update[std::ceil(update.size()/2)];
        mid_sum += mid;
    }

    std::cout << mid_sum << std::endl;
}