#include<iostream>

int main()
{
    int x;
    std::cin>>x;
    int sum=0;
    int temp=x;
    while(temp!=0)
    {
        sum+=temp%10;
        temp/=10;
    }
    std::cout << sum << std::endl;
    return 0;
}