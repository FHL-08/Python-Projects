# GaussBin_distribution

## Installing the package
Use the `pip` command below to install the package
    ```pip install distribution```

## Gaussian Distribution
### Creating a Gaussian Class
you can create a gaussian object using this syntax:
    `Gaussian(mu, sigma)`
where mu is the mean and sigma is the standard deviation of the data set

### Adding two Gaussian Objects
you can add two Gaussian Objects by simply using the '+' operator and it will return the new mean and standard deviations

### Reading data stored in a file
Function to read in data file from a text file, The text file should have one number (float) per line, The numbers are stored in the data attribute. After reading in the data file, the mean and standard deviation are calculated
    ```
    <Gaussian_objectName>.read_data_file("<file_name>")
    ```

### Calculating the mean
Function to calculate the mean of the data set

Args:
    None
Returns:
    float: mean of the data set
    ```
    <Gaussian_objectName>.calculate_mean()
    ```

### Calculating the standard deviation
Function to calculate the standard deviation of the data set

Args:
    sample (bool): whether the data represents a sample or population
Returns:
    float: satandard deviation of the data set
    ```
    <Gaussian_objectName>.calculate_stdev()
    ```

### Visualizing the input data
Function to output a histogram of the instance for the guassian distribution

Args:
    None
Returns:
    None
    ```
    <Gaussian_objectName>.plot_histogram()
    ```

### Visualizing the Gaussian Proabability Density Function
Function to plot the normalized histogram of the data and a plot of the probability density function along the same range

Args:
    n_spaces (int): number of data points to plot
Returns:
    list: x values for the pdf plot
    list: y values for the pdf plot
    ```
    <Gaussian_objectName>.plot_histogram_pdf(<n_space>)
    ```

## Binomial Distribution
### Creating a Binomial Class
you can create a binomial object using this syntax:
    `Binomial(mu, sigma)`
where mu is the mean and sigma is the standard deviation of the data set

### Adding two Binomial Objects
you can add two Binomial Objects by simply using the '+' operator and it will return the new mean and standard deviations

### Reading data stored in a file
Function to read in data file from a text file, The text file should have one number either, 0 (False) or 1 (True) per line; The numbers are stored in the data attribute. After reading in the data file, the mean and standard deviation are calculated
    ```
    <Binomial_objectName>.read_data_file("<file_name>")
    ```

### Calculating the mean
Function to calculate the mean of the data set

Args:
    None
Returns:
    float: mean of the data set
    ```
    <Binomial_objectName>.calculate_mean()
    ```

### Calculating the standard deviation
Function to calculate the standard deviation of the data set

Args:
    sample (bool): whether the data represents a sample or population

Returns:
    float: satandard deviation of the data set
    ```
    <Binomial_objectName>.calculate_stdev()
    ```
    
### Visualizing the input data
Function to output a histogram of the instance for the binomial distribution

Args:
    None

Returns:
    None
    ```
    <Binomial_objectName>.plot_bar()
    ```

### Visualizing the Gaussian Proabability Density Function
    Function to plot the pdf of the binomial distribution
    
    Args:
        None
    
    Returns:
        list: x values for the pdf plot
        list: y values for the pdf plot 
    ```
    <Binomial_objectName>.plot_histogram_pdf()

&copy;