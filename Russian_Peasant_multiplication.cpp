#include "RPM_functions.cpp"
#include <iostream>
#include <ostream>
#include <vector>

int check_negative(int num);
bool check_char(int first, int second);
void printfinal(std::vector<int> first_col, std::vector<int> second_col);
void printfinal(int total, std::vector<int> odd_nums);

int main() {
  char user_repeat = 'y';
  std::cout << "Hello Russian Peasant Muiltplication.";
  do {

    int first_num = 0, second_num = 0, total = 0;
    char repeat = true;
    bool is_negative1 = false, is_negative2 = false;
    std::vector<int> odd_nums, first_col, second_col;

    while (repeat == true) {
      std::cout << std::endl;
      first_num = 0;
      second_num = 0;
      std::cout << "Enter the first number: ";
      std::cin >> first_num;

      if (check_negative(first_num) == -1) {
        is_negative1 = true;
        first_num *= check_negative(first_num);
      }
      std::cout << "Enter the second number: ";
      std::cin >> second_num;
      if (check_negative(second_num) == -1) {
        is_negative2 = true;
        second_num *= check_negative(second_num);
      }
      if (check_char(first_num, second_num) == true) {
        std::cout << "Invalid input or equals 0" << std::endl;
        exit(0);
      } else {
        repeat = false;
      }

      do {
        if ((second_num % 2) == 1) {
          total += first_num;
          odd_nums.push_back(first_num);
          first_col.push_back(first_num);
          second_col.push_back(second_num);
        }
        second_num /= 2;
        first_num *= 2;

      } while (second_num >= 1);
    }

    std::cout << std::endl
              << "------------------------------------------" << std::endl;
    printfinal(first_col, second_col);
    std::cout << "------------------------------------------" << std::endl;
    printfinal(total, odd_nums);
    if (is_negative1 == true) {
      total *= -1;
    }
    if (is_negative2 == true) {
      total *= -1;
    }
    std::cout << "The product of the two numbers is " << total;
    std::cout << std::endl;
    std::cout << "------------------------------------------" << std::endl;
    std::cout << "Would you like to do anyother calculation?(y/n)";
    std::cin >> user_repeat;
  } while (user_repeat == 'y');
  return 0;
}