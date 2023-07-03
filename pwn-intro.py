from pwn import *

#Host
p = process("/bin/sh")
p.sendline("echo hello;")
p.interactive()

#Remote
r = remote("0.0.0.0",1234)
r.sendline("Hello!")
r.interactive()
r.close()

"""Terminal listener
nc -lvnp 1234
"""

#Packing Number
print(p32(0x13371337))
#Unpacking Number
print(hex(u32(p32(0x13371337))))

#ELF
l = ELF('/bin/bash')
print(hex(l.address))
print(hex(l.entry))
print (hex(l.address)) 
print(hex(l.entry))
print(hex(l.got['write']))
print(hex(l.plt['write']))
for address in l.search(b'/bin/sh\x00'): 
    print (hex(address))
print (hex(next(l.search(asm('jmp esp')))))
r = ROP (1)
print(r.rbx)

#Encoding/Decoding
print(xor(xor("A", "B"), "A")) 
print(b64e (b"test")) 
print(b64d (b"dGVzdA=="))
print(md5sumhex(b"hello"))
print(sha1sumhex(b"hello"))
print(bits(b'a'))
print(unbits([0, 1, 1, 0, 0, 0, 0, 1]))