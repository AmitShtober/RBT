# RBT
Implementation of Red-Black Tree using Python3.

# RBT
RBT (Red Black Tree) is a binary search tree which has the following red-black properties:
* Every node is either red or black.
* Every leaf (NULL) is black.
* If a node is red, then both its children are black.
* Every simple path from a node to a descendant leaf contains the same number of black nodes

![Red-black_tree_example svg](https://user-images.githubusercontent.com/5290591/159977120-54def971-cbff-4759-8a8a-6d3fd9bc06ec.png)

# Implementation
The current implementation pretty standard. Each node in the tree contains a numeric (int/double) value and you can create an RBTree and add items (with no duplicates). The implementation is based upon:
* https://www.cs.auckland.ac.nz/software/AlgAnim/red_black.html
* http://staff.ustc.edu.cn/~csli/graduate/algorithms/book6/chap14.htm


# To-Do
* Implement deletion of nodes
* Improve the current UnitTests (add more compilcated scenarios)
* Update the tree to hold any data, no only numeric values
