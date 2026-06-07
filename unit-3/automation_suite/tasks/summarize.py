def run(file_path, dry_run=False):
    if dry_run:
        return f'[Dry-Run] Summarizing text file: {file_path}'
    return f'[API-Success] Here is a short summary of the text from {file_path}.'
