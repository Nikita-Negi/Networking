#include<stdio.h>
#include<time.h>
#include<string.h>
int main()
{
int i,f,c=0;
int sf[20],rf[20],ep[20];
printf("ENTER NUMBER OF FRAMES:\n");
scanf("%d",&f);
for(i=0;i<f;i++)
{
printf("Sending frame %d=%d\n",i,i);
sf[i]=i;
}
printf("ENTER THE FRAMES RECEIVED:\n");
for(i=0;i<f;i++)
{
scanf("%d",&rf[i]);
if(rf[i]!=sf[i])
{
c++;
ep[i]=1;
}
else
ep[i]=0;
}
if(c==0)
{
printf("NO ERROR IN TRANSMISSION=======================\n");
}
else
{
printf("RETRANSMITTING INCORRECT FRAMES==================\n");
for(i=0;i<f;i++)
{
if(ep[i]==1)
{
printf("Resending frame %d\n",i);
rf[i]=i;
}
}
printf("NEW RECEIVED FRAMES:==============================\n");
for(i=0;i<f;i++)
{
printf("Frame %d=%d\n",i,rf[i]);
}
}
}
