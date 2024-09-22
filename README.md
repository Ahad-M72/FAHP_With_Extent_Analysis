# FAHP_With_Extent_Analysis
Fuzzy Analytic Hierarchy Process (FAHP) with extent analysis is an advanced decision-making technique that incorporates fuzzy logic into the traditional AHP framework. It is particularly useful when subjective judgments are involved, allowing for the incorporation of uncertainty and vagueness into pairwise comparisons. This script, `Fuzzy_AHP.py`, processes calculations using a primary pairwise comparison matrix for up to 10 items. The script reads data from a CSV file containing integrated pairwise comparisons, then computes the fuzzy synthetic extent values and normalized weights, as outlined in Chang's 1996 study [1]. Additionally, it calculates the Consistency Ratio (CR) values following the methodology from Gogus and Boucher's 1998 research [2]. This script effectively aids in determining normalized weights.

To reference this repository in academic publications and other documentation, a DOI badge has been added to the README. This badge links directly to the Zenodo archive, providing a stable and citable DOI.

[![DOI](https://zenodo.org/badge/854655029.svg)](https://zenodo.org/doi/10.5281/zenodo.13824776)

## How to Use
1. Place your integrated pairwise comparisons in a CSV file (Primary_Matrix) and an accessible location.
2. Modify the `file_path` variable in the script to point to your CSV file.
3. Run the script.
## Requirements
- Python 3.x
- Pandas
- NumPy
## CSV File
The CSV file should be structured as follows: 

The first row in the CSV file contains headers (9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9). In this format:

A value of 1 indicates that the items being compared are of equal significance.
Values other than 1 (e.g., 3 or 4) indicate how many times more significant one item is compared to the other in contributing to the goal.
For example, a value of 3 on the left means that the item on the left is three times more significant than the item on the right.

The subsequent rows contain numeric data representing the total number of times participants have chosen each option during the pairwise comparisons.
## References
1. Chang, D.Y., 1996. Applications of the extent analysis method on fuzzy AHP. European journal of operational research 95, 649–655 (https://doi.org/10.1016/0377-2217(95)00300-2).
2. Gogus, O., Boucher, T.O., 1998. Strong transitivity, rationality and weak monotonicity in fuzzy pairwise comparisons. Fuzzy sets and systems 94, 133–144 (https://doi.org/10.1016/S0165-0114(96)00184-4).

```bash
python Fuzzy_AHP.py
