# Site Connectivity Checker

A Python project to check the connectivity status of websites. This tool helps you quickly determine if a website is online or offline by sending HTTP requests and reporting the result.

## Features

- Check if a website is reachable (online/offline).
- Supports checking multiple sites.
- Simple command-line interface.
- Displays response status codes and error messages.

## Requirements

- Python 3.x
- [requests](https://pypi.org/project/requests/)

## Installation

1. Clone the repository or download the source code.
2. Install the required package:
    ```bash
    pip install requests
    ```

## Usage

Run the main script and enter the website URL(s) you want to check:

```bash
python src/site_connectivity_checker.py
```

Example output:
```
Checking connectivity for: https://www.google.com
Status: Online (200 OK)

Checking connectivity for: https://www.nonexistentwebsite123.com
Status: Offline (Could not connect)
```

## Customization

- You can modify the script to check a list of URLs from a file.
- Adjust timeout settings in the code for slower connections.

## License

This project is licensed under the MIT License.

## Contact

For questions or feedback, please contact [amirabbas316](mailto:amirabbasc316@gmail.com).