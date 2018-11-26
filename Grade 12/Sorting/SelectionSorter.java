public class SelectionSorter implements Sorter
{
    public void sort (int num, int list[])
    {
        int i, j, temp, small;


        for (i = 0 ; i < num ; i++)
        {
            small = i;
            for (j = i + 1 ; j < num ; j++)
            {
                if (list [j] < list [small])
                {
                    small = j;
                }
            }
            temp = list [i];
            list [i] = list [small];
            list [small] = temp;
        }
    }
}
