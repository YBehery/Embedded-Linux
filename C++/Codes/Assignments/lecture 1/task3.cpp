#include<iostream>
#include <cmath>
int main()
{
    int x,y,z;
    std::cin>>x>>y>>z;
    if(((pow(x,2)+pow(y,2))==pow(z,2))||((pow(x,2)+pow(z,2))==pow(y,2))||((pow(y,2)+pow(z,2))==pow(x,2)))
    {
        std::cout << "IS Right Angle" << std::endl;
    }
    else
    {
        std::cout << "NOT RIGHT angle" << std::endl;
    }

}