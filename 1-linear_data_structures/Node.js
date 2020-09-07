class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }

  setNextNode(node) {
    if (node instanceof Node || node === null) {
      this.next = node;
    } else {
      throw new Error('Next node must be a member of the Node class.');
    }
  }

  getNextNode() {
    return this.next;
  }
}

// const firstNode = new Node('No 1');
// const secondNode = new Node('No 2');
// const thirdNode = new Node('No 3');

// firstNode.setNextNode(secondNode);
// secondNode.setNextNode(thirdNode);

// let currentNode = firstNode;
// while (currentNode !== null) {
//   console.log(currentNode.data);
//   currentNode = currentNode.getNextNode();
// }

module.exports = Node;
