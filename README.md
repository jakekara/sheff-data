## Cleanup of school segregation and school choice lottery data

These data sets were printed and scanned then sent to us. We had to do a
lot of cleaning to digitize the data and then combine the separate
spreadsheets.

Each step adds potential mistakes, so if you find any mistakes that I
didn't catch, please let me know! jkara@ctmirror.org

The basic steps included:

1. Get the raw data
2. OCR the documents to excel
3. Merge the excel sheets
3. Remove scanner mistakes and school name inconsistencies
4. Restructure for use in the table

### 1. Get the raw data

PDF files are available in the raw_data directory:

* The number of applicants who chose each school as their first choice. The
  data is available for each grade all students, as well as broken down
  based on whether the students reside in Hartford or surrounding
  suburbs.

* The number of offers made by each school.

### 2. OCR the documents to Excel

For this, I used Adobe Acrobat Pro, and exported them to

* data/CLEANED - First Chocie Apps By School By Grade 2017-18.xlsx
* data/CLEANED - Offers By School By Grade 2017-18.xlsx

The file names are deceiving. They were digitized but far from
clean. Numbers like "10" were read as the letters "IO".

So I had to do more intense cleaning.

### 3. Remove scanner mistakes and school name inconsistencies

In the notebook [Odds of getting in - 2.ipynb](Odds of getting in -
2.ipynb), I combined the two scanned sheets, then imported them into
OpenRefine. The OpenRefine project is called
[REFINED.openrefine.tar.gz](REFINED.openrefine.tar.gz).

But that wasn't enough cleaning. OpenRefine is amazing for finding similar
words that should probably be the same, but I also needed to look for other
mistakes Refine wouldn't catch, such as empty cells that shouldn't be
empty. 

You'll note that a lot of the original data is missing, suppressed
for privacy reasons, so that's OK. But I went through the data looking for
cells that were empty that shouldn't be. I did that the old fashioned way,
comparing a printed out version of the two raw PDFs to the product of the
Refine process, in a Google spreadsheet
[here](https://docs.google.com/spreadsheets/d/e/2PACX-1vQDOK99IEzl8m6CuPk9RAa9VCG9wSniELaT8K-OBZzguf6DAk8gkmpm0xGCKvYlzan-yvMRf94_mTfG/pubhtml).

#### 4. Restructure for use in the table

Finally, and of no importance to anyone else, I had to restructure the data
to wedge it into an old table display, so I did that in the [csv-to-json/structure for
odds table.ipynb notebook](csv-to-json/structure for odds table.ipynb)