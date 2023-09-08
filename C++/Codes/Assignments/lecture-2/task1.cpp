#include <iostream>

int get_max(int arr[],int size)
{
	int max = 0;
	for (int i = 0; i < size; i++)
	{
		if (arr[i] > max)
			max = arr[i];
	}
	return max;
}
void main()
{
	int arr[] = { 5,1,3,4,100,251,313 };
	std::cout<<get_max(arr, sizeof(arr)/sizeof(int));
}