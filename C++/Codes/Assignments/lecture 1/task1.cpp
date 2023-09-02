#include<iostream>
#include <iomanip>
int main()
{
    
    std::cout <<std::setw(1)<< "|"<<std::setw(5)<<"Char"<<std::setw(1)<< "|"<<std::setw(5)<< "ASCII"<<std::setw(1)<< "|" << std::endl;
    std::cout << "-------------" << std::endl;  
    for (int i=33;i<128;i++)
    {
       // std::cout << (char)i <<std::endl;
        std::cout <<std::setw(1)<< "|"<<std::setw(5)<<char(i)<<std::setw(1)<< "|"<<std::setw(5)<< i<<std::setw(1)<< "|" << std::endl;
    }
    return 0;
}