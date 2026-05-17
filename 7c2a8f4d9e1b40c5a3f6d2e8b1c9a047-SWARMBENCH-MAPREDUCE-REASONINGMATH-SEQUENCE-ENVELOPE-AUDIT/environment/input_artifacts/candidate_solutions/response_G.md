# Response G

The "Mixed" envelope is incorrectly labeled, so it must contain only one type.

Suppose the first inspected sequence is strictly decreasing. Then the "Mixed" envelope is actually the decreasing envelope.

Now the remaining envelopes contain:

* increasing,
* constant,
* mixed.

Choose the envelope labeled "Strictly Decreasing."

If we observe:

* an increasing sequence, then it could still be mixed,
* a constant sequence, then it could still be mixed,
* another decreasing sequence, then it must be mixed.

To guarantee correctness, continue inspecting until either:

* two sequence categories appear, or
* 14 identical categories appear.

After that, the remaining envelopes are determined by elimination.

Therefore the minimum guaranteed number of inspections is **16**.
