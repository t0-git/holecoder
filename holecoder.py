#!/usr/local/bin/python3

import argparse
import urllib.parse
import logging
import html
import string

def stdout_or_not(payload, boolean, output=None, encoding=None):
    if boolean:
        logging.info(f"{encoding}:")
        logging.info(f"{payload}\r\n")
    else:
        output.write(f"{payload}\r\n")


def encoder(args):

    # Change this to your need, \r\n or \n    
    linebreak = "\r\n"
    
    if args.f:
        with open(args.f, 'r') as lines:
            payload = lines.read()
            payload = linebreak.join(payload.splitlines())
    else:
        payload = args.p

    if args.o:
        output = open(args.o, 'a')
        boolean = False
    else:
        boolean = True
        output = None
    

    # Payload
    stdout_or_not(payload, boolean, output, "Payload") 
    
    # Partial URL encoding
    stdout_or_not(urllib.parse.quote(payload), boolean, output, "Partial URL encoding")
    
    # Partial URL encoding using + as space
    stdout_or_not(urllib.parse.quote_plus(payload), boolean, output, "Partial URL encoding using + as space")
    
    # Full URL encoding
    percent_encode = ""
    for i in payload:
        hexa = i.encode('latin-1').hex()
        percent_encode += f"%{hexa}"
    stdout_or_not(percent_encode, boolean, output, "Full URL encoding")
    
    # Partial double URL encoding
    stdout_or_not(urllib.parse.quote(urllib.parse.quote(payload)), boolean, output, "Partial double URL encoding")
    
    # Full double URL encoding
    percent_encode = ""
    for i in payload:
        hexa = i.encode('latin-1').hex()
        percent_encode += f"%{hexa}"
    stdout_or_not(urllib.parse.quote(urllib.parse.quote(percent_encode)), boolean, output, "Full double URL encoding")
    
    # Partial HTML entities
    entities = html.escape(payload, quote=True)
    stdout_or_not(entities, boolean, output, "Partial HTML entities")
    
    # Full HTML entities
    # Check if the linebreak is \r\n, if so, change to \n, as \r is not supported in HTML entities
    if linebreak == "\r\n" and args.f:
        linebreak = "\n"
        with open(args.f, 'r') as lines:
            html_payload = lines.read()
            html_payload = linebreak.join(html_payload.splitlines())
    else:
        html_payload = payload
    
    inverted_entities = html.entities.html5
    entities = {v: k for k, v in inverted_entities.items()}
    encoded = ""
    for char in html_payload:
        if(char in entities):
            encoded += f'&{entities[char]}'
        else:
            encoded += char
    stdout_or_not(encoded, boolean, output, "Full HTML entities")
    
    # Partial HTML decimal encoding
    encoded = ''
    for char in payload:
        if char not in string.ascii_letters and char not in string.digits:
            encoded += f'&#{ord(char)};'
        else:
            encoded += char
    stdout_or_not(encoded, boolean, output, "Partial HTML entities decimal encoding")
    
    # Full HTML decimal encoding
    encoded = ''
    for char in payload:
        encoded += f'&#{ord(char)};'
    stdout_or_not(encoded, boolean, output, "Full HTML entities decimal encoding")
    
    # Partial HTML decimal encoding with five zeros
    encoded = ''
    for char in payload:
        if char not in string.ascii_letters and char not in string.digits:
            encoded += f'&#00000{ord(char)};'
        else:
            encoded += char
    stdout_or_not(encoded, boolean, output, "Partial HTML entities decimal encoding with five zeros")
    
    # Full HTML decimal encoding with five zeros
    encoded = ''
    for char in payload:
        encoded += f'&#00000{ord(char)};'
    stdout_or_not(encoded, boolean, output, "Full HTML entities decimal encoding with five zeros")
    
    # Partial HTML decimal encoding with ten zeros
    encoded = ''
    for char in payload:
        if char not in string.ascii_letters and char not in string.digits:
            encoded += f'&#0000000000{ord(char)};'
        else:
            encoded += char
    stdout_or_not(encoded, boolean, output, "Partial HTML entities decimal encoding with ten zeros")
    
    
    # Full HTML decimal encoding with ten zeros
    encoded = ''
    for char in payload:
        encoded += f'&#0000000000{ord(char)};'
    stdout_or_not(encoded, boolean, output, "Full HTML entities decimal encoding with ten zeros")
    
    
    # Partial HTML hexadecimal encoding
    encoded = ''
    for char in payload:
        if char not in string.ascii_letters and char not in string.digits:
            hexa = char.encode('latin-1').hex()
            encoded += f'&#x{hexa};'
        else:
            encoded += char
    stdout_or_not(encoded, boolean, output, "Partial HTML entities hexadecimal encoding")
    
    
    # Full HTML hexadecimal encoding
    encoded = ''
    for char in payload:
        hexa = char.encode('latin-1').hex()
        encoded += f'&#x{hexa};'
    stdout_or_not(encoded, boolean, output, "Full HTML entities hexadecimal encoding")
    
    
    # Unicode encoding
    encoded = ''
    for char in payload:
        encoded += '\\u00{0:x}'.format(ord(char))
    stdout_or_not(encoded, boolean, output, "Unicode")
    
    # ECMAScript6 encoding
    encoded = ''
    for char in payload:
        encoded += '\\u' + "{" + '{0:x}'.format(ord(char)) + "}"
    stdout_or_not(encoded, boolean, output, "ES6")
    
    # ECMAScript6 encoding with five zeros
    encoded = ''
    for char in payload:
        encoded += '\\u' + "{00000" + '{0:x}'.format(ord(char)) + "}"
    stdout_or_not(encoded, boolean, output, "ES6 with five zeros")
    
    
    # ECMAScript6 encoding with ten zeros
    encoded = ''
    for char in payload:
        encoded += '\\u' + "{0000000000" + '{0:x}'.format(ord(char)) + "}"
    stdout_or_not(encoded, boolean, output, "ES6 with ten zeros")
    
    # Hex escaping
    hex_escape = ''
    for i in payload:
        hexa = i.encode('latin-1').hex()
        hex_escape += '\\x' + hexa
    stdout_or_not(hex_escape, boolean, output, "Hex escaping")
    
    # Octal escaping
    encoded = ''
    for char in payload:
        encoded += '\\{0:o}'.format(ord(char))
    stdout_or_not(encoded, boolean, output, "Octal escaping")
    
    
    # SQL Char in decimal
    encoded = ''
    for char in payload:
        encoded += 'CHAR({})+'.format(ord(char))
    stdout_or_not(encoded[:-1], boolean, output, "SQL char in decimal")
    
    
    
    # SQL Char in hex
    encoded = ''
    for char in payload:
        encoded += 'CHAR(x{0:x})+'.format(ord(char))
    stdout_or_not(encoded[:-1], boolean, output, "SQL char in hex")



if __name__ == "__main__":
    logging.basicConfig(format='%(message)s',level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", help="Payload to encode")
    parser.add_argument("-f", help="Data inside a file to encode")
    parser.add_argument("-o", help="File to output payloads (easier to ingest in intruder for example")
    args = parser.parse_args()
    if args.p is None and args.f is None:
        parser.error("At least one of -p (payload) or -f (file) is required")
        exit()
    encoder(args)
