#include <iostream>
#include <vector>
int main()
{
    std::vector<char> c={'a','e','i','o','u'};
    char a;
    int flag=0;
    std::cin>>a;
    for(char t:c)
    {
        if(a==t)
        {
            flag=1;
            std::cout<<"IS vowel"<<std::endl;
        }
    }
    if(flag==0)
    {
        std::cout<<"NOT vowel"<<std::endl;
    }
    return 0;
}