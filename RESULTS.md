# Truncated Weil ground-state scan

## N-convergence (fixed c=19, the far end)

| N | dim | lambda_1 | lambda_2 | gap | log10(g) | odd-in-gap | sec |
|---|-----|----------|----------|-----|----------|------------|-----|
| 36 | 73 | `2.660800021072413844157557e-63` | `1.256316643919471063638832e-56` | `1.256316377839468956397448e-56` | -55.9009 | True | 1150.0 |
| 44 | 89 | `1.038343948795195954722348e-69` | `1.120680536363843683935079e-62` | `1.120680432529448804415483e-62` | -61.9505 | True | 1400.1 |
| 52 | 105 | `2.948838523623860015055096e-75` | `5.305872985126769615465892e-68` | `5.30587269024291725307989e-68` | -67.2752 | True | 1439.2 |

## c-scan at N=52

| c | a=log c | lambda_1 | log10(l1) | gap | log10(gap) | l1/gap |
|---|---------|----------|-----------|-----|------------|--------|
| 19 | 2.94444 | `2.948838523623860015055096e-75` | -74.5303 | `5.30587269024291725307989e-68` | -67.2752 | -7.2551 |


## Interpretation warning

The `c=19` absolute eigenvalues are still strongly N-dependent: both
`lambda_1` and `lambda_2` drift downward together as N increases.  Do not fit
an arithmetic decay law to either absolute sequence yet.  The next required
columns are Gram/overlap conditioning and a precision budget tied to the
smallest resolved eigenvalue.  The ratio `lambda_1/lambda_2` is a useful
dimensionless diagnostic, not yet a proved or certified limit.
