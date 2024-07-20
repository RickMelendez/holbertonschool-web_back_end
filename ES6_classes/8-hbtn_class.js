export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // Override valueOf method
  valueOf() {
    return this._size;
  }

  // Override toString method
  toString() {
    return this._location;
  }
}
