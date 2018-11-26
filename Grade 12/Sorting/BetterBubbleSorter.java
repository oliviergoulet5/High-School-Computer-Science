public class BetterBubbleSorter implements Sorter
{
    public void sort (int num, int list[])
    {
        int i, j = 0, temp;
        boolean swapped;


        do
        {
            swapped = false;
            for (i = 0 ; i < num - j - 1 ; i++)
            {
                if (list [i] > list [i + 1])
                {
                    temp = list [i];
                    list [i] = list [i + 1];
                    list [i + 1] = temp;
                    swapped = true;
                }
            }
            j++;
        }
        while (swapped);
    }
}