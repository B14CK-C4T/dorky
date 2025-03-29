#!/usr/bin/env/python3
#######################################################################################
# * DORKY 
# * Copyright (c) 2025 B14CK_C4T
# * 
# * this program is free software: you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation, either version 3 of the License, or
# * (at your option) any later version.
# * 
# * this program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# * GNU General Public License for more details.
# * 
# * You should have received a copy of the GNU General Public License
# * along with this program. If not, see <http://www.gnu.org/licenses/>.
########################################################################################

import sys
from random import choice
import time
try:
    from googlesearch import search
except ImportError:
    print("Module not found! Install it using: pip install google")
    sys.exit(1)

user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/74.0",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.172",
        ]
        
google_tlds = ["com", "ca", "in", "au", "de", "fr"]

def load_dorks(filename):
    """Loads Google Dork queries from a file."""
    try:
        with open(filename, 'r') as file:
            dorks = [line.strip() for line in file if line.strip()]
        return dorks
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        sys.exit(1)

def save_results(results, filename):
    """Saves results to a text file."""
    dir_name = "output"
    os.makedirs(dir_name, exist_ok=True) # create the output directory if it doesn't exist
    file_path = os.path.join(dir_name, filename)
    with open(f"{file_path}.txt", 'w') as file:
        for dork, urls in results.items():
            file.write(f"{dork}\n")
            file.writelines(f"  - {url}\n" for url in urls)
            file.write("\n")

def run_dorks(domain, dork_file):
    """Executes dork queries and retrieves results."""
    dorks = load_dorks(dork_file)
    results = {}
    
    for dork in dorks:
        query = dork.replace("{domain}", domain)
        print(f"[+] Searching: {query}")
        urls = []
        try:
            for result in search(query, lang='en', num=5, pause=5, tld=choice(google_tlds), user_agent=choice(user_agents)):
                print(f"  - {result}")
                urls.append(result)
            results[query] = urls
        except Exception as e:
            print(f"  [!] Error searching: {e}")
        time.sleep(1)  # Avoid rate limits
    return results

def main():
    """Main function to execute the tool."""
    domain = input("Enter the target domain: ").strip()
    dork_file = "dork.txt"
    results = run_dorks(domain, dork_file)
    
    save_option = input("Do you want to save the results? (y/n): ").lower()
    if save_option.startswith('y'):
        filename = input("Enter the output file name: ").strip()
        save_results(results, filename)
        print(f"Results saved to {filename}.txt")
    else:
        print("Results not saved.")

if __name__ == "__main__":
    main()



            
    
