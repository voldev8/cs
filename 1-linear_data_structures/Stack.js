const LinkedList = require('./LinkedList');

class Stack {
  constructor(maxSize = Infinity) {
    this.stack = new LinkedList();
    this.maxSize = maxSize;
    this.size = 0;
  }

  hasRoom() {
    return this.size < this.maxSize;
  }

  isEmpty() {
    return this.size === 0;
  }

  push(value) {
    if (this.hasRoom()) {
      this.stack.addToHead(value);
      this.size++;
    } else {
      // throw new Error('Stack is full')
      console.log('Stack is full');
    }
  }

  pop() {
    if (!this.isEmpty()) {
      const value = this.stack.removeHead();
      this.size--;
      return value;
    } else {
      console.log('Stack is empty');
    }
  }

  peek() {
    if (!this.isEmpty()) {
      return this.stack.head.data;
    } else {
      return null;
    }
  }
}

// const newStack = new Stack(6);

// for (let i = 0; i < newStack.maxSize; i++) {
//   newStack.push(`new #${i + 1}`);
// }

// try {
//   newStack.push('new #7');
// } catch (e) {
//   console.log(e);
// }

// console.log(`The top the stack ${newStack.peek()}`);

// newStack.pop();
// newStack.pop();
// newStack.pop();
// newStack.pop();
// newStack.pop();
// newStack.pop();

// try {
//   newStack.pop();
// } catch (e) {
//   console.log(e);
// }

module.exports = Stack;
