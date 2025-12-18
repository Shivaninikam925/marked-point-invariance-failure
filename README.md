# When Permutation Invariance Fails

This project presents a minimal counterexample demonstrating a fundamental
limitation of permutation-invariant representations in neural networks.

We construct a synthetic set-based task in which one element of the set is
semantically marked, and the label depends on the marked element’s position
relative to the set centroid. While order-sensitive encoders can represent this
information, permutation-invariant (group-averaged) encoders necessarily discard
the identity of the marked element and fail by construction.

Through controlled experiments, we show:
- Order-sensitive encoders change their embeddings under permutation.
- Invariant encoders remain stable under permutation, as expected.
- Crucially, invariant encoders also remain stable under *semantic changes*,
  revealing a failure to capture task-relevant structure.

This work highlights that symmetry-aware learning must be applied selectively:
enforcing invariance can be harmful when symmetry assumptions conflict with the
semantics of the problem.

<p align="center">
  <img src="c:\GitHub\marked-point-invariance-failure\notebooks\invariance_failure.png" width="600">
</p>

## Key Takeaway

Invariance is not universally beneficial. When tasks depend on distinguished
elements within a set, permutation invariance becomes an inappropriate inductive
bias.

## Relevance

This project connects to representation learning, inductive bias design,
group-invariant neural networks, and theoretical limitations of deep learning
models.

The entire project is intentionally minimal and concept-focused.
