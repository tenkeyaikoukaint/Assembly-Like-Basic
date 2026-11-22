# Assembly-Like Basic (or simply ALBasic)
The easiest interpreter with an insanely twisted design.

### Registers
Only two registers exist: `*` (accumulator) and `+` (pointer/counter).

### Instructions
- `load* arg`     : Load `arg` into the accumulator.
- `set+ arg`      : Set `arg` to the counter.
- `inc+`          : Increment the counter.
- `dec+`          : Decrement the counter.
- `add*+`         : Add the value pointed to by the counter to the accumulator.
- `sub*+`         : Subtract the value pointed to by the counter from the accumulator.
- `store*+`       : Store the accumulator's value into the memory address pointed to by the counter.
- `stores*+ arg`  : Store `arg` into memory starting at the counter, for a length specified by the accumulator.
- `print+`        : Print the number at the memory address pointed to by the counter.
- `prints*+`      : Print characters from memory starting at the counter, for a length specified by the accumulator.

### Labels
Add the prefix `&` (e.g., `&loop`).

### Memory

256 Bytes or Words. 


１##
