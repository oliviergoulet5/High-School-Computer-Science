public class InsertionSorter implements Sorter
{
    public void sort (int num, int list[])
    {
        int i, j, k, temp;


        for (i = 1 ; i < num ; i++)
        {
            for (j = 0 ; j < i ; j++)
            {
                temp = list [i];
                if (temp < list [j])
                {
                    for (k = i ; k > j ; k--)
                    {
                        list [k] = list [k - 1];
                    }
                    list [j] = temp;
                }
            }
        }
    }
}


