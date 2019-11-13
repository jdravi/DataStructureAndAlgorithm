public class InnerClassDemo{

	private String name = "Ravi";
	private static String ceo = "I dont Know";
	public class InnerClassNonStatic{
		
		public void get(){
		
			System.out.println("Inside Normal inner class " + name);
		}
	}

	public static class InnerClassStatic{
		
		public void get(){
		
			System.out.println("Inside Normal inner class " + ceo);
		}
	}



	public static void main(String[] args){
	
		InnerClassDemo.InnerClassNonStatic inner = new InnerClassDemo().new InnerClassNonStatic();

		InnerClassDemo.InnerClassStatic nested = new InnerClassDemo.InnerClassStatic();	
		inner.get();
		nested.get();
	
	}
}
