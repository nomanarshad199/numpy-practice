#Task 3: Weather Analyzer
import numpy as np

# Each column = one month (Jan, Apr, Jul, Oct)
temperatures = np.array([
    [12, 22, 33, 19],  # Day 1
    [13, 24, 35, 21],  # Day 2
    [11, 23, 34, 20],  # Day 3
    [10, 21, 32, 18],  # Day 4
    [14, 42, 36, 22],  # Day 5
    [13, 26, 37, 23],  # Day 6
    [15, 27, 38, 24]   # Day 7
])

#1 : Calculate the average temperature for each month
avg_temperatures = np.mean(temperatures, axis=0)
print("Average temperatures for each month:", avg_temperatures)

#2. Hottest and coldest days of the week (across all months)
hottest_day = np.max(temperatures, axis=0)
coldest_day = np.min(temperatures, axis=0)
print("Hottest day temperatures:", hottest_day)
print("Coldest day temperatures:", coldest_day)

#3. Which month had the highest temperature overall?

highest_temp_month = np.argmax(temperatures, axis=0)
print("Highest temperature month: ", highest_temp_month) # it tells the indexes of highest temp value

#4. Replace all temperatures above 35°C with np.nan
replaced_temp = np.where(temperatures > 35, np.nan, temperatures) #np.nan is used to represent missing values
print("Temperatures after replacing values > 35 with np.nan:\n", replaced_temp)

#5. Flatten the array and find the overall mean (excluding NaNs)

flat_temp= np.ravel(replaced_temp)         # Flatten the array
print("Flattened temperature array:", flat_temp)
flatten_mean = np.nanmean(flat_temp)  
print("Overall mean temperature:", flatten_mean)