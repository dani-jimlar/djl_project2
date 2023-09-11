# 2023.706 Data Enigineering. Mini project 2
## Code description 
In this project two functions are used to descirbe the data from a csv file:
One function prints the descriptive statistcs using pandas describe():
- mean 
- median
- standard deviation
- min value
- max value
- first qt
- second qt
- third qt

Another function makes a barplot from a two selected variables using seaborn and matplotlib, and saves it as a png image.

## For this data set, the outputs are the following:

The variables in this data set are the following: ['entidad_a', 'enticve1', 'rangedad_a', 'sexostt', 'sexos1', 'sexos2', 'descrip']
Data behaves as follows:
         entidad_a    enticve1  rangedad_a       sexostt        sexos1       sexos2
count  310.000000  310.000000  310.000000    310.000000    310.000000   310.000000
mean    16.812903   16.812903    5.790323    740.564516    653.358065    87.206452
std      9.200244    9.200244    6.036934   1958.968172   1720.754210   244.881299
min      1.000000    1.000000    1.000000      0.000000      0.000000     0.000000
25%      9.000000    9.000000    3.000000     60.250000     50.000000     7.000000
50%     17.000000   17.000000    5.500000    185.500000    167.000000    21.000000
75%     25.000000   25.000000    8.000000    468.000000    402.500000    61.750000
max     32.000000   32.000000   99.000000  22782.000000  19580.000000  3202.000000

![image](https://github.com/dani-jimlar/djl_project2/blob/main/bar_plot.png)


