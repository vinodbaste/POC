# artifact_20

Competition: IMOSL  
Problem ID: IMOSL_2007_13  
Year: 2007

Human annotation sourced from the Open Proof Corpus (INSAIT-Institute/OPC). The reviewer's free-form note identified a first logical error; four candidate proof windows have been curated from the incorrect attempt. Select the one window that spans the human-marked flaw.

## Problem

Find all surjective functions \( f: \mathbb{N} \rightarrow \mathbb{N} \) such that for every \( m, n \in \mathbb{N} \) and every prime \( p \), the number \( f(m+n) \) is divisible by \( p \) if and only if \( f(m)+f(n) \) is divisible by \( p \).

## Candidate Excerpts

### Option A

```text
Inductive step.  Fix \(p\) and assume \((1)\) holds for all positive integers up to \(n-1\).  Apply \((\ast)\) with \((m,n)=(n-1,1)\).  Since \(f(1)=1\), we get
\[
p\mid f(n)
\quad\Longleftrightarrow\quad
p\mid\bigl(f(n-1)+1\bigr).
\]
By the inductive hypothesis \(p\mid f(n-1)\) exactly when \(p\mid (n-1)\).  Hence
\[
p\mid\bigl(f(n-1)+1\bigr)
\quad\Longleftrightarrow\quad
p\mid\bigl((n-1)+1\bigr)
\quad\Longleftrightarrow\quad
p\mid n.
\]
Combining these equivalences we obtain
\[
p\mid f(n)\quad\Longleftrightarrow\quad p\mid n,
\]
which completes the induction.  Thus for \emph{every} \(n\) and \emph{every} prime \(p\),
\[
p\mid f(n)\iff p\mid n.
\]
```

### Option B

```text
3. Finally, fix any \(n\in\Bbb N\).  From step 2 we know that the sets of prime divisors of \(f(n)\) and of \(n\) coincide.  Hence the ratio
\[
\frac{f(n)}{n}
\]
is a positive integer having no prime divisors at all, so it must be \(1\).  Therefore
\[
f(n)=n
\]
for every \(n\).
```

### Option C

```text
1. First we show \(f(1)=1\).  Suppose, to the contrary, that \(f(1)\) has some prime divisor \(p\).  Then for every \(m\in\Bbb N\) we may apply \((\ast)\) with \((m,n)=(m,1)\):  
\[
p\mid f(m+1)\quad\Longleftrightarrow\quad
p\mid\bigl(f(m)+f(1)\bigr).
\]
Since \(p\mid f(1)\), the right–hand side is equivalent to \(p\mid f(m)\).  Thus by induction on \(m\) we get
\[
p\mid f(1)\ \Longrightarrow\ p\mid f(2)\ \Longrightarrow\ p\mid f(3)\ \Longrightarrow\cdots,
\]
so \(p\) divides \emph{every} value \(f(m)\).  But then \(f\) never attains any number not divisible by \(p\), contradicting surjectivity onto all of \(\Bbb N\).  Hence \(f(1)\) has no prime divisors, i.e.\ \(f(1)=1\).
```

### Option D

```text
2. Next we prove by induction on \(n\) that for every prime \(p\),
\[
p\mid f(n)\quad\Longleftrightarrow\quad p\mid n.
\tag{1}
\]
Base case \(n=1\): we have just seen \(f(1)=1\), so neither \(1\) nor \(f(1)\) is divisible by \(p\).  Thus \((1)\) holds at \(n=1\).
```

## Full Candidate Proof

```text
Here is a self‐contained proof that the only surjective \(f\colon\Bbb N\to\Bbb N\) satisfying

\[
\forall\,m,n\in\Bbb N,\ \forall\,\hbox{prime }p,\quad
p\mid f(m+n)\ \Longleftrightarrow\ p\mid\bigl(f(m)+f(n)\bigr)
\tag{$\ast$}
\]

is the identity \(f(n)=n\).

Proof.

1. First we show \(f(1)=1\).  Suppose, to the contrary, that \(f(1)\) has some prime divisor \(p\).  Then for every \(m\in\Bbb N\) we may apply \((\ast)\) with \((m,n)=(m,1)\):  
\[
p\mid f(m+1)\quad\Longleftrightarrow\quad
p\mid\bigl(f(m)+f(1)\bigr).
\]
Since \(p\mid f(1)\), the right–hand side is equivalent to \(p\mid f(m)\).  Thus by induction on \(m\) we get
\[
p\mid f(1)\ \Longrightarrow\ p\mid f(2)\ \Longrightarrow\ p\mid f(3)\ \Longrightarrow\cdots,
\]
so \(p\) divides \emph{every} value \(f(m)\).  But then \(f\) never attains any number not divisible by \(p\), contradicting surjectivity onto all of \(\Bbb N\).  Hence \(f(1)\) has no prime divisors, i.e.\ \(f(1)=1\).

2. Next we prove by induction on \(n\) that for every prime \(p\),
\[
p\mid f(n)\quad\Longleftrightarrow\quad p\mid n.
\tag{1}
\]
Base case \(n=1\): we have just seen \(f(1)=1\), so neither \(1\) nor \(f(1)\) is divisible by \(p\).  Thus \((1)\) holds at \(n=1\).

Inductive step.  Fix \(p\) and assume \((1)\) holds for all positive integers up to \(n-1\).  Apply \((\ast)\) with \((m,n)=(n-1,1)\).  Since \(f(1)=1\), we get
\[
p\mid f(n)
\quad\Longleftrightarrow\quad
p\mid\bigl(f(n-1)+1\bigr).
\]
By the inductive hypothesis \(p\mid f(n-1)\) exactly when \(p\mid (n-1)\).  Hence
\[
p\mid\bigl(f(n-1)+1\bigr)
\quad\Longleftrightarrow\quad
p\mid\bigl((n-1)+1\bigr)
\quad\Longleftrightarrow\quad
p\mid n.
\]
Combining these equivalences we obtain
\[
p\mid f(n)\quad\Longleftrightarrow\quad p\mid n,
\]
which completes the induction.  Thus for \emph{every} \(n\) and \emph{every} prime \(p\),
\[
p\mid f(n)\iff p\mid n.
\]

3. Finally, fix any \(n\in\Bbb N\).  From step 2 we know that the sets of prime divisors of \(f(n)\) and of \(n\) coincide.  Hence the ratio
\[
\frac{f(n)}{n}
\]
is a positive integer having no prime divisors at all, so it must be \(1\).  Therefore
\[
f(n)=n
\]
for every \(n\).

It is immediate that the identity \(f(n)=n\) is surjective and indeed satisfies \((\ast)\), since
\[
f(m+n)=m+n
\quad\text{and}\quad
f(m)+f(n)=m+n
\]
are literally equal.  This completes the proof that the \emph{only} surjective solution of \((\ast)\) is
\[
\boxed{f(n)=n\quad(\forall\,n\in\Bbb N).}
\]
```

## Reviewer Note

Reasoning mistake.
