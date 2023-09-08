#include<iostream>

void merge (int arr1[],int arr2[],int merged[],int size1,int size2)
{
    for(int i=0;i<size1;i++)
    {
        merged[i]=arr1[i];
    }
    for(int i=size1;i<size2+size1;i++)
    {
        merged[i]=arr2[i-size1];
    }
}
int main()
{
    int arr1[]={1,2,3,4,5,6,7,8,9,10};
    int arr2[]={11,12,13,14,15,16,17,18,19,20};
    int merged_arr[100];
    merge(arr1,arr2,merged_arr,10,10);
    for(int i=0;i<(sizeof(arr1)+sizeof(arr2))/sizeof(int);i++)
    {
        std::cout<<merged_arr[i]<<std::endl;
    }
    return 1;
}