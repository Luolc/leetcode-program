We loop the sequence and maintain that `[0, i)`, `[i, j)`, and `[j, k)` are `0`s, `1`s, and `2`s sorted in place for `[0,k)`.
An important trick is moving `2` earlier than `1`, and `1` earlier than `0`.
See the code for details.
