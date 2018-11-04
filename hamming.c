#include <stdio.h>

void main()
{
        int i;
        int cw[12];
        int dw[8];
        printf("Enter data word:\n");
        for(i=7;i>=0;i--)
        {
                scanf("%d",&dw[i]);
        }
        int j=7;
        for(i=11;i>=0;i--)
        {
                if(i==0 || i==1 || i==3 || i==7)
                {
                        cw[i]=0;
                }
                else
                {
                        cw[i]=dw[j];
                        j--;
                }
        }
        int rc1;
        rc1=cw[2]+cw[4]+cw[6]+cw[8]+cw[10];
        if(rc1%2==0)
                cw[0]=0;
        else
                cw[0]=1;

        int rc2=cw[2]+cw[5]+cw[6]+cw[9]+cw[10]+cw[11];
        if(rc2%2==0)
                cw[1]=0;
        else
                cw[1]=1;

        int rc3=cw[4]+cw[5]+cw[6];
        if(rc3%2==0)
         cw[3]=0;
        else
                cw[3]=1;

        int rc4=cw[8]+cw[9]+cw[10]+cw[11];
        if(rc4%2==0)
                cw[7]=0;
        else
                cw[7]=1;

        printf("Enter received codeword:");
        int rcw[12];
        for(i=11;i>=0;i--)
        scanf("%d",&rcw[i]);

        int err=0;
        for(i=0;i<11;i++)
        {
                if(cw[i]!=rcw[i])
                {
                        err=i+1;
                        break;
                }
        }
        if(err==0)
        printf("NO ERROR IN TRANMISSION");
        else
        printf("ERROR BIT=%d",err);

}
