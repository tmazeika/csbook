---
layout: default
title: Growth Rates
---

Asymptotic growth rates help us to describe how well an algorithm performs across machines, implementations, and input sizes.

|                | Lower Bound       | Exact Bound       | Upper Bound  |
| -------------- | :---------------: | :---------------: | :----------: |
| **Inclusive**  | $$\Omega(\cdot)$$ | $$\Theta(\cdot)$$ | $$O(\cdot)$$ |
| **Exclusive**  | $$\omega(\cdot)$$ | &mdash;           | $$o(\cdot)$$ |

## $$\Theta$$-Related Functions 

Given two functions $$f(n)$$ and $$g(n)$$, we say that $$f(n) \in \Theta(g(n))$$ if there exist positive constants $$a$$, $$b$$, and $$n_0$$ such that for all $$n \geq n_0$$:

<p>
\begin{equation}
   a \leq \frac{f(n)}{g(n)} \leq b
\end{equation}
</p>

In English, this means that $$f(n)$$ and $$g(n)$$ grow at the same rate.
