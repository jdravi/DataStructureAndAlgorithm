
import java.util.*;

class Node{
	
	public int data;
	public Node left;
	public Node right;
	public Node(int data){
			this.data = data;
			this.left = null;
			this.right = null;
	}

}
public class KDistanceNode{

	public Node head;
	public KDistanceNode(int data){
		this.head = new Node(data); 
	}
	

	public void addEdge(Node root,HashMap<Node,Node> map){
		
		if(root!=null){
		
			map.put(root.left,root);
			map.put(root.left,root);
			return;
		}return;
	}
	
	public int KDistanceUtil(Node root,int k){
	
		
		Node current  = root ;
		
		HashMap<Node,Node> map  = new HashMap<Node,Node>();
		map.put(root,null);
		addEdge(root,map);
		return 1;
		
	}

}
