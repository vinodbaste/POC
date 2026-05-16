# Response E

## Setting Up the Puzzle

We have four bags labeled "Chocolate," "Mint," "Gum," and "Mixed." The actual contents are one pure-chocolate bag, one pure-mint bag, one pure-gum bag, and one mixed bag containing exactly two of the three types, 10 items each. All four labels are wrong.

## The Key Insight

Pick from the bag labeled "Mixed." Since this label is wrong, this bag is actually one of the three pure bags. So whatever single item I pull out tells me its true contents immediately.

Say I pull out a chocolate. Then:
- "Mixed" bag = Chocolate.

Now I need to identify the remaining three bags, labeled Chocolate, Mint, and Gum, which actually contain Mint, Gum, and Mixed in some order.

## Identifying the Rest

Consider the bag labeled "Mint." Its true contents must be Gum or Mixed: not Mint, and not Chocolate because Chocolate is already placed.

Pull items from it one at a time:
- If I ever see a mint, it must be the Mixed bag, since pure Mint is ruled out.
- If I see only gum, I might still be in the Mixed bag, which could be a Mint+Gum mix where I keep drawing the gum half.

In the worst case, the Mixed bag is Mint+Gum, and I unluckily pull all 10 gums before any mint. After 10 gums, I still cannot be sure. On the 11th draw, I am guaranteed to see a mint if it is the mixed bag, or another gum if it is pure Gum.

So 11 items from the "Mint"-labeled bag suffice to identify it. Once that bag is known, the last bag is determined by elimination.

Total: 1 + 11 = 12.

Worst case: 12 items.