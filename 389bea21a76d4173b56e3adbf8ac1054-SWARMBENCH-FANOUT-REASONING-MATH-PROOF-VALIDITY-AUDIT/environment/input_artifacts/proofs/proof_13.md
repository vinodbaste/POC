<!-- DOMAIN_BACKGROUND: /input_artifacts/background_combinatorics.md -->
<!-- REQUIRED: Read /input_artifacts/background_combinatorics.md before evaluating this proof. -->

    # proof_13

    - Problem ID: USAMO_2015_3
    - Competition: USAMO
    - Year: 2015
    - Level: high_school
    - Source URL: https://web.evanchen.cc/problems.html
    - Dataset row index: 41

    ## Problem

    Let \( S = \{1, 2, \ldots, n\} \), where \( n \geq 1 \). Each of the \( 2^n \) subsets of \( S \) is to be colored red or blue. For any set \( T \subseteq S \), let \( f(T) \) be the number of subsets of \( T \) that are blue.

Determine the number of colorings that satisfy the following condition: for any subsets \( T_1 \) and \( T_2 \) of \( S \),

\[
f(T_1) f(T_2) = f(T_1 \cup T_2) f(T_1 \cap T_2)
\]

    ## Candidate Solution Attempt

    Proof.  Let \(S=\{1,2,\dots,n\}\), and suppose we have colored each subset of \(S\) red or blue.  Denote by  
\[
B=\{\text{blue subsets of }S\}\subseteq\mathcal P(S),
\]
and define
\[
f(T)=\#\{\,U\in B:U\subseteq T\}
\]
for each \(T\subseteq S\).  The condition in the problem is
\[
f(T_1)\,f(T_2)\;=\;f(T_1\cup T_2)\;f(T_1\cap T_2)
\quad\text{for all }T_1,T_2\subseteq S.
\]
We will classify all such colorings by analyzing the corresponding function \(f\).

---

1. First observe that
\[
f(\varnothing)\;=\;\#\{\,U\in B:U\subseteq\varnothing\}
\;=\;\begin{cases}1,&\varnothing\in B,\\0,&\varnothing\notin B.\end{cases}
\]
Hence \(f(\varnothing)\) is either \(0\) or \(1\).  We split into two cases.

---

Case 1. \(f(\varnothing)=1\) (equivalently \(\varnothing\) is blue).

Define for each \(i\in S\)
\[
\lambda_i\;=\;f(\{i\})\;=\;\#\{\,U\in B:U\subseteq\{i\}\}.
\]
Since the only subsets of \(\{i\}\) are \(\varnothing\) and \(\{i\}\), and \(\varnothing\in B\), we have
\(\lambda_i=1\) if \(\{i\}\) is red, and \(\lambda_i=2\) if \(\{i\}\) is blue.  

Now for any \(T\subseteq S\) and any \(i\notin T\), apply the multiplicative condition with
\(\;T_1=\{i\},\;T_2=T\).  Since \(\{i\}\cap T=\varnothing\) and \(\{i\}\cup T=T\cup\{i\}\), we get
\[
f(\{i\})\,f(T)
\;=\;f(T\cup\{i\})\,f(\varnothing)
\quad\Longrightarrow\quad
\lambda_i\,f(T)
\;=\;f\bigl(T\cup\{i\}\bigr)\,.
\]
By induction on \(|T|\), it follows that
\[
f(T)
\;=\;\prod_{\,i\in T}\lambda_i,
\]
and in particular
\[
f(T)
\;=\;\prod_{i\in T}\bigl(\;1\text{ or }2\bigr)
\;=\;2^{\,\#\{\,i\in T:\lambda_i=2\}\;} 
\;=\;2^{\,|T\cap A|},
\]
where 
\[
A=\{\,i\in S:\lambda_i=2\}
\;=\;\{\;i:\{i\}\text{ is blue}\}\subseteq S.
\]
Thus
\[
f(T)=2^{\,|T\cap A|}\quad\text{for all }T\subseteq S.
\]
We claim that this forces \(B\) to be exactly the family of all subsets of \(A\).  Indeed, by Möbius inversion on the Boolean lattice one has the well-known formula
\[
\mathbf1_{B}(U)
\;=\;\sum_{\,T\subseteq U}(-1)^{\,|U|-|T|}\,f(T),
\]
where \(\mathbf1_B(U)=1\) if \(U\in B\) and \(0\) otherwise.  Substituting \(f(T)=2^{|T\cap A|}\) gives
\[
\mathbf1_{B}(U)
\;=\;\sum_{T\subseteq U}(-1)^{|U|-|T|}\,2^{|T\cap A|}
\;=\;\begin{cases}
1,&U\subseteq A,\\
0,&U\not\subseteq A,
\end{cases}
\]
since one checks by separating into the parts \(T\cap A\) and \(T\cap (U\setminus A)\) that the sum vanishes unless \(U\subseteq A\).  Hence
\[
B=\{\,U:U\subseteq A\}=\mathcal P(A).
\]
Conversely, any choice of \(A\subseteq S\) and then coloring exactly the subsets of \(A\) blue produces such an \(f\), and one checks directly that it satisfies
\(
f(T_1)f(T_2)=f(T_1\cup T_2)f(T_1\cap T_2)
\).  There are \(2^n\) choices of \(A\), hence \(2^n\) colorings in Case 1.

---

Case 2. \(f(\varnothing)=0\) (equivalently \(\varnothing\) is red).

If \(f\) were identically zero then \(B=\varnothing\) (all subsets red) and trivially the multiplicative condition holds.  That is one valid coloring.  Otherwise there is some \(T\subseteq S\) with \(f(T)>0\); let
\[
\mathcal F=\{\,T:f(T)>0\}
\]
be the “support’’ of \(f\).  From the multiplicative condition applied to any two *disjoint* sets \(T_1,T_2\) we have
\[
f(T_1)\,f(T_2)
\;=\;f(T_1\cup T_2)\,f(T_1\cap T_2)
\;=\;f(T_1\cup T_2)\,f(\varnothing)
\;=\;0,
\]
so at least one of \(f(T_1)\) or \(f(T_2)\) must be zero.  Hence \(\mathcal F\) is an *intersecting* family: no two members of \(\mathcal F\) are disjoint.

Since \(\mathcal F\neq\emptyset\), choose a minimal element \(U\in\mathcal F\) under inclusion.  Then \(f(U)>0\) but \(f(V)=0\) for every proper subset \(V\subsetneq U\).  By definition \(f(U)=\#\{\,X\in B:X\subseteq U\}>0\), so some \(X\in B\) lies in \(P(U)\).  Minimality of \(U\) forces \(X=U\), and no proper subset of \(U\) lies in \(B\).  Thus
\[
U\in B,\quad f(U)=1,\quad\text{and}\;\;B\cap P(U)=\{U\}.
\]

Next for *any* \(T\subseteq S\) apply the multiplicative condition with \(T_1=U\) and \(T_2=T\).  We get
\[
f(U)\,f(T)
\;=\;f(U\cup T)\,f(U\cap T)
\quad\Longrightarrow\quad
1\cdot f(T)
\;=\;f(U\cup T)\,f(U\cap T).
\]
If \(U\not\subseteq T\) then \(U\cap T\subsetneq U\), so \(f(U\cap T)=0\) by minimality, whence \(f(T)=0\).  Thus
\[
f(T)>0\;\Longrightarrow\;U\subseteq T,
\]
i.e.\ 
\[
\mathcal F=\{T:T\supseteq U\}
\;=\;\text{the upward‐closure of }U.
\]
In particular *every* blue set must contain \(U\), so
\[
B\;\subseteq\;\{\,V:U\subseteq V\subseteq S\}.
\]

Set \(S'=S\setminus U\), and for each \(W\subseteq S'\) define
\[
g(W)\;=\;f(U\cup W).
\]
Then \(g:\mathcal P(S')\to\mathbb Z_{\ge0}\) satisfies
\[
g(\varnothing)=f(U)=1,
\]
and one checks easily that the original multiplicative identity for \(f\) on pairs of sets containing \(U\) translates into
\[
g(W_1)\,g(W_2)
\;=\;g(W_1\cup W_2)\,g(W_1\cap W_2)
\quad\text{for all }W_1,W_2\subseteq S'.
\]
Hence by exactly the same argument as in Case 1, there is a unique subset \(A'\subseteq S'\) such that
\[
g(W)
\;=\;2^{\,|W\cap A'|}
\quad\Longrightarrow\quad
f(T)
\;=\;2^{\,|(T\setminus U)\cap A'|}\quad(\,T\supseteq U),
\]
and Möbius inversion shows that the blue sets are precisely
\[
B
\;=\;
\{\,U\cup W:W\subseteq A'\}
\;=\;
\{\,V:U\subseteq V\subseteq U\cup A'\},
\]
i.e.\ \(B\) is the interval \([\;U,\;U\cup A'\;]\) in the Boolean lattice.  

Conversely one checks by routine verification that *any* choice of a nonempty \(U\subseteq S\) and any \(A'\subseteq S\setminus U\), coloring exactly the sets \(V\) with
\[
U\subseteq V\subseteq U\cup A'
\]
blue (and all others red), yields an \(f\) satisfying the required multiplicativity.  Finally, there is the trivial additional solution \(B=\varnothing\) (all red), corresponding to the case \(\mathcal F=\emptyset\).

---

Counting the colorings:

• Case 1 (\(f(\varnothing)=1\)) gives exactly one coloring for each \(A\subseteq S\), namely \(B=\mathcal P(A)\).  There are \(2^n\) such.

• Case 2 (\(f(\varnothing)=0\)) gives one coloring for each choice of
\[
\hbox{either }B=\varnothing,
\quad\hbox{or}
\quad
\bigl(U,A'\bigr)\;\text{with }U\subseteq S,\;U\neq\varnothing,\;A'\subseteq S\setminus U,
\]
namely \(B=[\,U,U\cup A'\,]\).  Thus the total from Case 2 is
\[
1\;+\;\sum_{\substack{U\subseteq S\\U\neq\varnothing}}2^{\,|S\setminus U|}
\;=\;
1\;+\;\sum_{k=1}^n\binom nk\,2^{\,n-k}
\;=\;
1\;+\;\bigl(3^n-2^n\bigr)
\;=\;3^n-2^n+1.
\]
Adding both cases yields in total
\[
2^n\;+\;\bigl(3^n-2^n+1\bigr)
\;=\;3^n+1.
\]

Answer. \(\displaystyle 3^n+1\) colorings satisfy the required condition.