# Oracle Justification

## Correct mathematical answer

Under the sparse Gaussian mixture alternative, epsilon_n = n^{-beta}, mu_n = sqrt(2 r log n), beta = 0.85, and r = 0.45.

For Test A, the one-sided z-test based on the sample mean has standardized mean shift

sqrt(n) epsilon_n mu_n = n^{1/2 - beta} sqrt(2 r log n)
= n^{-0.35} sqrt(0.9 log n) -> 0.

The variance remains 1 + o(1), so the z-statistic has the same limiting null distribution under H0 and H1. Test A does not have asymptotic power tending to 1.

For Test B, the maximum test must account for the maximum over the nonnull coordinates, not just compare one signal mean against the null maximum. The number of nonnull observations is about n^{1-beta}. The maximum among signals is on the scale

sqrt(2 log n) (sqrt(r) + sqrt(1 - beta)).

The null maximum is on the scale sqrt(2 log n). Therefore the maximum test succeeds when

sqrt(r) + sqrt(1 - beta) > 1,

equivalently r > (1 - sqrt(1 - beta))^2 for beta in this range. With beta = 0.85 and r = 0.45,

sqrt(0.45) + sqrt(0.15) approximately equals 1.058 > 1,

so Test B has asymptotic power tending to 1.

For Test C, Higher Criticism achieves the Donoho-Jin/Ingster detection boundary. For beta in (3/4, 1),

rho^*(beta) = (1 - sqrt(1 - beta))^2.

For beta = 0.85,

rho^*(0.85) = (1 - sqrt(0.15))^2 approximately 0.3754.

Since r = 0.45 > 0.3754, Higher Criticism has asymptotic power tending to 1.

Thus the correct original-problem answer is ["B", "C"].

## Six-response visible set

The final visible response set contains six proposed responses. The fully correct proposed response from the earlier draft was removed. Therefore no visible proposed response is fully acceptable, although Response E still gives the correct final test-letter list with flawed reasoning.

Thus acceptable_solution_ids is [].

## Response-label rationale

### Response A

Response A claims ["C"]. It correctly rejects Test A and correctly concludes Higher Criticism succeeds, but it rejects the maximum test using the wrong condition r > 1. Its final answer is wrong, Test B conclusion is wrong, and it has a final-answer-critical mathematical error. It uses the correct Donoho-Jin boundary for Higher Criticism and computes/compares that boundary correctly.

### Response B

Response B claims ["C"]. It uses the wrong Donoho-Jin boundary formula for beta = 0.85, namely the beta - 1/2 branch outside its valid range, and it mishandles the maximum-test conclusion. Its final answer is wrong and it has a final-answer-critical mathematical error. The comparison-to-boundary label is false because it compares r against the wrong boundary for this problem.

### Response C

Response C claims ["C"]. It rejects the maximum test by comparing only the signal mean to the null maximum and not by analyzing the maximum over the nonnull coordinates. It contains final-answer-critical mathematical errors. Its prose is not organized into the required stepwise structure and its mathematical notation is not mostly proper LaTeX.

### Response D

Response D claims ["C"]. It rejects the maximum test incorrectly and contains confused Higher Criticism calculations. It has a calculation/exponent-sign error in its Higher Criticism calculation after its stated premises. Its final answer is wrong and it has final-answer-critical mathematical errors.

### Response E

Response E claims ["B", "C"], so its final answer to the original multiple-choice question is correct. However, it justifies the result using the wrong detectability condition r > 1 - beta instead of the correct Donoho-Jin boundary for beta = 0.85. Therefore it is not a fully acceptable solution. Its boundary formula, boundary value, and comparison-to-boundary labels are false, and it has a final-answer-critical mathematical error.

### Response F

Response F claims ["C"]. It is vague and unsupported, misses the correct boundary calculation, and makes an incorrect statement about the z-test. Its final answer is wrong and it has final-answer-critical mathematical errors. Its final-answer-critical reasoning is also insufficiently justified, and substantial mathematical notation is written in HTML/non-LaTeX markup, so has_proper_latex_format is false.

## Scoring-weight rationale

The judge keeps top-level summary fields and routine extraction/format fields at low weight. The high-weight fields are mathematical audit fields that test subtle sparse-mixture reasoning: false boundary comparisons, parameterization mistakes, numerical-boundary evaluation, exponent-sign/calculation errors, and final-answer-critical mathematical error classification.

The critical fields are:
- Response B compares_r_to_boundary_correctly.
- Response D compares_r_to_boundary_correctly.
- Response D has_calculation_error.
- Response E uses_correct_donoho_jin_boundary.
- Response E boundary_numeric_value_correct.
- Response E compares_r_to_boundary_correctly.
- Response E has_final_answer_critical_math_error.
- Response F test_a_conclusion_correct.
- Response F has_final_answer_critical_math_error.

These fields are central to the audit objective and are not simple answer-extraction checks.
