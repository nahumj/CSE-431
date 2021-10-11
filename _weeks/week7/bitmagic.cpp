#include <bitset>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <set>
#include <vector>

int find_lonely_number_set(const std::vector<int>& vec) {
  std::set<int> seen;
  int total_sum = 0;
  for (int value : vec) {
    if (seen.find(value) == seen.end()) {
      seen.insert(value);
    }
    total_sum += value;
  }
  int sum_of_seen = std::accumulate(seen.begin(), seen.end(), 0);
  return 2 * sum_of_seen - total_sum;
}

int find_lonely_number_xor(const std::vector<int>& vec) {
  int result = 0;
  for (int value : vec) {
    result ^= value;
  }
  return result;
}

bool alternating_bits(uint32_t input) {
  uint32_t shifted_left = input >> 1;
  uint32_t xor_with_self = input ^ shifted_left;
  return !(xor_with_self & (xor_with_self + 1));
}

bool is_power_of_2(uint32_t input) { return input && !(input & (input - 1)); }

uint32_t reverse_bitwise(uint32_t input) {
  uint32_t result = 0;
  while (input) {
    result <<= 1;
    if (input & 1 == 1) {
      result ^= 1;
    }
    input >>= 1;
  }
  return result;
}

int main() {
  std::vector<int> vec = {1, 3, 7, 3, 2, 1, 7};
  std::cout << find_lonely_number_set(vec) << std::endl;

  uint32_t input = 0b1100100;
  std::cout << std::bitset<32>(input) << std::endl;
  std::cout << std::bitset<32>(reverse_bitwise(input)) << std::endl;
  std::cout << is_power_of_2(input) << std::endl;
  std::cout << is_power_of_2(1 << 5) << std::endl;
  std::cout << alternating_bits(0b10101010) << std::endl;
  std::cout << alternating_bits(0b1001010101) << std::endl;

  return 0;
}