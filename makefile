CC = gcc
 
all: create_rand_file get_histogram

create_random_file: create_rand_file.c
		$(CC) -o create_random_file create_rand_file.c
 
get_histogram: histogram.c
		$(CC) -o get_histogram histogram.c