package facadeExample;

public class Waiter {
	public static String deliverFood(FoodType foodType) {
		Ingredient ingredient = new Ingredient () ;
		
		switch (foodType) {
			case PASTA:
				Menu pasta = new Pasta();
				String pastaItems = ingredient.getPastaItems();
				pasta.prepareFood(pastaItems);
				return pasta.deliverFood();
				
			case BURGER:
				Menu burger = new Burger();
				String burgerItems = ingredient.getBurgerItems();
				burger.prepareFood(burgerItems);
				return burger.deliverFood();
				
		}
		return null;
	}
}


