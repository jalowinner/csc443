import subprocess;
import numpy as np;
import matplotlib.pyplot as plt;

def calculate_read_data_rate():
	executable_name = "create_rand_file";
	block_size_list = [100, 1000, 5000, 20000, 40000, 50000, 100000, 500000, 1000000, 2000000, 3000000]
	data_rates = []
	for i in range(11):
		fname = "test" + str(i) + ".txt";
		out = subprocess.check_output(["./get_histogram", fname, str(block_size_list[i])]);
		data = out.split("\n");
		out_list = data[-2].split(" ");
		data_rate = float(out_list[-2].strip()) / 1000;
		data_rates.append(data_rate);

	print(block_size_list);
	print(data_rates);
	plt.plot(block_size_list, data_rates, linestyle='-', marker='o', color='b',linewidth=2.0);
	plt.ylabel("data rate (b/ms)");
	plt.xlabel("block size (b)");
	plt.savefig('read_plot.png');
	plt.show();
	return;

if __name__ == "__main__":
	calculate_read_data_rate();