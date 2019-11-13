//import java.util.*;
import java.util.HashMap; 
import java.util.Map; 
public final class ImmutableDemo{

	
	private final int age;
	
	@SuppressWarnings("unchecked")
	private HashMap map; 
	

	@SuppressWarnings("unchecked")
	public ImmutableDemo(int age,HashMap map){
		this.age = age;
		this.map = new HashMap(map);
		
	}
	
	public int getAge(){
		return this.age;
	}
	
	@SuppressWarnings("unchecked")
	public HashMap getMap(){
		return new HashMap(this.map);
	}
	
	public static void main(String[] args){
		
		//
	}


}
