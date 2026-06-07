def run(file_path, dry_run=False):
    if dry_run:
        return f'[Dry-Run] Extracting entities from: {file_path}'
    return f'[API-Success] Extracted entities output loaded from {file_path}.'
