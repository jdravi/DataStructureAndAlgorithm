public class SingltonObject{

	
	private static class helper{
	
		public static final SingltonObject instance = new SingltonObject();
		
	}

	private SingltonObject(){
	}

	public static SingltonObject getInstance(){
	
		return helper.instance;
	}

}


