import subprocess;

def calculate_read_data_rate():
	executable_name = "create_rand_file";
	block_size_list = [100, 1000, 5000, 20000, 50000, 100000, 500000, 1000000, 2000000, 3000000]
	data_rate = []
	for i in range(10):
		fname = "test" + str(i) + ".txt";
		out = subprocess.check_output(["./create_rand_file", fname, str(30000000), str(block_size_list[i])]);
		data = out.split(":");
		data_rate.append(data.strip()[:-1]);
		
		