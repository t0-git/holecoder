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
    logging.info(f"{payload}")
    
    # Partial URL encoding
    logging.info("Partial URL encoding:")
    logging.info(f"{urllib.parse.quote(payload)}")
    
    # Partial URL encoding using + as space
    logging.info("Partial URL encoding using + as space:")
    logging.info(f"{urllib.parse.quote_plus(payload)}")
    
    # Full URL encoding
    percent_encode = ""
    logging.info("Full URL encoding:")
    for i in payload:
        hexa = i.encode('latin-1').hex()
        percent_encode += f"%{hexa}"
    logging.info(f"{percent_encode}")
    
    # Partial double URL encoding
    logging.info("Partial double URL encoding:")
    logging.info(f"{urllib.parse.quote(urllib.parse.quote(payload))}")
    
    # Full double URL encoding
    percent_encode = ""
    logging.info("Full double URL encoding:")
    for i in payload:
        hexa = i.encode('latin-1').hex()
        percent_encode += f"%{hexa}"
    logging.info(f"{urllib.parse.quote(percent_encode)}")

    # Partial HTML entities
    logging.info("Partial HTML entities:")
    entities = html.escape(payload, quote=True)
    logging.info(f"{entities}")
    
    # Full HTML entities
    # Check if the linebreak is \r\n, if so, change to \n, as \r is not supported in HTML entities
    if linebreak == "\r\n" and args.f:
        linebreak = "\n"
        with open(args.f, 'r') as lines:
            html_payload = lines.read()
            html_payload = linebreak.join(html_payload.splitlines())
    else:
        html_payload = payload

    logging.info("Full HTML entities:")
    inverted_entities = html.entities.html5
    entities = {v: k for k, v in inverted_entities.items()}
    encoded = ""
    for letter in html_payload:
        if(letter in entities):
            encoded += '&{}'.format(entities[letter])
        else:
            encoded += letter
    logging.info(f"{encoded}")
    
    # Partial HTML decimal encoding
    encoded_payload = ''
    for letter in payload:
        if letter not in string.ascii_letters and letter not in string.digits:
            encoded_payload += '&#{};'.format(ord(letter))
        else:
            encoded_payload += letter
    logging.info("Partial HTML entities decimal encoding:")
    logging.info(f"{encoded_payload}")
    
    # Full HTML decimal encoding
    encoded_payload = ''
    for letter in payload:
        encoded_payload += '&#{};'.format(ord(letter))
    logging.info("Full HTML entities decimal encoding:")
    logging.info(f"{encoded_payload}")
    
    # Partial HTML decimal encoding with five zeros
    encoded_payload = ''
    for letter in payload:
        if letter not in string.ascii_letters and letter not in string.digits:
            encoded_payload += '&#00000{};'.format(ord(letter))
        else:
            encoded_payload += letter
    logging.info("Partial HTML entities decimal encoding with five zeros:")
    logging.info(f"{encoded_payload}")
    
    # Full HTML decimal encoding with five zeros
    encoded_payload = ''
    for letter in payload:
        encoded_payload += '&#00000{};'.format(ord(letter))
    logging.info("Full HTML entities decimal encoding with five zeros:")
    logging.info(f"{encoded_payload}")
    
    # Partial HTML decimal encoding with ten zeros
    encoded_payload = ''
    for letter in payload:
        if letter not in string.ascii_letters and letter not in string.digits:
            encoded_payload += '&#0000000000{};'.format(ord(letter))
        else:
            encoded_payload += letter
    logging.info("Partial HTML entities decimal encoding with ten zeros:")
    logging.info(f"{encoded_payload}")
    
    
    # Full HTML decimal encoding with ten zeros
    encoded_payload = ''
    for letter in payload:
        encoded_payload += '&#0000000000{};'.format(ord(letter))
    logging.info("Full HTML entities decimal encoding with ten zeros:")
    logging.info(f"{encoded_payload}")
    
    
    # Partial HTML hexadecimal encoding
    encoded_payload = ''
    for letter in payload:
        if letter not in string.ascii_letters and letter not in string.digits:
            hexa = letter.encode('latin-1').hex()
            encoded_payload += '&#x{};'.format(hexa)
        else:
            encoded_payload += letter
    logging.info("Partial HTML entities hexadecimal encoding:")
    logging.info(f"{encoded_payload}")
    
    
    # Full HTML hexadecimal encoding
    encoded_payload = ''
    for letter in payload:
        hexa = letter.encode('latin-1').hex()
        encoded_payload += '&#x{};'.format(hexa)
    logging.info("Full HTML entities hexadecimal encoding:")
    logging.info(f"{encoded_payload}")
    
    
    # Unicode encoding
    encoded_payload = ''
    for letter in payload:
        encoded_payload += '\\u00{0:x}'.format(ord(letter))
    logging.info("Unicode:")
    logging.info(f"{encoded_payload}")
    
    # ECMAScript6 encoding
    encoded_payload = ''
    for letter in payload:
        encoded_payload += '\\u' + "{" + '{0:x}'.format(ord(letter)) + "}"
    logging.info("ES6:")
    logging.info(f"{encoded_payload}")
    
    # ECMAScript6 encoding with five zeros
    encoded_payload = ''
    for letter in payload:
        encoded_payload += '\\u' + "{00000" + '{0:x}'.format(ord(letter)) + "}"
    logging.info("ES6 with five zeros:")
    logging.info(f"{encoded_payload}")
    
    
    # ECMAScript6 encoding with ten zeros
    encoded_payload = ''
    for letter in payload:
        encoded_payload += '\\u' + "{0000000000" + '{0:x}'.format(ord(letter)) + "}"
    logging.info("ES6 with ten zeros:")
    logging.info(f"{encoded_payload}")
    
    # Hex escaping
    hex_escape = ''
    for i in payload:
        hexa = i.encode('latin-1').hex()
        hex_escape += '\\x' + hexa
    logging.info("Hex escaping:")
    logging.info(f"{hex_escape}")
    
    # Octal escaping
    encoded_payload = ''
    for letter in payload:
        encoded_payload += '\\{0:o}'.format(ord(letter))
    logging.info("Octal escaping:")
    logging.info(f"{encoded_payload}")
    
    
    # SQL Char in decimal
    encoded_payload = ''
    for letter in payload:
        encoded_payload += 'CHAR({})+'.format(ord(letter))
    logging.info("SQL Char in decimal:")
    logging.info(f"{encoded_payload[:-1]}")
    
    
    
    # SQL Char in hex
    encoded_payload = ''
    for letter in payload:
        encoded_payload += 'CHAR(x{0:x})+'.format(ord(letter))
    logging.info("SQL char in hex:")
    logging.info(f"{encoded_payload[:-1]}")



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
