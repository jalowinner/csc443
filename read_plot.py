import subprocess;
import numpy as np;
import matplotlib.pyplot as plt;
import matplotlib;

def calculate_read_data_rate(loop_time):
	f = open('read_rand_data.txt', 'a+');
	i = 128;
	block_size_list = [];
	while i < (3*1024*1024):
		block_size_list.append(i);
		i = i*2;
	fastest_block_index_count = len(block_size_list)*[0];
	for j in range(loop_time):
		data_rates = []
		max_rate = 0;
		max_block_index = 0;
		for i in range(len(block_size_list)):
			fname = "test" + str(i+1) + ".txt";
			out = subprocess.check_output(["./get_histogram", fname, str(block_size_list[i])]);
			data = out.split("\n");
			out_list = data[-2].split(" ");
			data_rate = int(float(out_list[-2].strip()) / 1000);
			data_rates.append(data_rate);
			if data_rate > max_rate:
				max_rate = data_rate;
				max_block_index = i;

		f.write('Block size:\n');
		f.write(str(block_size_list)+'\n');
		f.write('Data rate:\n');
		f.write(str(data_rates)+'\n');
		max_block_size = block_size_list[max_block_index];
		single_info = "max rate: "+str(max_rate)+", "+"optimal_block_size: "+str(max_block_size)+"\n\n";
		f.write(single_info);
		
		plt.figure(j+1);
		plt.plot(block_size_list, data_rates, linestyle='-', marker='o', color='b',linewidth=2.0);
		plt.ylabel("data rate (b/ms)");
		plt.xlabel("block size (b)");
		label_text = "max:" + str(max_rate) + " " + "block:" + str(max_block_size);
		plt.annotate(label_text, xy=(max_block_size, max_rate), xytext=(max_block_size+20000, max_rate+20000), arrowprops=dict(facecolor='black', shrink=0.05))
		plt.ylim(0,600000);
		plt.xscale('log');
		plt.xticks(block_size_list);
		plt.axes().get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter());
		plt.axes().tick_params(axis='x', labelsize=13);
		plt.xticks(rotation=30);
		plt.margins(x=0);
		save_fig_name = 'read_plot_' + str(j+1) + '.png';
		plt.savefig(save_fig_name, bbox_inches="tight");
		print(str(j+1)+"th iteration ends");
		fastest_block_index_count[max_block_index] += 1;

	max_count_index = 0;
	optimal_index = 0;
	for x in range(len(block_size_list)):
		if fastest_block_index_count[x] > max_count_index:
			max_count_index = fastest_block_index_count[x];
			optimal_index = x;

	f.write('OPTIMAL BLOCK SIZE: ' + str(block_size_list[optimal_index]));
	f.close();

if __name__ == "__main__":
	calculate_read_data_rate(10);



