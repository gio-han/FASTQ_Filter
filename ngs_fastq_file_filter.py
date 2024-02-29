with open("seq_sample.fastq") as in_file: # opens input file
	seq_list = in_file.readlines() # reads file to list
	q_score_list = seq_list[3::4] # creates list only containing Q scores
avg_read_score_list = [] # creates empty list for each read's average Q score
for read_q_scores in q_score_list: # outer for loop works through Q scores for each read
	read_q_scores = read_q_scores.rstrip() # removes newline character to right
	ascii_score_list = [] # makes empty list for ascii Q scores
	for q_score in read_q_scores: # inner for loop works through Q score for each base
		ascii_score = ord(q_score) - 64 # converts Q scores to ascii - 64
		ascii_score_list.append(ascii_score) # adds ascii Q score to end of list
	# calculates each read's average ascii Q score
	avg_read_score = sum(ascii_score_list) / len(ascii_score_list)
	avg_read_score_list.append(avg_read_score) # adds each read's ascii Q score to end of list

out_file_1 = open("seq_output_1.fastq", "w") # opens first output file to write to
out_file_2 = open("seq_output_2.fastq", "w") # opens second output file to write to
seq_list_index = 0 # sets value of index variable as 0
# outer for loop works through pairs of average scores
for count in range(0, len(avg_read_score_list), 2):
	avg_1 = avg_read_score_list[count] # assigns value to average score for read 1
	avg_2 = avg_read_score_list[count+1] # assigns value to average score for read 2
	if avg_1 and avg_2 >= 30: # checks conditions for 1st output file
		# takes slice with all fastq info for pair of reads
		paired_end_read = seq_list[seq_list_index:seq_list_index+8]
		# inner for loop works through each line of fastq info for pair of reads
		for line in paired_end_read:
			out_file_1.write(line) # writes line to 1st output file
		seq_list_index += 8 # updates index variable
	elif avg_1 or avg_2 < 30: # checks conditions for 2nd output file
		# takes slice with all fastq info for pair of reads
		paired_end_read = seq_list[seq_list_index:seq_list_index+8]
		# inner for loop works through each line of fastq info for pair of reads
		for line in paired_end_read:
			out_file_2.write(line) # writes line to 2nd output file
		seq_list_index += 8 # updates index variable
	else: seq_list_index += 8 # mops up every other scenario and updates index
out_file_1.close() # closes 1st output file
out_file_2.close() # closes 2nd output file