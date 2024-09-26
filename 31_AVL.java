class Node {
    int key, height;
    Node left, right;

    Node(int d) {
        key = d;
        height = 1;
    }
}

class AVLTree {

    int height(Node N) {
        if (N == null)
            return 0;
        return N.height;
    }

  
    Node rightRotate(Node y) {
        Node x = y.left;
        Node T2 = x.right;


        x.right = y;
        y.left = T2;


        y.height = Math.max(height(y.left), height(y.right)) + 1;
        x.height = Math.max(height(x.left), height(x.right)) + 1;

        return x;
    }
