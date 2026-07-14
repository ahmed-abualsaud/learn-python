import statistics as stats

# Sample data
data = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 50, 10, 10, 5]

print("Data:", data)

# Calculate mean
mean = stats.mean(data) # mean = sum(data)/(len(data) - 1)
print("Mean:", mean)

# Calculate median
median = stats.median(data)
print("Median:", median)

# Calculate mode
mode = stats.mode(data) # If two numbers are repeated the same number of times, an error will appear.
print("Mode:", mode)

# Calculate standard deviation
std_dev = stats.stdev(data)
print("Standard Deviation:", std_dev)

# Calculate variance
variance = stats.variance(data)
print("Variance:", variance)

# Calculate the harmonic mean
harmonic_mean = stats.harmonic_mean(data) # harmonic mean = len(data)/sum([1/x for x in data])
print("Harmonic Mean:", harmonic_mean)

# Calculate the geometric mean
geometric_mean = stats.geometric_mean(data) # geometric mean = sqrt(reduce(lambda x,y: x*y, data))
print("Geometric Mean:", geometric_mean)

# Calculate the median low
median_low = stats.median_low(data)
print("Median Low:", median_low)

# Calculate the median high
median_high = stats.median_high(data)
print("Median High:", median_high)

# Calculate the median group
median_group = stats.median_grouped(data)
print("Median Grouped:", median_group)

# Calculate the population standard deviation
population_std_dev = stats.pstdev(data)
print("Population Standard Deviation:", population_std_dev)

# Calculate the population variance
population_variance = stats.pvariance(data)
print("Population Variance:", population_variance)

# Calculate the quantiles
quantiles = stats.quantiles(data, n=4)
print("Quantiles:", quantiles)