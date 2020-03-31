# CS5352
# Project 1: Retrieving, comparing, and presenting process profiling data
An examination into extracting system and user level information of running programs and use them to compare the efficiency of two algorithms 
 
This program looks at the comparison of implementing a hash function with two different collision-resolution methods to see which one is better in terms of how taxing it is on a system.
The two collision methods that will be examined are separate chaining and quadratic probing (open addressing).
Given below is a comparison between the two methods from a high-level point of view:

| Separate Chaining                                                   | Quadratic Probing                                |
|---------------------------------------------------------------------|--------------------------------------------------|
| Easier to implement                                                 |  Requires more computation                       |
| Table never becomes full                                            | Table may become full                            |
| Increase in storage                                                 | Fixed Size                                       |
| Cache performance not as good since  keys are stored in linked list | Better cache performance everything on one table |


## Results
After implementing both methods system and user level information was taken using the psutil library and self-made functions to see if a conclusion could be made on which method was the best/more efficient.
Before getting to the results some terms must be defined to better understand how to examine the two methods
 
|                                                                |                                                        |
|----------------------------------------------------------------|--------------------------------------------------------|
| RSS (Resident Set Size)                                        | Non-swapped physical memory a process has used         |
| VMS (Resident Set Size)                                        | The total amount of virtual memory used by the process |
| Paged_pool, peak_page_pool, nonpaged_pool, peak_nonpaged_pool, | Deal with memory usage by the program                  |
| pagefile, peaked_pagefile, private                             | Deal with memory usage by program                      |

Based upon reviewing the results it was shown that the program that had implemented quadratic probing came out on top. 
While the two functions had somewhat similar statistics, the quadratic probing program was able to hash the randomly
generated list of 100000 numbers in about half the time as the separate (inserting into the hash took 310.198 ms vs 608.374 ms
in the separate chaining program). Furthermore, the Quadratic probing program used less memory (in terms of RSS and VSS)
compared to the separate chaining program, though it was at the expense in the number of page faults seen. The full statistics 
of this project are offered below

### Chaining  
The screen shot below provides details on the performance of the program that implemented Separate Chaining 
#### System Level Information:
##### CPU Info:
1. CPU Percentage -  100%
##### Running Time:
1. Total Running time - 1630.613 ms
2. Running Time to add number into hash - 608.374ms
##### Memory Usage:
1. RSS - 89419776 Bytes 
2. VMS - 82264064 Bytes
3. Pagefile - 82264064 Bytes
##### Page Faults:
1. Number of Page Faults - 38137
##### Hard Drive Usage:
1. Read Bytes - 851325 Bytes
2. Write Bytes - 1676 Bytes

![ScreenShot](https://github.com/just331/CS5352/blob/master/Project%201/p1_separate-chaining_results.PNG)

### Quadratic Probing
The screen shot below provides details on the performance of the program that implemented Quadratic Probing 
#### System Level Information:
##### CPU Info:
1. CPU Percentage - 99.1 %
##### Running Time:
1. Total Running time -  1339.391 ms
2. Running time to insert into hash - 310.198 ms 
##### Memory Usage:
1. RSS - 144789504 Bytes
2. VMS - 367177728 Bytes
3. Pagefile - 367177728 Bytes
##### Page Faults:
1. Number of Page Faults - 51760
##### Hard Drive Usage:
1. Read Bytes -  6766303 Bytes
2. Write Bytes - 201705 Bytes 

![ScreenShot](https://github.com/just331/CS5352/blob/master/Project%201/p1_quad-probing_results.PNG)

### Concurrent Running
Below is a screenshot of both programs running in current to see the effects they have on a system when they are ran as threads at the same time. 
As you can see, for the most part the numbers stay relatively similar with an increase in cpu usage as well as an increase in page faults.

#### System Level Information:
##### CPU Info:
1. CPU Percentage - 98.5 %
##### Running Time:
1. Total Running time - 3171.406 ms
##### Memory Usage:
1. RSS - 194150400 Bytes
2. VMS - 416403456 Bytes
3. Pagefile - 414871552 Bytes
##### Page Faults:
1. Number of Page Faults - 85829
##### Hard Drive Usage:
1. Read Bytes -  8773029 Bytes
2. Write Bytes - 206187 Bytes 

![ScreenShot](https://github.com/just331/CS5352/blob/master/Project%201/p1_concurrent.PNG)