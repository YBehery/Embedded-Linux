#include<iostream>

int main()
{
    int x,y,z;
    std::cin>>x>>y>>z;
    int max=x;
    if(max<y)
    {
        max=y;
    }
    if(max<z)
    {
        max=z;
    }
    std::cout << max << std::endl;
    return 0;
}