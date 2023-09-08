#include<iostream>
#include<math.h>

int main()
{
    auto func=[](int x){
        return pow(x,2);
    };
    int x;
    std::cin>>x;
    std::cout<<func(x);
    return 1;
}