# b64X
> Secure Base64 Encode / Decode Terminal — v2.4.1

```
██████╗  ██████╗ ██╗  ██╗    ██╗  ██╗
██╔══██╗██╔════╝ ██║  ██║    ╚██╗██╔╝
██████╔╝███████╗ ███████║     ╚███╔╝ 
██╔══██╗██╔═══██╗╚════██║     ██╔██╗ 
██████╔╝╚██████╔╝      ██║   ██╔╝╚██╗
╚═════╝  ╚═════╝       ╚═╝   ╚═╝  ╚═╝
```

---
## Installation

**1. Clone the repo**
```bash
git clone https://github.com/n0voidX/b64x
cd b64x
```

**2. Install the dependency**
```bash
pip install rich
```

> If `pip` isn't recognized, try:
> ```bash
> pip3 install rich
> # or
> python -m pip install rich
> ```

---

## Usage

```bash
python main.py
```

You'll be prompted to choose an operation:

```
Type (E)ncode or (D)ecode:
```

### Encode
Press `E` and enter your plaintext string:
```
Type (E)ncode or (D)ecode: E
Enter the string: hello world
Result: aGVsbG8gd29ybGQ=
```

### Decode
Press `D` and paste your Base64 string:
```
Type (E)ncode or (D)ecode: D
Enter base64 hash value to decode: aGVsbG8gd29ybGQ=
Result: hello world
```

---

