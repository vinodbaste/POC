# Review Rubric

You are validating multiple-choice conversions of incorrect informal proof attempts for miniF2F benchmark problems.

For each artifact:
- Read the problem statement carefully.
- Read the full candidate proof from start to finish.
- Inspect each of the four candidate excerpts and locate them within the proof.
- Exactly one excerpt contains the **first** reasoning step that is mathematically invalid, unjustified, or logically broken.
- "First" means earliest in the proof order — subsequent steps may be conditionally valid given the flaw, or may compound it.
- Return only the chosen option letter for each artifact.

Common flaw types to look for:
- Applying a theorem outside its stated conditions (e.g., AM-GM on signed quantities, Fermat's little theorem with a composite modulus)
- Algebraic manipulation error (wrong sign, dropped term, incorrect factoring)
- Unjustified claim about existence or uniqueness
- Incorrect case enumeration (missing or double-counted cases)
- Circular reasoning or assuming the conclusion
- Wrong formula for a named mathematical quantity

The reducer must also compute exact aggregate counts for each option letter, competition, and year.
