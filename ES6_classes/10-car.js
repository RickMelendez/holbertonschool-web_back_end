class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    // Return an instance of the same class as the original object
    return new this.constructor(this._brand, this._motor, this._color);
  }
}

export default Car;
