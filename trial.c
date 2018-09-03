#include<stdio.h>
int p()
{
	printf("%d\n",6+6);
}
int main()
{
	int (*q)      () = &p;
	(*q)      ();
}