const LinkedList = require('./LinkedList');

class Queue {
  constructor(maxSize = Infinity) {
    this.queue = new LinkedList();
    this.maxSize = maxSize;
    this.size = 0;
  }

  isEmpty() {
    return this.size === 0;
  }

  hasRoom() {
    return this.size < this.maxSize;
  }

  enqueue(data) {
    if (this.hasRoom()) {
      this.queue.addToTail(data);
      this.size++;
    } else {
      console.log('Queue is full!');
    }
  }

  dequeue() {
    if (!this.isEmpty()) {
      const data = this.queue.removeHead();
      this.size--;
      return data;
    } else {
      console.log('Queue is empty nothing to dequeue!');
    }
  }

  peek() {
    if (!this.isEmpty()) {
      console.log(`The first of the queue is ${this.queue.head.data}`);
    } else {
      console.log('The queue is empty');
    }
  }
}

const newQueue = new Queue(3);

newQueue.peek();

for (let i = 0; i < newQueue.maxSize; i++) {
  newQueue.enqueue(`new #${i + 1}`);
}

newQueue.enqueue('new #4');

newQueue.peek();

newQueue.dequeue();
newQueue.dequeue();
newQueue.dequeue();

try {
  newQueue.dequeue();
} catch (e) {
  console.log(e);
}

module.exports = Queue;
