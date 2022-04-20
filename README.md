# Bink Test

### Executes functions in dos utilising the provided dataset

    using python 3.8.6 no external libraries have been used 

# How to use

  Pull from this repository
  Locate main.py in command prompt
  Run "py main.py" in command prompt
  
# Assumptions and Possible improvements

I have approached the task with user input in mind for each requirement as this will allow for more dry code
and also plan for possible errors that I may need to raise

## Read in the attached file
### Produce a list sorted by “Current Rent” in ascending order
### Obtain the first 5 items from the resultant list and output to the console

Currently providing the list as return and then printing out the list to console without altering how it looks,
could use 

>return "\n".join([str(x) for x in finaRetList]) 

to print each on new line when returned if needed.

## From the list of all mast data, create a new list of mast data with “Lease Years” = 25 years.
### Output the list to the console, including all data fields
### Output the total rent for all items in this list to the console

A possible improvement would be to make it more readable by formating the returned string with the data prior
to it.

## Create a dictionary containing tenant name and a count of masts for each tenant
### Output the dictionary to the console in a readable form

Instead of outputting the dictionary directly on to command promp, added string formatting to make it more
readable.

## List the data for rentals with “Lease Start Date” between 1st June 1999 and 31st August 2007
### Output the data to the console with dates formatted as DD/MM/YYYY

There is a lot of nested code to change date format, could explore ways of making it more readable, maybe have the compare
value be handled prior to loop to reduce the code for loop
  
# Pain points

## Testing

Prior to this I had no experience with writing tests and I only understood at a conceptual level so, I spent some time learning the basics and how 
to integrate it into GitHub actions to have some CI/CD integrations. There have been quite few learning points and quite few things I could
improve at over time, especially with using set up and tear down classes and it is very likely I missed some basic tests.

## Running functions with few lines of code

Originally, I wanted to execute functions based on if statements after user makes a choice but I felt like it was a lot of lines of code
and the process could improve. I used partials from functools library, I have not used this previously but it allowed me to use dictionary with values
hardcoded to run each function without having to use if statement on each. Another approach to this could be using lambda in dictionary but I had problems
with functions executing while creating dictionary so I ended up using partials to solve this.

## Creating Test Dataset

In hindsight it may have been better to create a smaller scale test dataset so when writing tests I did not have to fill in every value
in dictionary and could spend time focusing on testing the specific fields needed.

