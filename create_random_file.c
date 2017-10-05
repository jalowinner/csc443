#include <stdlib.h>
#include <sys/timeb.h> 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void random_array(char *array, long bytes){
	long i;
	memset(array, '\0', sizeof(char) * (bytes + 1));
	for(i = 0; i < bytes; i++){
		array[i] = 'A' +(rand() % 26);
	}
}

int main(int argc, char **argv){
	long block_size = atol(argv[3]);
	long total_size = atol(argv[2]);
	char *filename = argv[1];
 	
	char buf[block_size + 1];
	struct timeb t;
	ftime(&t);
	
	FILE *fp = fopen(filename, "w");
	
	long now_in_ms = t.time * 1000 + t.millitm;
	
	while(total_size > block_size){
		random_array(buf, block_size);
		fwrite(buf, 1, block_size, fp);
		fflush(fp);
		total_size -= block_size;
	}

	random_array(buf, total_size);
	fwrite(buf, 1, total_size, fp);
	fflush(fp);
	total_size -= block_size;
	
	
	ftime(&t);
	long running_time = (t.time * 1000 + t.millitm) - now_in_ms;
	
	fclose(fp);

	printf("Running time is: %ld.\n", running_time);
	return 0;
}

