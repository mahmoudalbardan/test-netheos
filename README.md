# Compute offset of PDF files

## How to run 

1 - Download the code and the files from github

2 - Go the the corresponding folder in your terminal and type: `python3 script.py --path [file path]` 

example: `python3 script.py --path test_1.pdf` 


## Results

- test_1.pdf: **4568**

- test_2.pdf: **22195**

- test_3.pdf: **19155**

- test_4.pdf: **19155**

- test_6.pdf: **21371**


## Remarks

We split the binary stream of the pdf file into chunks to prevent issues in memory. By default, we choose a chunk size of 512, however, you can change it directly from the script (I did not put this parameter as an argument).
