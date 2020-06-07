package facadeExample;

public class Burger implements Menu{
	public String preparedItem;
	@Override 
	public void prepareFood (String itemsRequired) {
		preparedItem="Making the Burger with ingredients -"+ itemsRequired;
	}
	
	public String deliverFood() {
		return preparedItem;
	}
}

