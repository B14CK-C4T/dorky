# dorky

---

### **README.md**  
```md
# DORKY is a Google Dork Search Tool  

A Python script that automates Google Dorking to find indexed information using advanced search queries. This tool allows you to search and optionally save the results to a text file.  

## Features  
- Perform Google Dork queries  
- Set a custom output limit  
- Save results to a file    

## Requirements  
- Python 3.x  
- `googlesearch-python` module (for querying Google)  

## Installation  

1. Clone the repository or download the script:  
   ```bash
   git clone https://github.com/your-repo/dork-search-tool.git
   cd dorky
   ```

2. Create a Virtual Environment:
```bash
python -m venv venv
```
Activate the virtual environment:
- **Linux/macOS**:  
  ```bash
  source venv/bin/activate
  ```
- **Windows**:  
  ```powershell
  venv\Scripts\activate
  ```

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

## Usage  

Run the script:  
```bash
python dorky.py
```

Follow the prompts:  
- Enter a **Google Dork query** (e.g., `site:example.com`)  
- Specify the **output limit**  
- Choose whether to **save results**  

Example interaction:  
```
Enter the dork query to search: site:example.com  
Enter the output limit: 5  
[1] https://example.com/page1  
[2] https://example.com/page2  
...
Do you want to save the output? (y/n): y  
Enter the file name: results  
Results saved to output/results.txt  
```

## Notes   
- If you get errors, try changing the `pause` parameter in the script to avoid rate limits.  

## Disclaimer  
The author is not responsible for any misuse of this tool. Ensure compliance with Google’s Terms of Service.  
