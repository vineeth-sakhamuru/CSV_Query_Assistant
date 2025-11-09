## What is this?
- Ever wished you could just ask questions about your data instead of searching through rows and columns? This project lets you do exactly that. Upload a CSV file and chat with it using plain English. No SQL required, seriously.

## How it works
- You provide a CSV file
- The chatbot parses your questions, finds the answer, and responds conversationally
- Built with Python and LangChain, so it's easy to extend and customize

## Try it out
- Clone this repo

```bash
git clone https://github.com/vineeth-sakhamuru/csv-chatbot.git
cd csv-chatbot
```
## Install requirements

```bash
pip install -r requirements.txt
```
## Run the chatbot
(Set your CSV file path in main.py)
```bash
python main.py
```

## Example questions
- Which county has the highest population?
- What’s the average sales in Q1?
- Show me all entries where status is "active".

## Why I built this
- I wanted a smarter way to explore tabular data—whether it’s for quick analysis, teaching, or just making data less intimidating. If you find bugs, have suggestions, or just want to use this for your data, happy to connect!

## Tech
- Python 3.8+
- LangChain
