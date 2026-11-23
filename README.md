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
- `stores*+ arg`  : Store `arg`(string) into memory starting at the counter, for a length specified by the accumulator.
- `call+ label`   : Jump to label and keep current program counter to memory and increment the counter.
- `ret+`          : Fetch return address from counter and jump.
- `jpnz+`         : Jump if the value of counter is not equal to zero.
- `cinc*+ arg`    : Increment the counter if the accumulator is equal to arg 
- `cdec*+ arg`    : Decrement the counter if the accumulator is equal toarg
- `print+`        : Print the number at the memory address pointed to by the counter.
- `prints*+`      : Print characters from memory starting at the counter, for a length specified by the accumulator.

### Labels
Add the prefix `&` (e.g., `&loop`).

### Memory

256 Bytes or Words. 


１##
