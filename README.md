# CMPS 2200  Recitation 01

**Name (Team Member 1):**__Raymond Liu_______________________  
**Name (Team Member 2):**_________________________

In this recitation, we will investigate asymptotic complexity. Additionally, we will get familiar with the various technologies we'll use for collaborative coding.

To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`. All tests are in `test_main.py`.

## Install Python Dependency

We need Python library of "tabulate" to visualize the results in a good shape. Please install it by running 'pip install tabulate' or 'pip install -r requirements.txt' in Shell Tab of Repl.  

## Running and testing your code

- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Comparing search algorithms

We'll compare the running times of `linear_search` and `binary_search` empirically.

`Binary Search`: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

- [ ] 1. In `main.py`, the implementation of `linear_search` is already complete. Your task is to implement `binary_search`. Implement a recursive solution using the helper function `_binary_search`. 

- [ ] 2. Test that your function is correct by calling from the command-line `pytest test_main.py::test_binary_search`

- [ ] 3. Write at least two additional test cases in `test_binary_search` and confirm they pass.

- [ ] 4. Describe the worst case input value of `key` for `linear_search`? for `binary_search`? 

**TODO: Worst Case Input Value for Searches:
For linear_search, the worst-case input value of key would be an element that is not in the list or the last element in the list.
For binary_search, the worst-case input value would be an element that is not in the list, requiring the algorithm to complete its entire search process.

- [ ] 5. Describe the best case input value of `key` for `linear_search`? for `binary_search`? 

**TODO: Best Case Input Value for Searches:
For linear_search, the best-case input value of key would be the first element in the list, resulting in an immediate find.
For binary_search, the best case would be if the key is exactly in the middle of the list, resulting in a find in the first comparison.

- [ ] 6. Complete the `time_search` function to compute the running time of a search function. Note that this is an example of a "higher order" function, since one of its parameters is another function.

- [ ] 7. Complete the `compare_search` function to compare the running times of linear search and binary search. Confirm the implementation by running `pytest test_main.py::test_compare_search`, which contains some simple checks.

- [ ] 8. Call `print_results(compare_search())` and paste the results here:

**TODO: |        n | linear | binary |
        |     10.0 |  0.008 |  0.013 |
        |    100.0 |  0.008 |  0.007 |
        |   1000.0 |  0.127 |  0.009 |
        |  10000.0 |  0.914 |  0.018 |
        | 100000.0 | 13.647 |  0.053 |
        |1000000.0 |193.543 |  0.032 |
        |10000000.0|2586.449|  0.056 |

- [ ] 9. The theoretical worst-case running time of linear search is $O(n)$ and binary search is $O(log_2(n))$. Do these theoretical running times match your empirical results? Why or why not?

**TODO: The empirical results are expected to align with the theoretical predictions qualitatively. That is, the linear search times will increase linearly with n, and binary search times will increase logarithmically. However, due to constants and lower-order terms, as well as overhead from function calls and recursion, the exact times may not perfectly fit the big O notation.

- [ ] 10. Binary search assumes the input list is already sorted. Assume it takes $\Theta(n^2)$ time to sort a list of length $n$. Suppose you know ahead of time that you will search the same list $k$ times. 
  + What is worst-case complexity of searching a list of $n$ elements $k$ times using linear search? **TODO: O(kn) because we have to search through all n elements k times.
  + For binary search? **TODO: O(k log n) if the list is pre-sorted. If not, you must include the sort cost, so it's O(n^2 + k log n).
  + For what values of $k$ is it more efficient to first sort and then use binary search versus just using linear search without sorting? **TODO: To determine for which values of k sorting is worth it, we need to compare kn (for linear search) with n^2 + k log n (for sort once, then binary search). Sorting first is more efficient when n^2 + k log n < kn. This is generally true for large k and when the cost of sorting (n^2) is less than the cost of doing many linear searches (kn - k log n). So, if we plan to search the list more than n times, it is more efficient to sort the list first and then use binary search. However, this is a rough approximation