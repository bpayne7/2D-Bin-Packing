   
   README - Lab 11/12
   --------------

   Author: Brian Payne

   CS505 Spring 2015

   Lab 11/12 - Final project

   V1.0

   Due 29 April 2015 at 8:15 (by the beginning of the exam time)



   INSTALLATION
   ------------

   The "BPayne_Lab11_12.tar" file contains "packer.py" and 
   "packer_nodes.py". Both these programs employ python 3. Please make sure
   to have the math, time, random, pprint, and tkinter packages installed.


   HOW TO RUN PROGRAM
   ------------------

   Once uppacked, enter "python3 packer.py" or 
   "packer_nodes.py" into your shell command line to run
   each program.


   INPUTS
   ------

   For both programs, the user is required to enter 'y' or 'n' for the use of 
   random blocks(random height and random width). The user is also required 
   to enter which algorithm to use: 'ff' or 'nf' for more information about 
   these algorithms, please see "algorithm_info".


   OUTPUTS
   -------
   
   The output for "packer.py" when 'nf' is specified, is a box or bin, which blocks 
   are placed in an order of smaller height to larger height once they are sorted.

   The output for "packer.py" when 'ff' is specified, is the blocks placed in the 
   best position, in an attempt to minimize wasted space. For more info on these 
   algorithms, please see "algorithm_info".

   The output for "packer_nodes.py" when 'ff' and 'nf' are specified are a red outline of 
   the actual nodes that are calculated.

   All of these programs have a line drawn on the canvas that shows where the bin
   height would be, which is a good way of tracking the effectivness of the algorithm.
   All of these programs also output the location of the node and block along with 
   the size of the node and block. Additionally, it prints whether the block was placed 
   or not.

   TESTING 
   -------

   Testing was done by knowing what the algorithm was physically look like. The 
   block placement was slowed down to ensure that the block was being placed in 
   the appropriate node. For more info, please see "algorithm_info".

   HELP
   ----

   If there is assistance needed please email: bpayne7@vols.utk.edu

