public class BubbleSorter implements Sorter
{
    public void sort (int num, int list[])
    {
        int i, j, temp;


        for (j = 0 ; j < num - 1 ; j++)
        {
            for (i = 0 ; i < num - j - 1 ; i++)
            {
                if (list [i] > list [i + 1])
                {
                    temp = list [i];
                    list [i] = list [i + 1];
                    list [i + 1] = temp;
                }
            }
        }
    }
}