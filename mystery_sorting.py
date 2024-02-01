import pandas as pd
import math
import os
import csv
import sys
import numpy as np
sys.path.append("../Sorting_Algorithms/.idea")
from sorting_algos import merge_sort


column_names= ['tconst', 'primaryTitle', 'originalTitle', 'startYear',
               'runtimeMinutes', 'genres', 'averageRating', 'numVotes', 'ordering',
               'category', 'job', 'seasonNumber', 'episodeNumber', 'primaryName', 'birthYear',
               'deathYear', 'primaryProfession']

####################################################################################
# Donot Modify this Code
####################################################################################
class FixedSizeList(list):
    def __init__(self, size):
        self.max_size = size

    def append(self, item):
        if len(self) >= self.max_size:
            raise Exception("Cannot add item. List is full.")
        else:
            super().append(item)

####################################################################################
# Mystery_Function
####################################################################################
def Mystery_Function(file_path, memory_limitation, columns):
    """
    # file_path :  file_path for Individual Folder (datatype : String)
    # memory_limitation : At each time how many records from the dataframe can be loaded (datatype : integer : 2000)
    # columns : the columns on which dataset needs to be sorted (datatype : list of strings)
    # Load the 2000 chunck of data every time into Data Structure called List of Sublists which is named as "chuncks_2000"
    # **NOTE : In this Mystery_Function records are accessed from only the folder Individual.

    #Store all the output files in Folder named "Final".
    #The below Syntax will help you to store the sorted files :
                # name_of_csv = "Final/Sorted_" + str(i + 1)
                # sorted_df.reset_index(drop=True).to_csv(name_of_csv, index=False)
    #Output csv files must be named in the format Sorted_1, Sorted_2,...., Sorted_93
    # ***NOTE : Every output csv file must have 2000 sorted records except for the last ouput csv file which might have less
                #than 2000 records.
    """

    #Need to Code
    #Helps to Sort all the 1,84,265 rows with limitation.

    #Load the 2000 chunck of data every time into Data Structure called List of Sublists which is named as "chuncks_2000"
    chuncks_2000=FixedSizeList(2000)
    fp_array = []
    Record_list = [0]*93
    for i in range(93):
        fp_array.append(open('Individual/sorted_'+str(i+1)+'.csv', 'r'))
        Record_list[i] = fp_array[i].readline().strip().split(',')
        for k in range(len(Record_list[i])):
            if 'primaryTitle' in columns and k!=columns.index('primaryTitle')+1 and Record_list[i][k].isdigit():
                Record_list[i][k] = int(Record_list[i][k])
    flag = 1
    Output_List = []
    switch = 0
    file_Number = 0
    while flag:
        for i in range(len(Record_list)):
            if Record_list[i]!=None:
                min = i
                break
        for i in range(len(Record_list)):
            if Record_list[i]!=None and Record_list[i][1:]<Record_list[min][1:]:
                min = i
        Output_List.append(Record_list[min])
        next_rec = fp_array[min].readline().strip().split(',')
        if next_rec == ['']:
            Record_list[min] = None
        else:
            for k in range(len(next_rec)):
                if 'primaryTitle' in columns and k!=columns.index('primaryTitle')+1 and next_rec[k].isdigit():
                    next_rec[k] = int(next_rec[k])
            Record_list[min] = next_rec
        file_name = "./Final/Sorted_" + str(file_Number + 1) + ".csv"
        if switch%2==0 and len(Output_List)==memory_limitation-93:
            # file_name = "./Final/Sorted_" + str(file_Number+1) + ".csv"
            with open(file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(Output_List)
            Output_List = []
            switch += 1
        if switch%2==1 and len(Output_List)==93:
            with open(file_name, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(Output_List)
            Output_List = []
            file_Number += 1
            switch += 1
        if Record_list == [None]*93:
            if len(Output_List)!=0:
                file_name = "./Final/Sorted_" + str(file_Number+1) + ".csv"
                with open(file_name, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(Output_List)
            flag = 0

####################################################################################
# Data Chuncks
####################################################################################
def data_chuncks(file_path, columns, memory_limitation):
        """
        # file_path : dataset file_path for imdb_dataset.csv (datatype : String)
        # columns : the columns on which dataset needs to be sorted (datatype : list of strings)
        # memory_limitation : At each time how many records from the dataframe can be loaded (datatype : integer)
        # Load the 2000 chunck of data every time into Data Structure called List of Sublists which is named as "chuncks_2000"
        # NOTE : This data_chuncks function uses the records from imdb_dataset. Only 2000 records needs to be loaded at a
                # Time in order to process for sorting using merge sort algorithm. After sorting 2000 records immediately
                # Store those 2000 sorted records into Floder named Individual by following Naming pattern given below.
        #Store all the output files in Folder named "Individual".
        #Output csv files must be named in the format Sorted_1, Sorted_2,...., Sorted_93
        #The below Syntax will help you to store the sorted files :
                    # name_of_csv = "Individual/Sorted_" + str(i + 1)
                    # sorted_df.reset_index(drop=True).to_csv(name_of_csv, index=False)

        # ***NOTE : Every output csv file must have 2000 sorted records except for the last ouput csv file which
                    might have less than 2000 records.

        Description:
        This code reads a CSV file, separates the data into chunks of data defined by the memory_limitation parameter,
        sorts each chunk of data by the specified columns using the merge_sort algorithm, and saves each sorted chunk
        as a separate CSV file. The chunk sets are determined by the number of rows in the file divided by the
        memory_limitation. The names of the sorted files are stored as "Individual/Sorted_" followed by a number
        starting from 1.
        """
        chuncks_2000=FixedSizeList(2000)

        current_index = 0
        for k in range(93):
            column_indxes = [column_names.index(i) for i in columns]
            column_indxes.insert(0,0)
            column_order = []
            for i in column_indxes:
                column_order.append(sorted(column_indxes).index(i))
            chuncks_2000   = pd.read_csv(file_path,index_col=column_order, usecols = column_indxes, skiprows = current_index, nrows = memory_limitation).reset_index()
            chuncks_2000 = chuncks_2000.values.tolist()
            chuncks_2000 = merge_sort(chuncks_2000,column_indxes)
            file_name = "./Individual/sorted_"+str(k+1)+".csv"
            with open(file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(chuncks_2000)
            current_index += memory_limitation



#Enable only one Function each from data_chuncks and Mystery_Function at a time

#Test Case 13
data_chuncks('imdb_dataset.csv', ['startYear'], 2000)

#Test Case 14
# data_chuncks('imdb_dataset.csv', ['primaryTitle'], 2000)

#Test Case 15
# data_chuncks('imdb_dataset.csv', ['startYear','runtimeMinutes' ,'primaryTitle'], 2000)


#Test Case 13
Mystery_Function("Individual", 2000, ['startYear'])

#Test Case 14
# Mystery_Function("Individual", 2000, ['primaryTitle'])

#Test Case 15
# Mystery_Function("Individual", 2000, ['startYear','runtimeMinutes' ,'primaryTitle'])
