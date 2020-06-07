package facadeExample;

public class Customer {
	public static void main(String[] args) {
		
	System.out.println("----output using facade----");
	System.out.println(Waiter.deliverFood(FoodType.PASTA));
	System.out.println(Waiter.deliverFood(FoodType.BURGER));
	}
}	

