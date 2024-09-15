
class Node {
    int key;
    Node left, right;

    public Node(int item) {
        key = item;
        left = right = null;
    }
}

class BinarySearchTree {
 
    Node root;

    
    BinarySearchTree() {
        root = null;
    }


    void insert(int key) {
        root = insertRec(root, key);
    }

    
    Node insertRec(Node root, int key) {
        
        if (root == null) {
            root = new Node(key);
            return root;
        }

        
        if (key < root.key)
            root.left = insertRec(root.left, key);
        else if (key > root.key)
            root.right = insertRec(root.right, key);

 
        return root;
    }

   
    boolean search(int key) {
        return searchRec(root, key);
    }

    // Recursive function to search for a key
    boolean searchRec(Node root, int key) {
        // Base case: root is null or key is present at root
        if (root == null || root.key == key)
            return root != null;

        // Key is smaller than root's key
        if (key < root.key)
            return searchRec(root.left, key);

        // Key is greater than root's key
        return searchRec(root.right, key);
    }

    // This method calls the recursive inOrderRec() method
    void inOrder() {
        inOrderRec(root);
    }

    // A utility function to do in-order traversal of BST
    void inOrderRec(Node root) {
        if (root != null) {
            inOrderRec(root.left);
            System.out.print(root.key + " ");
            inOrderRec(root.right);
        }
    }


    public static void main(String[] args) {
        BinarySearchTree bst = new BinarySearchTree();

      
        bst.insert(50);
        bst.insert(30);


        System.out.println("In-order traversal:");
        bst.inOrder();


        System.out.println("\nSearch 40: " + bst.search(40));
        System.out.println("Search 90: " + bst.search(90));
    }
}
