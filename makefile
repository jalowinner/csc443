CC = gcc
 
all: create_random_file get_histogram

create_random_file: create_random_file.c
		$(CC) -o create_random_file create_random_file.c
 
get_histogram: get_histogram.c
		$(CC) -o get_histogram get_histogram.c