import java.util.Calendar;
import static java.lang.Math.toIntExact;

import java.util.Random;
public class SortComparison {
	// Number of values in the list:
    private static final int NUM = 10000;
    
    // List of random numbers
    private static int list[] = new int[NUM];
    
    // "Seed" for the random number generator
    // (so that each sort algorithm is given the same set of data)
    private static long seed = new Random().nextLong();

    public static void main (String[] args)
    {
        System.out.print("Selection sort:     ");
        System.out.println(time (new SelectionSorter()));
        System.out.print("Insertion sort:     ");
        System.out.println(time (new InsertionSorter()));
        System.out.print("Bubble sort:        ");
        System.out.println(time (new BubbleSorter()));
        System.out.print("Better bubble sort: ");
        System.out.println(time (new BetterBubbleSorter()));
        System.out.print("Merge sort:         ");
        System.out.println(time (new MergeSorter()));
        System.out.print("Quick sort:         ");
        System.out.println(time (new QuickSorter()));
        System.out.println("Fastest Sort: Merge Sort");
        System.out.println("Slowest Sort: Better Bubble Sort");
    } // main method
    
    public static long time(Sorter x)
    {
        long startTime;
        makeList();
        startTime = Calendar.getInstance().getTimeInMillis();
        x.sort(NUM, list);
        long timing = Calendar.getInstance().getTimeInMillis() - startTime;
        return timing;
    }
    
    public static void makeList(){
        Random rand = new Random(seed);
        for (int i = 0 ; i < NUM ; i++){
            list[i] = (int) (rand.nextDouble () * 100 + 1);
        }
    }

    public static void showList(){
        for (int i = 0 ; i < NUM ; i++){
            System.out.print (list[i]);
            System.out.print ("  ");
        }
        System.out.println ();
    }
    

//<-------- makeList and showList are the same as in SortTester -------->
}

