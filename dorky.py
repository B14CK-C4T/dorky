#!/usr/bin/env/python3

import sys
import os

try:
    from googlesearch import search
except ImportError:
    print("[!] Module not found! Install it using: pip install google")

def save(data, filename):
    """Saves data to a text file."""
    with open(f"{filename}.txt", 'a') as file:
        for entry in data:
            file.write(f"{entry[0]}. {entry[1]}\n")

def dork_query():
    """Performs a Google dork search."""
    try:
        query = input("[*] Enter the dork query to search: ")
        limit = int(input("[*] Enter the output limit: "))

        results = []
        for counter, response in enumerate(search(query, lang='en', num=limit, start=0, stop=limit, pause=2), start=1):
            print(f"[{counter}] {response}")
            results.append((counter, response))
            
        return results
    
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)

def main():
    folder_name = "output"
    if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            
    save_output = input("[*] Do you want to save the output? (y/n): ").strip().lower()
    
    data = dork_query()  # Get results

    if save_output.startswith("y"):
        filename = input("[!] Enter the file name: ").strip()
        filepath = os.path.join(folder_name, filename)
        save(data, filepath)
        print(f"[-] Results saved to {filepath}.txt")
    else:
        print("[!] Skipped saving.")

if __name__ == "__main__":
    main()



            
    