# Mystery_Sorting

How to RUN:



Project Description
 Sorting is used time and again in many day-to-day life activities. While brute force way to sort is easy to build and simple to apply in any situation, the cost of implementing brute force increases exponentially as the size and complexity of the data increases. So, in this project, you will implement various algorithms to efficiently sort a real-world dataset. In particular, you will be implementing 6 sorting algorithms namely Insertion sort, Selection sort, Quick sort, Heap sort, Shell sort, and Merge sort. And in addition, you will get to see how the time to compute differs for each algorithm. 
 
Dataset 
For this project you will be using the IMDb dataset. The required data is extracted and provided as CSV files.

imdb_dataset.csv file
The dataset file includes the following attributes as columns.

tconst – a unique identifier for each movie primaryTitle – the popular title that is used for   promotions originalTitle – original title in the original language
StartYear – release year of the title/ start year of a series runtimeMinutes – primary run time of title in minutes genres – includes up to three genres associated with the title averageRating – weighted average of all individual user ratings numVotes – number of votes the title has received ordering – a number to uniquely identify the rows for a given title category – the category of job that person was in seasonNumber – season number the episode belongs to
episodeNumber – episode number of tconst in the TV series primaryName – name by which the person is most often credited birthYear – in YYYY format deathYear – in YYYY format if applicable, else ‘\N’
PrimaryProfession – top 3 professions of the person


Mystery_Function.py
You will need to write code for test cases #13, #14, and #15 in the mystery_function.py file. Here, you have a memory limitation. Meaning that now you can only load 2,000 data samples at a time. Because of this limitation, you cannot sort the entire dataset at once.

def data_chuncks(file_path, columns, memory_limitation)
This function loads 2,000 data samples at a time and sorts them using merge_sort() that you have already implemented. Then each sorted chunk (with 2,000 data samples) will be stored as an individual output file.
The total dataset contains 1,84,265 data samples. Every time, you must load and sort 2,000 samples. This will result in 93 output files. 
Note that the last file (i.e., the 93rd file) will have less than 2,000 data samples.
All output files must be stored under a directory named ‘./Individual/’.
Each output file must use the following name format: ‘sorted_x.csv’, where x indicates the number of files starting from 1 and ending with 93.
As a result, you will have the following output files: ‘./Individual/sorted_1.csv’, ‘./Individual/sorted_2.csv’, ‘./Individual/sorted_3.csv’,     …     ‘./Individual/sorted_93.csv’ 
def Mystery_Function(file_path, memory_limitation, columns):
This function uses 93 individually sorted files (i.e., the output files of data_chuncks()) to sort entire data samples.
The function also has the same memory limitation. That is, you can load and store 2,000 data samples at most.
You may load 2,000 data samples from any of these files you like. For example, student_1 can take 700 data samples from sorted_1.csv, 1,000 data samples from sorted_6.csv, and the remaining 300 from sorted_50.csv. Student_2 can choose 500 samples from sorted_1.csv, sorted_2.csv, sorted_3.csv, and sorted_4.csv.
You may have temporary files to store intermediate sorting results. The temporary files must meet the memory limitation. (At most 2,000 samples).
Finally, all sorted output files must be stored under a directory named ‘./Final/’.
There must be 93 final output files. Any temporary files must not be stored.
As a result, you will have the following output files: ‘./Final/sorted_1.csv’, ‘./Final/sorted_2.csv’,  ‘./Final/sorted_3.csv’,     …     ‘./Final/sorted_93.csv’
Note that the data items should be in ascending order using the given columns. That is, if we have 10,000 numbers from 1 to 10,000. The ‘Final/sorted_1.csv’ file should have 1-2000 in ascending order, ‘Final/sorted_2.csv’ file should have 2001 – 4000 in ascending order, and so on.

chuncks_2000 :
List data structure named “chuncks_2000” where you need to store 2000 records at a time from the dataset. 
You should only use this data structure to load the 2000 records per time from “imd_dataset.csv” or the file “Individual” incase of implementing “data_chuncks” as well as “Mystery_Function” functions.




Test cases #13-#15
Each test case will assess the efficient sorting of a given column combination with a memory limitation of 2,000 items. 
