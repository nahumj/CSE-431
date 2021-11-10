#include <iostream>
#include <cstdint>
#include <bitset>
#include <iomanip>


uint32_t reverse_bitwise(uint32_t input) {
  uint32_t result = 0;
  while (input) {
    result <<= 1;
    if (input & 1) {
      result ^= 1;
    }    
    input >>= 1;
  }
  return result;
}



bool alternating_bits(uint32_t input) {
  uint32_t shifted = input << 1;
  uint32_t xorred = input ^ shifted; 
  uint32_t check = xorred & (xorred + 1);
  return !check;
}


int main() {
  uint32_t input = 0b11010101;
  std::cout << "Input = " << std::bitset<32>(input) << std::endl;
  // uint32_t other = input;
  // uint32_t bit_locator = 1 << 3;
  // other |= bit_locator;
  // uint32_t shifted = input;
  // shifted <<= 1;
  // std::cout << "shifted = " << std::bitset<32>(shifted) << std::endl;

  // uint32_t xorred = input ^ shifted;  
  // std::cout << "xorred = " << std::bitset<32>(xorred) << std::endl;

  // uint32_t check = xorred & (xorred + 1);
  // std::cout << "check = " << std::bitset<32>(check) << std::endl;



  std::cout << std::boolalpha;
  std::cout << "Output =" <<std::bitset<32>(reverse_bitwise(input)) << std::endl;


  return 0;

}