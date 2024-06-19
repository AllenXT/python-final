# Python Programming Final Project

## Introduction

In this final project, the task is to develop a modeling system using Markov Models. These models capture the statistical relationships present in a language like English, allowing us to appreciate not just the frequency of specific letters or words, but the relationships between them in sequences. One application of Markov models is analyzing text to assess the likelihood that a particular person uttered it.

Another objective of this project is to create a hash tables module. Hash tables store associations between keys and values and provide an efficient means of looking up the value associated with a given key. Understanding hash tables will prepare developers to write their own in the future or handle cases where built-in hash tables interact poorly with their data.

## Part 1: Hash Table with Separate Chaining

This project will start by building a hash table using the separate chaining method to handle collisions. This involves implementing a Hashtable class with specific methods and properties.

### Separate Chaining

Separate chaining resolves collisions by adding new items to a linked list at the colliding index. Developers will need to implement a linked list class for this purpose. The hash table must be able to grow dynamically and rehash its contents to maintain performance.

### Rehashing

Rehashing involves expanding the table and reassigning items to new positions to maintain efficient access as the table grows.

## Part 2: A Speaker Recognition System

Using Markov models, this project will build a speaker recognition system. A Markov model for a known speaker helps assess the likelihood that a given text was uttered by that speaker.

### Building the Markov Model

The Markov model is represented as a Hashtable. It stores the frequency of k-length and k+1-length substrings from a known text. This model allows the determination of the likelihood of new text sequences.

### Determining the Likelihood of Unidentified Text

By comparing the frequency of substrings in the unknown text to the model, the probability that the text was uttered by the modeled speaker can be computed. This process uses log probabilities to handle very small numbers and avoid precision issues.

### Markov Class

A `Markov` class will be implemented to build and query the model. It will have methods for constructing the model from text and calculating the log probability of a string being uttered by the modeled speaker.

### `identify_speaker` Function

This function will compare the likelihoods of different speakers for a given text and determine the most likely speaker. It uses normalized log probabilities to provide meaningful comparisons across different text lengths.

## Part 3: Driver Files & Performance Testing

### Driver for Speaker Recognition System

A driver file will be created to run the speaker recognition system on provided text files. This file will read in texts, build models, and output the most likely speaker along with the calculated probabilities.

### Performance Testing

Another driver file will measure the performance of the `Markov` class using both the `Hashtable` and built-in `dict` implementations. It will run multiple tests with varying parameters and record the timings in a pandas dataframe.

### Graphing

A seaborn graph will be generated to visualize the performance data, comparing the average execution times for different implementations and k values. The graph will help assess the efficiency of the `Hashtable` implementation.

### Acknowledgment

This project was developed by the CAPP 30122 Team at The University of Chicago, with contributions from Rob Schapire and Kevin Wayne.
