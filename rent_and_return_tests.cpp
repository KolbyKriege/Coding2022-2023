#include "car_class.h"
#include "weekly_schedule.cpp"
#include "weekly_schedule.h"
#include <iomanip>
#include <ios>
#include <iostream>
#include <ostream>
#include <string>
#include <vector>
using namespace std;

double Rent(string car, int day, vector<Car> &tempcar) {
  bool repeat = true;
  int DaysRented;
  day = day - 1;
  if (day > 6) {
    cout << "Sorry we do not rent out Saturday as we are not open.";
    return -1;
  } else if (day < 0) {
    cout << "Sorry pleace Enter a number (1-6)";
    return -1;
  }

  cout << "How many days are your renting your car?" << endl;
  cin >> DaysRented;
  for (int i = 0; i < tempcar.size(); i++) {
    if (car == tempcar[i].getModel()) {
      if ((DaysRented + day) >= 0 && (DaysRented + day) < 7) {
        if (tempcar[i].getAvailability(day) == true) {
          for (int j = 0; j < DaysRented; j++) {
            tempcar[i].setFirstDayRented(day);
            tempcar[i].setAvailability((day + j), false);
            tempcar[i].setDaysRented(DaysRented);
          }
          return (tempcar[i].getPrice() * tempcar[i].getDaysRented());
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
void return_car(vector<Car> &tempcar) {
  string car;
  string responce;
  cout << "Please enter the model of your returned car" << std::endl;
  cin >> car;
  int temp = 0;
  for (int i = 0; i < tempcar.size(); i++) {
    if (tempcar[i].getModel() == car) { // Checks and comferming the right car
      cout << "The car you are returning is " << tempcar[i].getMake() << " "
           << tempcar[i].getModel() << " which was rented for "
           << tempcar[i].getDaysRented() << " days" << endl;
      cout << "Please confirm this is the correct car(y/n)";
      cin >> responce;
      if (responce == "y") { // code to reset need values
        for (int j = -1; j <= tempcar[i].getDaysRented(); j++) {
          tempcar[i].setAvailability((j + tempcar[i].getFirstDayRented()),
                                     true);
        }
        tempcar[i].setDaysRented(0);
        tempcar[i].setFirstDayRented(0);
        cout << "Your rented car is returned" << std::endl;
        return; // no errors
      }
    }
  }
  cout << "Sorry that is not one of our cars."
       << endl; // Error if they missed typed or not some thing we have
  return;
}

Car chevyImpala;
Car fordTaurus;
Car volkswagenPassat;
Car toyotaCorolla;
Car hondaPilot;

int main() {
  string car;
  double test;
  int day;
  // Modify the Class Attributes
  chevyImpala.setMake("Chevy");
  chevyImpala.setModel("Impala");
  chevyImpala.setPrice(60);
  for (int i = 0; i != 7; i++) {
    chevyImpala.setAvailability(i, true);
  }
  fordTaurus.setMake("Ford");
  fordTaurus.setModel("Taurus");
  fordTaurus.setPrice(52);
  for (int i = 0; i != 7; i++) {
    fordTaurus.setAvailability(i, true);
  }
  volkswagenPassat.setMake("Volkswagen");
  volkswagenPassat.setModel("Passat");
  volkswagenPassat.setPrice(41);
  for (int i = 0; i != 7; i++) {
    volkswagenPassat.setAvailability(i, true);
  }
  toyotaCorolla.setMake("Toyota");
  toyotaCorolla.setModel("Corolla");
  toyotaCorolla.setPrice(29);
  for (int i = 0; i != 7; i++) {
    toyotaCorolla.setAvailability(i, true);
  }
  hondaPilot.setMake("Honda");
  hondaPilot.setModel("Pilot");
  hondaPilot.setPrice(60);
  for (int i = 0; i != 7; i++) {
    hondaPilot.setAvailability(i, true);
  }
  vector<Car> CarInstances{chevyImpala, fordTaurus, volkswagenPassat,
                           toyotaCorolla, hondaPilot};
  for (int i = 0; i < 5; i++) {
    cout << CarInstances[i].getModel() << " "
         << CarInstances[i].getAvailability(0) << endl;
  }

  printWeeklySchedule(CarInstances);

  cout << "Enter Cars name " << endl;
  cin >> car;

  cout << "Enter in Day of week Sun-saturday (1-7)" << endl;
  cin >> day;
    // gets need inoutes
  test = Rent(car, day, CarInstances);
  cout << "Price is: " << test << endl;
    // outputs price
  printWeeklySchedule(CarInstances); //print out the scheuile to see if rent work

  return_car(CarInstances);

  printWeeklySchedule(CarInstances); //print out to see if return worked
  return 0;
}