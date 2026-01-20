*This project has been created as part of the 42 curriculum by <agarcia2>.*

# LibFT (Python Edition)

## Description

LibFT (Python Edition) is a foundational project inspired by the original C Libft from the 42 curriculum. The goal is to manually reimplement a collection of essential Python functions **without relying on their built‑in equivalents**, in order to deeply understand how they work internally.

This library is intentionally minimalistic and educational. Every function is implemented “from scratch”, using only basic Python constructs such as loops, conditionals, and primitive operations.

The project mirrors the philosophy of the C Libft:

- Build strong fundamentals  
- Understand what happens under the hood  
- Avoid shortcuts  
- Learn to reason about code  
- Develop reusable tools for future projects

LibFT is packaged as a Python module and can be installed locally.

## Instructions

### 📦 Installation

Clone the repository and install the library:

```bash pip install . ```

This will make the `LibFT` package available in your Python environment.

### 📁 Project Structure

``` LibFT/ ├── setup.py ├── __init__.py ├── ft_append.py ├── ft_input.py ├── ft_isinstance.py ├── ft_len.py ├── ft_print.py ├── ft_sorted.py ├── ft_chr.py ├── ft_int.py ├── ft_ord.py ├── ft_join.py ├── ft_range.py ├── ft_split.py └── __pycache__/ ```

### ▶️ Usage Example

```python from LibFT import ft_len, ft_ord, ft_chr

print(ft_len(*hola*)) print(ft_ord(*ñ*)) print(ft_chr(**241**)) ```

## Library Overview

LibFT currently includes the following reimplemented functions:

### 🔤 Character & String Utilities

- `ft_chr` — manual version of `chr`
- `ft_ord` — manual version of `ord`
- `ft_split` — manual string splitting
- `ft_join` — manual string joining

### 🔢 Numeric & Type Utilities

- `ft_int` — manual integer conversion
- `ft_len` — manual length calculation
- `ft_sorted` — manual sorting (bubble sort)
- `ft_isinstance` — manual type checking

### 🧰 List & Iteration Tools

- `ft_append` — manual append
- `ft_range` — custom iterable range class

### 🖥️ I/O Utilities

- `ft_print` — manual print using stdout
- `ft_input` — manual input using stdin

Each function is implemented without using the corresponding Python built‑in, following the same constraints as the C Libft: **no shortcuts, no cheating, full manual logic.**

## Resources

These references were used to understand the concepts behind the project:

- Python official documentation  
- Articles on Python internals (iteration protocol, Unicode, I/O streams)  
- Educational resources on algorithmic thinking and low‑level implementation  
- 42’s Libft subject (C version), used as conceptual inspiration

### AI Usage Statement

AI assistance was used exclusively for:

- Structuring the project  
- Clarifying Python internals  
- Generating boilerplate packaging files  
- Reviewing function design choices  
- Producing this **README** according to the official Libft requirements

All code was manually reasoned, adapted, and validated to ensure full understanding of every function.

## Detailed Description of the Library

LibFT is designed as a learning tool. Each function replicates the behavior of a Python built‑in, but implemented manually to reinforce understanding of:

- Iteration protocols  
- Unicode handling  
- Manual type checking  
- String manipulation  
- Basic algorithms (sorting, parsing, conversion)  
- Standard input/output streams  
- Mutable vs immutable types  
- Error handling and edge cases

The library can be reused in future educational projects, just like the original C Libft.

## License

This project is free to use for learning and experimentation. ```
