public class MergeSorter implements Sorter
{
    private int list[];
    private int num;
    private int temp[];


    public void sort (int theNum, int theList[])
    {
        num = theNum;
        list = theList;
        temp = new int [num];
        mergeSort (0, num - 1);
    }


    public void mergeSort (int first, int last)
    {
        int middle;
        if (last > first)
        {
            middle = (int) (first + last) / 2;
            mergeSort (first, middle);
            mergeSort (middle + 1, last);
            merge (first, middle, last);
        }
    }


    public void merge (int first, int middle, int last)
    {
        int point1, point2, point3;


        point1 = first;
        point2 = middle + 1;
        point3 = first;


        while (point3 <= last)
        {
         if ((point1<middle+1) && (point2>last || list[point1]<list[point2]))
            {
                temp [point3] = list [point1];
                point1++;
            }
            else
            {
                temp [point3] = list [point2];
                point2++;
            }
            point3++;
        }
        for (int i = first ; i <= last ; i++)
        {
            list [i] = temp [i];
        }
    }
}


