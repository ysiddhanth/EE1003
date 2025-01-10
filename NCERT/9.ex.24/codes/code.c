#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

int main(){
        double h=0.01, n= 200, x = 0,y=1,yp=y, y_pr = 1, y_pp = 1;
        double a = 1 + h - (h*h) / 2, b = 1 - h + (h*h) / 2, c = -2*h / b;
        FILE *file;
	file = fopen("values.dat", "w");
        fprintf(file, "x y\n");
        for(int i=0;i<=n;i++){
            fprintf(file,"%lf %lf\n", x,y);
            x += h;
            yp = y;
            y_pp = y_pr;
            y = yp + (h / 2) * (y_pr * (a / b) + c * y + y_pr);
            y_pr = y_pp*(a / b) + (c * yp);
        }
	fclose(file);
	printf("Results have been written to values.dat\n");
	return 0;
}





