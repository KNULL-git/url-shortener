# URL Shortener

This Python script provides a simple command-line URL shortener. It uses regex for URL validation and generates shortened URLs using cryptographic hashing.

### Features:

- **Shorten URL**: Enter a long URL to receive a shortened version.
- **Retrieve Original URL**: Input a shortened URL to get back the original long URL.
- **Validation**: Uses regex to ensure valid URLs are processed.
- **Persistence**: Shortened URLs are stored in memory during runtime.

### Usage:

1. **Clone the repository:**
   ```
   git clone https://github.com/your-username/url-shortener.git
   cd url-shortener
   ```

2. **Run the script:**
   ```
   python main.py
   ```

3. **Follow the prompts:**
   - Choose option `1` to shorten a URL.
   - Choose option `2` to retrieve the original URL from a shortened URL.
   - Option `3` exits the program.

### Requirements:

- Python 3.x (No additional libraries required)

### Example:

```
URL Shortener
1. Shorten URL
2. Retrieve original URL
3. Exit
Enter your choice: 1
Enter the URL to be shortened: https://example.com
Shortened URL: EDkJ4FTTUxwn

URL Shortener
1. Shorten URL
2. Retrieve original URL
3. Exit
Enter your choice: 2
Enter the shortened URL: EDkJ4FTTUxwn
Original URL: https://example.com

URL Shortener
1. Shorten URL
2. Retrieve original URL
3. Exit
Enter your choice: 3
Exiting...
```
