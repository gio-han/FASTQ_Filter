""" The Python script below reads FASTQ files and filters out any read pairs
where at least one of the sequences has an average Q score below 30. The
script outputs 2 files. The first will contain the sequences where both reads
have an average score above and including, 30 and the second those sequences
that have at least 1 read with an average score below 30. """


def filter_reads(file_name):
    """ A function that filters reads based on
    Q scores and writes to output files. """

    with open(file_name) as in_file:
        all_lines = in_file.readlines()

    # Getting the quality score lines.
    q_score_lines = all_lines[3::4]

    good_reads = []
    bad_reads = []
    index = 0

    # Processing the reads in pairs.
    for count in range(0, len(q_score_lines), 2):
        q_scores_read_1 = [ord(q_score) - 64
                           for q_score in q_score_lines[count].rstrip()]
        q_scores_read_2 = [ord(q_score) - 64
                           for q_score in q_score_lines[count+1].rstrip()]

        avg_q_read_1 = sum(q_scores_read_1) / len(q_scores_read_1)
        avg_q_read_2 = sum(q_scores_read_2) / len(q_scores_read_2)

        if avg_q_read_1 >= 30 and avg_q_read_2 >= 30:
            good_reads.extend(all_lines[index : index+8])
            index = index+8
        else:
            bad_reads.extend(all_lines[index: index+8])
            index = index+8

    # Writing to the output files and closing them.
    with open("seq_output_1.fastq", "w") as out_file_1:
        out_file_1.writelines(good_reads)
    out_file_1.close()

    with open("seq_output_2.fastq", "w") as out_file_2:
        out_file_2.writelines(bad_reads)
    out_file_2.close()


# Calling the function to initiate filtering.
filter_reads("seq_sample.fastq")


# End-of-File (EOF)
