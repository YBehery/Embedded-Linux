#include<iostream>

int main()
{
    for(int i=1;i<=10;i++)
    {
        for(int k=0;k<=10;k++)
        {
            std::cout << i<<'*'<<k <<'='<<i*k<< std::endl;
        }
    }
}