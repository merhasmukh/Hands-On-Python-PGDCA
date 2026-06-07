def run(file_path, dry_run=False):
    if dry_run:
        return f'[Dry-Run] Classifying rows in csv: {file_path}'
    return f'[API-Success] Batch classification complete for {file_path}.'
