#include<stdio.h>
#include<time.h>
#include<string.h>
int main()
{
int i,f;
printf("ENTER NUMBER OF FRAMES:\n");
scanf("%d",&f);
here:for(i=0;i<f;i++)
{
printf("Sending frame %d\n",i);
}
time_t s,e;
s=clock();
printf("ENTER THE LAST FRAME RECEIVED:\n");
int ans;
scanf("%d",&ans);
e=clock();
if((e-s)>100)
{
printf("TIME EXCEEDED, RE TRANSMITTING
DATA=============================\n");
goto here;
}
else
{
if(ans==f-1)
printf("TRANSACTION COMPLETE :)");
else
{
printf("TRANSMISSION ERROR, RE TRANSMITTING
DATA==========================\n");
goto here;
}
}
printf("%d",e-s);
return 0;
}
