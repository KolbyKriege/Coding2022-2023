#include "rent_and_return.h"
#include <iostream>
#include <ostream>
#include <vector>
using namespace std; // g++ main.cpp menu.cpp rent_and_return.cpp weekly_schedule.cpp -o a.out

// Function to Rent a car for starting data till friday
double Rent(string car, int day, vector<Car> &tempcar) {
  bool repeat = true;
  int DaysRented;
  day = day - 1;
  if (day > 6) { // Checks to see if days are correct
    cout << "Sorry we do not rent out Saturday as we are not open." << endl;
    return -1;
  } else if (day < 0) {
    cout << "Sorry pleace Enter a number (1-6)";
    return -1;
  }
  for (int i = 0; i < tempcar.size(); i++) {
    if (car == tempcar[i].getModel()) {
      if (tempcar[i].getDaysRented() > 0) { // Makes sure car is avaibale
        cout
            << "Sorry this Car is already rented this week and is not returned."
            << endl;
        return -1;
      }
    }
  }
  cout << "How many days are your renting your car?" << endl;
  cin >> DaysRented;
  for (int i = 0; i < tempcar.size(); i++) {
    if (car == tempcar[i].getModel()) {
      if ((DaysRented + day) >= 0 && (DaysRented + day) < 7) {
        if (tempcar[i].getAvailability(day) == true) { // many checks to make sure car can be rented in days
          for (int j = 0; j < DaysRented; j++) {
            tempcar[i].setFirstDayRented(day + 1); // changes to car so they are rented
            tempcar[i].setAvailability((day + j), false);
            tempcar[i].setDaysRented(DaysRented);
          }
          return (tempcar[i].getPrice() * tempcar[i].getDaysRented()); // return price
        } else {
          cout << "Sorry this car is not avabile please try again" << endl;
          return -1; // Requested car is not avalable
        }
      } else {
        cout << "Sorry you can only rent within the current week" << endl;
        return -1; // Error in user rent to far out
      }
    }
  }
  cout << "Sorry that is not a car we have. Please try again" << endl;
  return -1; // Error if user enters in a missed spell and not a car we have
}
// Function to return a car
void return_car(vector<Car> &tempcar) {
  string car;
  string responce;
  cout << "Please enter the model of your returned car" << std::endl;
  cout << "Impala, Taurus, Passat, Corolla, or Pilot: "; 
  cin >> car;
  for (int i = 0; i < tempcar.size(); i++) {
    if (tempcar[i].getModel() == car) { // Checks and comferming the right car
      cout << "The car you are returning is " << tempcar[i].getMake() << " "
           << tempcar[i].getModel() << " which was rented for "
           << tempcar[i].getDaysRented() << " days" << endl;
      cout << "Please confirm this is the correct car (y/n): ";
      cin >> responce;
      if (responce == "y") { // code to reset need values
        if (tempcar[i].getDaysRented() == 0) {
          return;
        }
        for (int j = -1; j <= tempcar[i].getDaysRented(); j++) { // resets values
          tempcar[i].setAvailability((j + tempcar[i].getFirstDayRented()),
                                     true);
        }
        tempcar[i].setDaysRented(0);
        tempcar[i].setFirstDayRented(0);
        cout << " Thank you :). Your rented car is returned" << std::endl;
        return; // no errors
      }
    }
    // cout << "Sorry this car is not rented";
    // return;
  }
  cout << "Sorry that is not one of our cars."
       << endl; // Error if they missed typed or not some thing we have
  return;
}