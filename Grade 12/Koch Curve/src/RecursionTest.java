
public class RecursionTest {
	public RecursionTest(){}
	public static long factorial(long n)
	{
		System.out.println(n);
		if (n == 0){
			return 1;
		}
		else{
			return n * factorial(n-1);
		}
	}
}
