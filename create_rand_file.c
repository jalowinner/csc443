#include <stdlib.h>
#include <sys/timeb.h> 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
char c = 'A' + (rand() % 26);
struct timeb t;
ftime(&t);
long now_in_ms = t.time * 1000 + t.millitm;

long block_size = ...;
char *buf = ...
 
FILE *fp = fopen(filename, "w");
fwrite(buf, 1, block_size, fp);
fflush(fp);
 
fclose(fp);

void random_array(char *array, long bytes){
	
}

int main(){

}
