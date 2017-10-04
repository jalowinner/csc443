CC = gcc
 
create_random_file: create_rand_file.c
		$(CC) -o create_random_file create_rand_file.c
 
get_histogram: histogram.c
		$(CC) -o get_histogram histogram.c