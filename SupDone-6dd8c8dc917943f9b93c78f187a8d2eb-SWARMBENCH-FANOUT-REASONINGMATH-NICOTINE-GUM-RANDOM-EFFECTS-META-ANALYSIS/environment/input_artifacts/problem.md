# Problem: random-effects meta-analysis of 26 nicotine-gum trials

A reviewer pooled 26 randomized controlled trials of **nicotine gum** for smoking
cessation. Each trial reports a 2x2 table of quitters vs. non-quitters in the
treatment (gum) and control arms. The raw counts are in
`/input_artifacts/trials.csv` and reproduced below.

Columns: `qt` = treated quitters, `tt` = total treated, `qc` = control quitters,
`tc` = total control. For each trial form `a = qt`, `b = tt - qt`, `c = qc`,
`d = tc - qc` (all cells are strictly positive, so no continuity correction).

| study | qt | tt | qc | tc |
|-------|----|----|----|----|
| Blondal89    | 37  | 92  | 24  | 90  |
| Campbell91   | 21  | 107 | 21  | 105 |
| Fagerstrom82 | 30  | 50  | 23  | 50  |
| Fee82        | 23  | 180 | 15  | 172 |
| Garcia89     | 21  | 68  | 5   | 38  |
| Garvey00     | 75  | 405 | 17  | 203 |
| Gross95      | 37  | 131 | 6   | 46  |
| Hall85       | 18  | 41  | 10  | 36  |
| Hall87       | 30  | 71  | 14  | 68  |
| Hall96       | 24  | 98  | 28  | 103 |
| Hjalmarson84 | 31  | 106 | 16  | 100 |
| Huber88      | 31  | 54  | 11  | 60  |
| Jarvis82     | 22  | 58  | 9   | 58  |
| Jensen91     | 90  | 211 | 28  | 82  |
| Killen84     | 16  | 44  | 6   | 20  |
| Killen90     | 129 | 600 | 112 | 617 |
| Malcolm80    | 6   | 73  | 3   | 121 |
| McGovern92   | 51  | 146 | 40  | 127 |
| Nakamura90   | 13  | 30  | 5   | 30  |
| Niaura94     | 5   | 84  | 4   | 89  |
| Pirie92      | 75  | 206 | 50  | 211 |
| Puska79      | 29  | 116 | 21  | 113 |
| Schneider85  | 9   | 30  | 6   | 30  |
| Tonnesen88   | 23  | 60  | 12  | 53  |
| Villa99      | 11  | 21  | 10  | 26  |
| Zelman92     | 23  | 58  | 18  | 58  |

## Required deliverable

Produce the **random-effects** pooled odds ratio using the standard
DerSimonian-Laird procedure on the log-odds-ratio scale, with its 95% confidence
interval. Use the following method:

1. Per study: `OR = (a*d)/(b*c)`, `y = ln(OR)` (natural log),
   `v = 1/a + 1/b + 1/c + 1/d`, inverse-variance weight `w = 1/v`.
2. Fixed-effect pool: `y_FE = sum(w*y)/sum(w)`.
3. Heterogeneity: `Q = sum(w*(y - y_FE)^2)`, `df = 25`,
   `I^2 = max(0, (Q - df)/Q) * 100`, and the DerSimonian-Laird
   `tau^2 = max(0, (Q - df)/C)` with `C = sum(w) - sum(w^2)/sum(w)`.
4. Random-effects pool: re-weight with `w* = 1/(v + tau^2)`,
   `y_RE = sum(w*·y)/sum(w*)`, `se_RE = sqrt(1/sum(w*))`.
5. Report `OR_RE = exp(y_RE)` and 95% CI `exp(y_RE +/- 1.96·se_RE)`.

The headline answer is the random-effects pooled odds ratio and its 95% CI. The
fixed-effect pooled odds ratio, `Q`, `I^2`, and `tau^2` are supporting quantities.
