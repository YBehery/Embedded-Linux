#include<bitset>
#include<iostream>
#include<cmath>
int main()
{
    int NUMd,NUMb;
    std::cout << "enter decimal number :";
    std::cin>>NUMd;
    std::bitset<8> N (NUMd);
    std::cout<<"Binary : "<<N<<std::endl;
    int errflag=0;
    std::cout << "enter binary number :";
    std::cin>>NUMb;
    NUMd=0;
    for(int i=0;i<8;i++)
    {
        if(NUMb%10==0)
        {
            //do nothing
        }        
        else if(NUMb%10==1)
        {
            NUMd+=pow(2,i);
        }
        else
        {
            std::cout << "ERROR!" << std::endl;
            errflag=1;
            break;
        }
        NUMb/=10;
    }
    if(errflag==0)
    {
        std::cout<<"decimal : "<<NUMd<<std::endl;
    }
    return 0;
}