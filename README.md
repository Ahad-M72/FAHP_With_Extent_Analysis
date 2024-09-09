# FAHP_With_Extent_Analysis
This script, `Fuzzy_AHP.py`, is designed to handle the uncertainties and ambiguities inherent in judgment-based decision-making processes. It processes calculations using a primary pairwise comparison matrix for up to 10 items. The script reads data from a CSV file containing integrated pairwise comparisons, then computes the fuzzy synthetic extent values and normalized weights, as outlined in Chang's 1996 study [1]. Additionally, it calculates the Consistency Ratio (CR) values following the methodology from Gogus and Boucher's 1998 research [2]. This script effectively aids in determining normalized weights.


## Usage
1. Place your integrated pairwise comparisons in the provided CSV (Primary_Matrix.csv) file in an accessible location.
2. Modify the `file_path` variable in the script to point to your CSV file.
3. Run the script.

## Requirements
- Python 3.x
- Pandas
- NumPy
- 
## References
1. Chang, D.Y., 1996. Applications of the extent analysis method on fuzzy AHP. European journal of operational research 95, 649–655 (https://doi.org/10.1016/0377-2217(95)00300-2).
2. Gogus, O., Boucher, T.O., 1998. Strong transitivity, rationality and weak monotonicity in fuzzy pairwise comparisons. Fuzzy sets and systems 94, 133–144 (https://doi.org/10.1016/S0165-0114(96)00184-4).

```bash
python Fuzzy_AHP.py
