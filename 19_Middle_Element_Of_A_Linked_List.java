import java.util.*;

// Creation of a singly-linked list node that consists of fields, data and next
class Node {
    int data;
    Node next;

    // Constructor to initialize a new node with data and next pointer pointing to null
  // this keyword is a reference to the current object instance within a class.
    Node(int new_data) {
        this.data = new_data;
        this.next = null;
    }
}

Class Mid_list {

}

public class Find_Mid{

    Vector vector = new Vector<>();
    static int return_mid(Node head){
        if(head!=null){
            vector.add(head.data);
            head = head.next;
        }

        int mid_index = vector.size() / 2;

        return mid_index;


    }
}
