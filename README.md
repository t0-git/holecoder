# Python script to encode payloads

I wrote this script to encode payloads to try to bypass filters.

## How to

Pass your payload directly as a string using `-p "<payload>"` or using the content of a file with `-f <file>`. 

```
python3 holecoder.py -p "<script>alert(1)</script>"
python3 holecoder.py -f file.txt
```

## Support

- Partial URL encoding
- Partial URL encoding using + as space
- Full URL encoding
- Partial double URL encoding
- Full double URL encoding
- Partial HTML entities
- Full HTML entities
- Partial HTML decimal encoding
- Full HTML decimal encoding
- Partial HTML decimal encoding with five zeros
- Full HTML decimal encoding with five zeros
- Partial HTML decimal encoding with ten zeros
- Full HTML decimal encoding with ten zeros
- Partial HTML hexadecimal encoding
- Full HTML hexadecimal encoding
- Unicode encoding
- ECMAScript6 encoding
- ECMAScript6 encoding with five zeros
- ECMAScript6 encoding with ten zeros
- Hex escaping
- Octal escaping
- SQL Char in decimal
- SQL Char in hex

## Todo

- [ ] Add more encoding (any idea ?)
- [ ] Beautify the output (maybe one day)
