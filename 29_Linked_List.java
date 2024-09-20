
class Node {
    int data;
    Node next;


    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}


class LinkedList {
    Node head; 

    public void append(int data) {
        Node newNode = new Node(data); 
        
       
        if (head == null) {
            head = newNode;
            return;
        }

      
        Node last = head;
        while (last.next != null) {
            last = last.next;
        }

        
        last.next = newNode;
    }

  
    public void prepend(int data) {
        Node newNode = new Node(data); // Create a new node
        newNode.next = head; // Make the new node point to the old head
        head = newNode; // Make the new node the new head
    }

  
    public void deleteNode(int key) {
        Node current = head;
        Node prev = null;

        
        if (current != null && current.data == key) {
            head = current.next; // Change the head
            return;
        }

        // Search for the key and keep track of the previous node
        while (current != null && current.data != key) {
            prev = current;
            current = current.next;
        }

        // If the key was not found
        if (current == null) return;

        // Unlink the node from the list
        prev.next = current.next;
    }

    // Method to print the entire linked list
    public void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " = ");
            current = current.next;
        }
        System.out.println("null");
    }

    public static void main(String[] args) {
        LinkedList llist = new LinkedList();

     
        llist.append(1);
        llist.append(2);
     

        System.out.println("Initial List:");
        llist.printList();

        llist.deleteNode(2);
        System.out.println("\nList after deleting node with value 2:");
        llist.printList();
    }
}

