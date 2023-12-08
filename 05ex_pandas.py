###05EX_PANDAS

#question 1

import pandas as pd
df = pd.read_csv('data/data_000637.txt',nrows=25000)
print(df.head()) 
print(df.shape) 



###question 2

import pandas as pd
df = pd.read_csv('data/data_000637.txt')
est_df= df["BX_COUNTER"]
est_bx = max(est_df)
print( est_bx)


###question 3

import pandas as pd
df = pd.read_csv('data/data_000637.txt',nrows=25000)
x = df["BX_COUNTER"]
est_x = max(x)
df["abs_time_in_ns"] = df['TDC_MEAS'].transform(lambda x: x * 25/30) + df['BX_COUNTER'].transform(lambda x: x * 25) +df['ORBIT_CNT'].transform(lambda x: x * est_bx * 25)
print(df)

###question 4
import datetime as dt
import pandas as pd
x = df["BX_COUNTER"]
est_x = max(x)
df = pd.read_csv('data/data_000637.txt',nrows=25000)
begin_time = dt.datetime.now()
print(begin_time)
time = df['TDC_MEAS'] *(25/30) + df['BX_COUNTER'] * 25 + df['ORBIT_CNT']*est_x*25
end_time = dt.datetime.now()
print(end_time)
print((end_time - begin_time))


###question 5
import numpy as np
import pandas as pd
df = pd.read_csv('data/data_000637.txt',nrows=25000)
y=  df.groupby('TDC_CHANNEL').sum().sort_values(by = ['HEAD']).iloc[-3:]
print(y)

###question 6

import numpy as np
import pandas as pd
df = pd.read_csv('data/data_000637.txt',nrows=25000)
count_num = df.ORBIT_CNT.unique().size
print(str(count_num))

###question 7
import numpy as np
import pandas as pd
df = pd.read_csv('data/data_000637.txt',nrows=25000)
unique_orbits = pd.DataFrame(df[df['TDC_CHANNEL'] == 139]).drop_duplicates(subset=['ORBIT_CNT'], inplace=False)
print(len(unique_orbits))
##q8
import numpy as np
import pandas as pd
data = pd.read_csv('data/data_000637.txt')
FPGA_0 = pd.Series(data[data['FPGA'] == 0]['TDC_CHANNEL'].value_counts())
FPGA_1 = pd.Series(data[data['FPGA'] == 1]['TDC_CHANNEL'].value_counts())
print(FPGA_0)
print(FPGA_1)

##9
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv 
data = pd.read_csv('data/data_000637.txt')
FPGA_0 = pd.Series(data[data['FPGA'] == 0]['TDC_CHANNEL'].value_counts())
FPGA_1 = pd.Series(data[data['FPGA'] == 1]['TDC_CHANNEL'].value_counts())
plt.hist(FPGA_0)
plt.title('FPGA == 0')
plt.xlabel('TDC_CHANNEL')
plt.ylabel('number of counts')
plt.show()
plt.hist(FPGA_1)
plt.title('FPGA == 1')
plt.xlabel('TDC_CHANNEL')
plt.ylabel('number of counts')
plt.show()
