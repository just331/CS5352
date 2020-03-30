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

### Chaining  
The screen shot below provides details on the performance of the program that implemented Separate Chaining 

![ScreenShot](https://github.com/just331/CS5352/blob/master/Project%201/p1_separate-chaining_results.PNG)

### Quadratic Probing
The screen shot below provides details on the performance of the program that implemented Quadratic Probing 
![ScreenShot](https://github.com/just331/CS5352/blob/master/Project%201/p1_quad-probing_results.PNG)