# rqubit

Simplify the usage of rigettis compiler and qvm


## Usage

It spins up a quilc and qvm instance so you don't have to open additional sessions

```python
from rqubit import Quomputer

from pyquil import Program
from pyquil import get_qc
from pyquil.gates import *

with Quomputer():
    
    p = Program()
    ro = p.declare('ro', 'BIT', 1)
    p += X(0)
    p += MEASURE(0, ro[0])
    
    qc = get_qc('1q-qvm')
    executable = qc.compile(p)
    result = qc.run(executable)
    
    print(result)
```

or

```python
from rqubit import Quomputer

q = Quomputer()
q.start()

p = Program()
ro = p.declare('ro', 'BIT', 1)
p += X(0)
p += MEASURE(0, ro[0])

qc = get_qc('1q-qvm')
executable = qc.compile(p)
result = qc.run(executable)

print(result)

q.stop()
```

