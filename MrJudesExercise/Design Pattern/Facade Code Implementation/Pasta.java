package facadeExample;

public class Pasta implements Menu {
	public String preparedItem;
	@Override 
	public void prepareFood (String itemsRequired) {
		preparedItem="Making the spaghet with ingredients -"+ itemsRequired;
	}
	
	public String deliverFood() {
		return preparedItem;
	}
}
