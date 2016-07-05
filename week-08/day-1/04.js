'use strict';

// Automated CarPark system
//
// All the dates in this examples should be stored as a number
// The milliseconds lasted from 1970-01-01
//
// Create a Car constructor
// it should take 3 parameters
//  - type: the cars type as a string (eg: 'volvo')
//  - color: the cars type as a string (eg: 'red')
//  - balance: the cars parking credis as a number (eg: 500)
//
// every car should have an id property (a number), that is
// unique for all the cars, staeting form 0
//
// Methods:
// enter(enterDate)
//  - it should store the date of entering
//
// getEnterDate()
//  - it should return the date of the last entering
//
// leave(price)
//  - it should decrease the balance with the price of the parking (that is given in an argument)
//
// getStats()
//  - it should give back a string like:
//    "Type: volvo, Color: red, Balance: 500"
//
//
// Create a CarPark constructor
// it should take 2 parameters
//  - income: the initial credits as a number (eg: 4000)
//  - startTime: the current date
//
// The parking fee: 40 per hours (only every whole hour)
//
// Methods:
// carEnter(car)
//  - It should add a car to the garage and add its stored startTime
//
// carLeave(id)
//  - It should remove the car with the given id and it should charge from its balance
//
// elapseTime(hours)
//  - It should increment the time with the hours
//
// Optional Methods:
//
// getStats()
//  - It should return a string like:
//    "Cars: 4, Time: 1234423453, Income: 1400"
//
// getParkingCarsSince(hours)
//  - It should return the number of cars that are parking since the given hours

var idCounter = 0;
function Car(type, color, balance) {
  this.type = type;
  this.color = color;
  this.balance = balance;
  this.id = idCounter;
  idCounter++;
}

Car.prototype.enter = function(enterDate) {
  this.enterDate = enterDate;
};

Car.prototype.getEnterDate = function() {
  return this.enterDate;
};

Car.prototype.leave = function(price) {
  this.balance -= price;
};

Car.prototype.getStats = function() {
  return "Type: " + this.type + ", Color: " + this.color + ", Balance: this.balance";
};

function CarPark(income, startTime) {
  this.income = income;
  this.startTime = startTime;
  this.fee = 40;
  this.cars = [];
}

CarPark.prototype.carEnter = function(cars) {
  this.cars.push(cars);
  cars.enter(this.startTime);
};

var j;
CarPark.prototype.carLeave = function(id) {
  var _this = this;
  this.cars.forEach(function(e, i) {
    if (e.id === id) {
      var charge = _this.fee * (_this.startTime - e.getEnterDate()) / 3600000;
      e.leave(charge);
      _this.income += charge;
      j = i;
    }
  });
  this.cars.splice(j, 1);
};

CarPark.prototype.elapseTime = function(hours) {
  this.startTime += 3600000 * hours;
};

CarPark.prototype.getStats = function() {
  return "Cars: " + this.cars.length + ", Time: " + this.startTime + ", Income: " + this.income
};

var car1 = new Car('volvo', 'red', 500);
var car2 = new Car('mazda', 'blue', 600);
var car3 = new Car('lada', 'yellow', 300);
var park = new CarPark(1000, new Date().getTime());
park.carEnter(car1);
park.carEnter(car3);
park.carEnter(car2);
console.log(park);
park.elapseTime(5);
console.log(park);
park.carLeave(1);
park.elapseTime(5);
park.carEnter(car2);
console.log(park);
console.log(park.getStats());
