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

    public static void main(String[] args){
	Scanner n_input = new Scanner(System.in);
	
	System.out.print("Enter number of nodes :");
	int n = n_input.nextInt();

	if (n =< ){
		System.out.println("the number of must be positive. ");
		return -1;
	    }

	
	System.out.println("Enter the value for node 1: ");
	Node head = new Node(n_input.nextInt());
	Node current = head;
	
	for(int i = 2; i =< n; i++){
		System.out.println("Emter the valude for node " + i + ": ");
		current.next = new Node(n_input.nextInt());
		current = current.next;
	    }

	System.out.println("middle value is: " + Find_Mid);

	n_input.close():
        }
    }

}
