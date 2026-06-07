# AI Automation Suite CLI

A unified CLI toolkit to perform AI-based summarization, classification, extraction, and email generation.

## Usage Instructions
Run the `main.py` entrypoint specifying `--task`, `--input`, and optionally `--dry-run`.

### Command Examples
```bash
# Summarization (Simulation mode)
python main.py --task summarize --input data/article.txt --dry-run

# Email Draft dispatching
python main.py --task email --input recipient@demo.com
```
