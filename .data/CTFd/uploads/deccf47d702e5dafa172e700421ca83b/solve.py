"""CBC padding-oracle solver for Doom's Padding. Usage: python solve.py http://HOST:8206"""
import sys
import requests

HOST = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8206"
BLOCK = 16


def get_ciphertext():
    r = requests.get(f"{HOST}/")
    # ciphertext hex is embedded in the page <pre> block
    import re
    m = re.search(r"<pre[^>]*>([0-9a-f]+)</pre>", r.text)
    return bytes.fromhex(m.group(1))


def oracle(blob: bytes) -> bool:
    r = requests.get(f"{HOST}/check", params={"ct": blob.hex()})
    return r.status_code == 200


def decrypt_block(prev: bytes, cur: bytes) -> bytes:
    intermediate = bytearray(BLOCK)
    for pad_val in range(1, BLOCK + 1):
        pos = BLOCK - pad_val
        test_prev = bytearray(BLOCK)
        for k in range(pos + 1, BLOCK):
            test_prev[k] = intermediate[k] ^ pad_val
        for guess in range(256):
            test_prev[pos] = guess
            if oracle(bytes(test_prev) + cur):
                if pad_val == 1 and pos > 0:
                    probe = bytearray(test_prev)
                    probe[pos - 1] ^= 0xFF
                    if not oracle(bytes(probe) + cur):
                        continue
                intermediate[pos] = guess ^ pad_val
                break
        else:
            raise RuntimeError(f"no byte found at pad {pad_val}")
    return bytes(p ^ i for p, i in zip(prev, intermediate))


def main():
    blob = get_ciphertext()
    iv = blob[:BLOCK]
    ct = blob[BLOCK:]
    blocks = [iv] + [ct[i:i + BLOCK] for i in range(0, len(ct), BLOCK)]
    recovered = b""
    for bi in range(len(blocks) - 1, 0, -1):
        recovered = decrypt_block(blocks[bi - 1], blocks[bi]) + recovered
    print(recovered)


if __name__ == "__main__":
    main()
