# bread_crumbs

A small Python web-crawler that follows the breadcrumb trail on
[autbor.com/breadcrumbs](https://autbor.com/breadcrumbs/).

The script visits the starting page, finds the first HTML page name in the text
of the first `<div>` element, and follows that link. It stops when the page text
contains no additional link or prints the final message when the trail ends.

## Requirements

- Python 3
- `requests`
- `beautifulsoup4`

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies:

```bash
python3 -m pip install requests beautifulsoup4
```

## Usage

Run the crawler from the project root:

```bash
python3 main.py
```

Example output:

```text
Visiting: https://autbor.com/breadcrumbs/
Reached the end! Final message: <final page message>
```
