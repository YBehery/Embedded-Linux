#include<iostream>
#include<vector>
void delete_ele(int arr[],int size,int num)
{
    for(int i=0;i<size;i++)
    {
        if(arr[i]==num)
        {
            for(int j=i;j<10-1;j++)
            {
                arr[j]=arr[j+1];
            }
        }
    }
}
int main()
{
    int arr[]={1,2,3,4,5,6,7,8,9,10};
    int num;
    std::cin>>num;
    delete_ele(arr,10,num);
    for(int i=0;i<10;i++)
    {
        std::cout<<arr[i]<<std::endl;
    }
    return 1;
}