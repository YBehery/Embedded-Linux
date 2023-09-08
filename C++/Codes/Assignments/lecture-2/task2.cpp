#include <iostream>

int get(int arr[], int size, int num)
{
	char flag = -1;
	for (int i = 0; i < size; i++)
	{
		if (arr[i] == num)
		{
			flag = i;
		}
	}
	return flag;
}
int main()
{
	int num;
	int arr[] = { 5,1,3,4,100,251,313 };
	std::cin >> num;
	if (get(arr, sizeof(arr) / sizeof(int), num) == -1)
		std::cout << "number not found";
	else
		std::cout << get(arr, sizeof(arr) / sizeof(int), num);
	while(1)
	{ }
	
}