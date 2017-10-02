#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/timeb.h> 

int get_histogram(FILE *file_ptr, long hist[], int block_size, long *milliseconds, long *total_bytes_read){
	char buf[block_size + 1];
	int bytes_read;
	memset(buf, '\0', block_size + 1);
	
	struct timeb t;
	ftime(&t);
	long now_in_ms = t.time * 1000 + t.millitm;
	
	while((bytes_read = fread(buf, 1, block_size, file_ptr)) == block_size){
		for(int i = 0; i < block_size; i++){
			if(buf[i] >= 'A' && buf[i] <= 'Z'){
				hist[buf[i] - 'A']++;
				//printf("%ld\n", hist[buf[i] - 'A']);
			}
		}
		*total_bytes_read += bytes_read;
	}
	//scan the leftover in the buffer
	if(bytes_read != 0){
		for(int i = 0; i < block_size; i++){
			if(buf[i] >= 'A' && buf[i] <= 'Z'){
				hist[buf[i] - 'A'] += 1;
			}
		}
		*total_bytes_read += bytes_read;
	}
	
	ftime(&t);
	*milliseconds = (t.time * 1000 + t.millitm) - now_in_ms;
	return 0;
}


int main(int argc, char **argv){
	int block_size = atoi(argv[2]);
	char *filename = argv[1];
	long milliseconds;
	long filelen;
	long hist[26];
	
	memset(hist, 0, 26*sizeof(long));
	FILE *fp = fopen(filename, "r");
	
	int ret = (int) get_histogram(fp, hist, block_size, &milliseconds, &filelen);
	//assert(! ret < 0);
	
	fclose(fp);
	
	//printf("Computed the histogram in %d ms.\n", milliseconds);
	for(int i=0; i < 26; i++) {
		printf("%c %ld\n", 'A' + i, hist[i]);
	}
	printf("BLOCK SIZE %d bytes\n", block_size);
	printf("TOTAL BYTES %ld bytes\n", filelen);
	printf("TIME %ld milliseconds\n", milliseconds);
	printf("DATA RATE %f Bps\n", (double)filelen/milliseconds * 1000);
	
	return 0;
}
