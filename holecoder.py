#!/usr/local/bin/python3

import argparse
import urllib.parse
import logging
import html
import string

def encoder(args):

    # Change this to your need, \r\n or \n    
    linebreak = "\r\n"

    if args.f:
        with open(args.f, 'r') as lines:
            payload = lines.read()
            payload = linebreak.join(payload.splitlines())
    else:
        payload = args.p

    # Payload
    logging.info("Payload:")
    logging.info(f"{payload}\r\n")
    
    # Partial URL encoding
    logging.info("Partial URL encoding:")
    logging.info(f"{urllib.parse.quote(payload)}\r\n")
    
    # Partial URL encoding using + as space
    logging.info("Partial URL encoding using + as space:")
    logging.info(f"{urllib.parse.quote_plus(payload)}\r\n")
    
    # Full URL encoding
    percent_encode = ""
    logging.info("Full URL encoding:")
    for i in payload:
        hexa = i.encode('latin-1').hex()
        percent_encode += f"%{hexa}"
    logging.info(f"{percent_encode}\r\n")
    
    # Partial double URL encoding
    logging.info("Partial double URL encoding:")
    logging.info(f"{urllib.parse.quote(urllib.parse.quote(payload))}\r\n")
    
    # Full double URL encoding
    percent_encode = ""
    logging.info("Full double URL encoding:")
    for i in payload:
        hexa = i.encode('latin-1').hex()
        percent_encode += f"%{hexa}"
    logging.info(f"{urllib.parse.quote(percent_encode)}\r\n")

    # Partial HTML entities
    logging.info("Partial HTML entities:")
    entities = html.escape(payload, quote=True)
    logging.info(f"{entities}\r\n")
    
    # Full HTML entities
    logging.info("Full HTML entities:")
    # Check if the linebreak is \r\n, if so, change to \n, as \r is not supported in HTML entities
    if linebreak == "\r\n" and args.f:
        linebreak = "\n"
        logging.info("\\r\\n has been replaced by \\n")  
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
    logging.info(f"{encoded}\r\n")
    
    # Partial HTML decimal encoding
    encoded = ''
    for char in payload:
        if char not in string.ascii_letters and char not in string.digits:
            encoded += f'&#{ord(char)};'
        else:
            encoded += char
    logging.info("Partial HTML entities decimal encoding:")
    logging.info(f"{encoded}\r\n")
    
    # Full HTML decimal encoding
    encoded = ''
    for char in payload:
        encoded += f'&#{ord(char)};'
    logging.info("Full HTML entities decimal encoding:")
    logging.info(f"{encoded}\r\n")
    
    # Partial HTML decimal encoding with five zeros
    encoded = ''
    for char in payload:
        if char not in string.ascii_letters and char not in string.digits:
            encoded += f'&#00000{ord(char)};'
        else:
            encoded += char
    logging.info("Partial HTML entities decimal encoding with five zeros:")
    logging.info(f"{encoded}\r\n")
    
    # Full HTML decimal encoding with five zeros
    encoded = ''
    for char in payload:
        encoded += f'&#00000{ord(char)};'
    logging.info("Full HTML entities decimal encoding with five zeros:")
    logging.info(f"{encoded}\r\n")
    
    # Partial HTML decimal encoding with ten zeros
    encoded = ''
    for char in payload:
        if char not in string.ascii_letters and char not in string.digits:
            encoded += f'&#0000000000{ord(char)};'
        else:
            encoded += char
    logging.info("Partial HTML entities decimal encoding with ten zeros:")
    logging.info(f"{encoded}\r\n")
    
    
    # Full HTML decimal encoding with ten zeros
    encoded = ''
    for char in payload:
        encoded += f'&#0000000000{ord(char)};'
    logging.info("Full HTML entities decimal encoding with ten zeros:")
    logging.info(f"{encoded}\r\n")
    
    
    # Partial HTML hexadecimal encoding
    encoded = ''
    for char in payload:
        if char not in string.ascii_letters and char not in string.digits:
            hexa = char.encode('latin-1').hex()
            encoded += f'&#x{hexa};'
        else:
            encoded += char
    logging.info("Partial HTML entities hexadecimal encoding:")
    logging.info(f"{encoded}\r\n")
    
    
    # Full HTML hexadecimal encoding
    encoded = ''
    for char in payload:
        hexa = char.encode('latin-1').hex()
        encoded += f'&#x{hexa};'
    logging.info("Full HTML entities hexadecimal encoding:")
    logging.info(f"{encoded}\r\n")
    
    
    # Unicode encoding
    encoded = ''
    for char in payload:
        encoded += '\\u00{0:x}'.format(ord(char))
    logging.info("Unicode:")
    logging.info(f"{encoded}\r\n")
    
    # ECMAScript6 encoding
    encoded = ''
    for char in payload:
        encoded += '\\u' + "{" + '{0:x}'.format(ord(char)) + "}"
    logging.info("ES6:")
    logging.info(f"{encoded}\r\n")
    
    # ECMAScript6 encoding with five zeros
    encoded = ''
    for char in payload:
        encoded += '\\u' + "{00000" + '{0:x}'.format(ord(char)) + "}"
    logging.info("ES6 with five zeros:")
    logging.info(f"{encoded}\r\n")
    
    
    # ECMAScript6 encoding with ten zeros
    encoded = ''
    for char in payload:
        encoded += '\\u' + "{0000000000" + '{0:x}'.format(ord(char)) + "}"
    logging.info("ES6 with ten zeros:")
    logging.info(f"{encoded}\r\n")
    
    # Hex escaping
    hex_escape = ''
    for i in payload:
        hexa = i.encode('latin-1').hex()
        hex_escape += '\\x' + hexa
    logging.info("Hex escaping:")
    logging.info(f"{hex_escape}\r\n")
    
    # Octal escaping
    encoded = ''
    for char in payload:
        encoded += '\\{0:o}'.format(ord(char))
    logging.info("Octal escaping:")
    logging.info(f"{encoded}\r\n")
    
    
    # SQL Char in decimal
    encoded = ''
    for char in payload:
        encoded += 'CHAR({})+'.format(ord(char))
    logging.info("SQL Char in decimal:")
    logging.info(f"{encoded[:-1]}\r\n")
    
    
    
    # SQL Char in hex
    encoded = ''
    for char in payload:
        encoded += 'CHAR(x{0:x})+'.format(ord(char))
    logging.info("SQL char in hex:")
    logging.info(f"{encoded[:-1]}\r\n")



if __name__ == "__main__":
    logging.basicConfig(format='%(message)s',level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", help="Payload to encode")
    parser.add_argument("-f", help="Data inside a file to encode")
    args = parser.parse_args()
    if args.p is None and args.f is None:
        parser.error("At least one of -p (payload) or -f (file) is required")
        exit()
    encoder(args)
