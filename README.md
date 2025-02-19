# A non-professional library created to provide value conversion functions in the number system.

## This library will provide the conversions:
    - Decimal to binary, octal or hexadecimal.
    - Binary to decimal, octal or hexadecimal.
    - Octal to decimal, binary or hexadecimal.
    - And in the future, hexadecimal to decimal, binary or octal.

# To install:
- In your cmd (Windows) - `pip install numeration_system`
- In terminal (Linux) - `pip3 install numeration_system`

## Example of use:
### To convert 256 in binary:
``` python
from numeration_system import *

number = 256

binary = decimal_to_binary(number)

print(binary)  # Output: 100000000
```
### If you want to see step-by-step conversion process:
``` python
from numeration_system import *

number = 256

binary = decimal_to_binary(number, step_by_step=True)
```