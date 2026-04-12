from rich.console import Console
from rich.text import Text

console = Console()

BANNER = r"""
██████╗  ██████╗ ██╗  ██╗    ██╗  ██╗
██╔══██╗██╔════╝ ██║  ██║    ╚██╗██╔╝
██████╔╝███████╗ ███████║     ╚███╔╝ 
██╔══██╗██╔═══██╗╚════██║     ██╔██╗ 
██████╔╝╚██████╔╝      ██║   ██╔╝╚██╗
╚═════╝  ╚═════╝       ╚═╝   ╚═╝  ╚═╝
"""


def print_banner():
    console.print()
    banner_text = Text(BANNER, style="bold green")
    console.print(banner_text, justify="center")
    console.print(
        "[dim]Secure Base64 Encode / Decode Terminal  •  v2.4.1[/dim]",
        justify="center"
    )
    console.print()

print_banner()

task = input("Type (E)ncode or (D)ecode: ")
base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

if task == 'E' or task == 'e':
    estring = input("Enter the string: ")
    stringX = ""

    encoded = estring.encode("utf-8")
    for byte in encoded:
        stringX += format(byte, '08b')

    b_string = stringX
    while len(b_string) % 6 != 0:
        b_string += "0"

    chunks = []
    decimals = []
    for i in range(0, len(b_string), 6):
        chunk = b_string[i:i+6]
        chunks.append(chunk)
        decimal = int(chunk, 2)
        decimals.append(decimal)

    result = ""
    for i in decimals:
        character = base64_chars[i]
        result += character
    if len(encoded) % 3 == 1:
        result += "=="
    elif len(encoded) % 3 == 2:
        result += "="

    console.print(f"\n[bold green]Result:[/bold green] {result}\n")

elif task == 'D' or task == 'd':
    dstring = input("Enter base64 hash value to decode: ")
    cnt = 0
    decoded = ""
    if dstring.endswith("=="):
        cnt = 2
        dstring = dstring[:-2]
    elif dstring.endswith("="):
        cnt = 1
        dstring = dstring[:-1]
    decimals = []
    for i in dstring:
        decimal = base64_chars.index(i)
        decimals.append(decimal)
    for decimal in decimals:
        decoded += format(decimal, '06b')
    if cnt == 1:
        decoded = decoded[:-2]
    elif cnt == 2:
        decoded = decoded[:-4]
    bytes_list = []
    for i in range(0, len(decoded), 8):
        byte = decoded[i:i+8]
        bytes_list.append(byte)
    result = ""
    for byte in bytes_list:
        char = chr(int(byte, 2))
        result += char

    console.print(f"\n[bold magenta]Result:[/bold magenta] {result}\n")

else:
    console.print("\n[bold red]ERR:[/bold red] wrong input — use E or D\n")
