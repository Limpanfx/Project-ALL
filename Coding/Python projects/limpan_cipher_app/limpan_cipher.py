"""
Limpan Cipher - A custom encoder/decoder inspired by the name "Limpan"
This module provides functions to encode English text to Limpan code and decode it back.
"""

import argparse
import re
import sys

class LimpanCipher:
    """
    A class that implements the Limpan cipher for encoding and decoding text.
    """

    VOWEL_MAP = {
        'a': 'im', 
        'e': 'pa',
        'i': 'li',
        'o': 'mo',
        'u': 'nu',
        'A': 'Im',
        'E': 'Pa',
        'I': 'Li',
        'O': 'Mo',
        'U': 'Nu'
    }
    
    REVERSE_VOWEL_MAP = {v: k for k, v in VOWEL_MAP.items()}
    
    @staticmethod
    def transform_consonant(char):
        """Transform a consonant according to Limpan rules."""
        if char.isalpha():
            suffix = 'an' if char.islower() else 'An'
            return char + suffix
        return char
    
    @staticmethod
    def is_limpan_consonant(text):
        """Check if a string matches the pattern of a Limpan-encoded consonant."""
        return (len(text) == 3 and 
                text[0].isalpha() and 
                text[1:].lower() == 'an')
    
    @classmethod
    def encode(cls, text):
        """
        Encode English text to Limpan code.
        
        Args:
            text (str): The English text to encode
            
        Returns:
            str: The encoded Limpan text
        """
        if not text:
            return ""
        
        result = []
        i = 0
        while i < len(text):
            char = text[i]
            
            if char.lower() in 'aeiou':
                result.append(cls.VOWEL_MAP[char])
            elif char.isalpha():
                result.append(cls.transform_consonant(char))
            else:
                result.append(char)
            i += 1
            
        return ''.join(result)
    
    @classmethod
    def decode(cls, text):
        """
        Decode Limpan code to English text.
        
        Args:
            text (str): The Limpan code to decode
            
        Returns:
            str: The decoded English text
        """
        if not text:
            return ""
        result = []
        i = 0
        while i < len(text):
            if i <= len(text) - 3 and cls.is_limpan_consonant(text[i:i+3]):
                result.append(text[i])  
                i += 3  
            else:
                vowel_found = False
                for limpan_vowel, english_vowel in cls.REVERSE_VOWEL_MAP.items():
                    if i <= len(text) - len(limpan_vowel) and text[i:i+len(limpan_vowel)] == limpan_vowel:
                        result.append(english_vowel)
                        i += len(limpan_vowel)
                        vowel_found = True
                        break
                if not vowel_found:
                    result.append(text[i])
                    i += 1
                
        return ''.join(result)


def main():
    """Main function to handle command-line arguments and process text."""
    parser = argparse.ArgumentParser(description='Limpan Cipher - Encode/Decode Text')
    parser.add_argument('mode', choices=['encode', 'decode'], 
                        help='Operation mode: encode (English to Limpan) or decode (Limpan to English)')
    parser.add_argument('text', nargs='?', help='Text to encode/decode (if not provided, reads from stdin)')
    
    args = parser.parse_args()
    if args.text:
        input_text = args.text
    else:
        print(f"Enter text to {args.mode} (press Ctrl+D when done):", file=sys.stderr)
        input_text = sys.stdin.read().strip()
    if args.mode == 'encode':
        result = LimpanCipher.encode(input_text)
        print(f"Encoded Limpan text: {result}")
    else: 
        result = LimpanCipher.decode(input_text)
        print(f"Decoded English text: {result}")


if __name__ == "__main__":
    main()
