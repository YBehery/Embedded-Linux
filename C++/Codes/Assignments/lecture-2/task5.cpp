#include<iostream>

void func(int arr[],int even[],int odd[],int size)
{
    int even_i=0;
    int odd_i=0;
    for(int i=0;i<size;i++)
    {
        if(arr[i]%2==0)
        {
            even[even_i]=arr[i];
            even_i++;
        }
        else
        {
            odd[odd_i]=arr[i];
            odd_i++;
        }

    }
    for(int i=0;i<even_i;i++)
    {
        std::cout<<"even:"<<even[i]<<std::endl;
    }
    std::cout<<"________________________\n";
    for(int i=0;i<odd_i;i++)
    {
        std::cout<<"odd:"<<odd[i]<<std::endl    ;    
    }
}
int main()
{
    int arr[]={1,2,3,4,5,6,7,8,9,10};
    int even_arr[10];
    int odd_arr[10];
    func(arr,even_arr,odd_arr,sizeof(arr)/sizeof(int));
    
    return 1;
}