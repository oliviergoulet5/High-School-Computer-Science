public class QuickSorter implements Sorter
{
    private int list[];
    private int num;


    public void sort (int theNum, int theList[])
    {
        num = theNum;
        list = theList;
        quickSort (0, num - 1);
    }




    public void quickSort (int left, int right)
    {
        int i, pivot, lastSmall;


        swap (left, (int) (left + right) / 2);
        lastSmall = left;


        for (i = left + 1 ; i <= right ; i++)
        {
            if (list [i] < list [left])
            {
                lastSmall++;
                swap (lastSmall, i);
            }
        }
        swap (left, lastSmall);
        pivot = lastSmall;
        if (left < pivot - 1)
        {
            quickSort (left, pivot - 1);
        }
        if (pivot + 1 < right)
        {
            quickSort (pivot + 1, right);
        }
    }




    private int temp;
    public void swap (int a, int b)
    {
        temp = list [a];
        list [a] = list [b];
        list [b] = temp;
    }
}