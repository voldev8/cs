class TreeNode {
  constructor(data) {
    this.data = data;
    this.children = [];
  }

  addChild(child) {
    if (child instanceof TreeNode) {
      this.children.push(child);
    } else {
      this.children.push(new TreeNode(child));
    }
  }

  removeChild(childToRemove) {
    const length = this.children.length;
    this.children = this.children.filter((child) => {
      return childToRemove instanceof TreeNode
        ? child !== childToRemove
        : child.data !== childToRemove;
    });
    if (length === this.children.length) {
      this.children.forEach((child) => (child) =>
        child.removeChild(childToRemove)
      );
    }
  }

  print(level = 0) {
    let result = '';
    for (let i = 0; i < level; i++) {
      result += '-- ';
    }
    console.log(`${result}${this.data}`);
    this.children.forEach((child) => child.print(level + 1));
  }

  depthFirstTraversal() {
    console.log(this.data);
    this.children.forEach((child) => child.depthFirstTraversal());
  }

  breadthFirstTraversal() {
    let queue = [this];
    while (queue.length > 0) {
      const current = queue.shift();
      console.log(current.data);
      queue = queue.concat(current.children);
    }
  }
}

const numbers = new TreeNode('Menu');

const entries = {
  1: ['11', '12', '13'],
  2: ['21', '34', '22'],
  3: ['31', '32', '33'],
};

const tens = Object.keys(entries);
for (let num = 0; num < tens.length; num++) {
  numbers.addChild(tens[num]);
  const entrylist = entries[tens[num]];
  entrylist.forEach((entry) => {
    numbers.children[num].addChild(entry);
  });
}

numbers.print();

numbers.children[1].removeChild('34');
numbers.children[2].addChild('34');

console.log('------- Corrected numbers');
numbers.print();

numbers.depthFirstTraversal();
