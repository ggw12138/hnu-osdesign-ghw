#include <iostream>
#include <cmath>
using namespace std;
int judgearr[16]={1};
int change(int *arr1)
{
    int c=0;
    for(int i=0;i<4;i++)
    {
        c+=arr1[i]*pow(2,3-i);
    }
    return c;
}
void DFS(int *arr1,int *arr2)
{
    if(arr1[0]==0&&arr1[1]==0&&arr1[2]==0&&arr1[3]==0)   //最终结束状态判断
    {
        return;
    }
    if(judgearr[0]==1)
    {
        if((arr1[1]==arr1[2])||(arr1[2]==arr1[3]))   //判断是否为安全的状态
        {
            if(arr1[0]!=arr1[2])
            {
                return;
            }
            int temp=arr1[0];    //农夫坐船到对岸
            arr1[0]=arr2[0];
            arr2[0]=temp;
            for(int i=1;i<4;i++)   //选择一个可以携带的物品
            {
                int temp1=arr1[i];  //如果物品和农夫状态相同则可以携带
                if(temp==temp1&&judgearr[change(arr1)]==1)
                {
                    arr1[i]=arr2[i];  //可以携带后交换携带物品的状态
                    arr2[i]=temp1;
                    for(int j=0;j<4;j++)
                    {
                        cout<<arr1[j];
                    }
                    cout<<" ";
                    for(int j=0;j<4;j++)
                    {
                        cout<<arr2[j];
                    }
                    cout<<endl;
                    judgearr[change(arr1)]=0;
                    DFS(arr1,arr2);   //进入下一次的递归
                }
                else          //如果状态不相同则不可以携带，选择下一个物品
                {
                    continue;
                }
            }
        }
    }
    
}
int main() {
    int arr1[4]={1,1,1,1};  //左：人，狼，羊，菜
    int arr2[4]={0,0,0,0};  //右，人，狼，羊，菜
    DFS(arr1,arr2);
    return 0;
}