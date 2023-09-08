#include<iostream>
#include <algorithm>

int main()
{
    char choice;
    std::cin>>choice;//A or D
    auto func=[choice](int a,int b){
        if(choice=='A')
        {
            return a<b;
        }
        else{
            return a>b;
        }
    };
    int arr[]={5,6,71,0,5,8,999};
    std::sort(arr,arr+(sizeof(arr)/sizeof(int)),func);
    for(int i=0;i<sizeof(arr)/sizeof(int);i++)
    {
        std::cout<<arr[i]<<std::endl;
    }
    return 1;

}