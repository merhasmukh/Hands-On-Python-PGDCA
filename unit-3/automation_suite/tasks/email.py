def run(recipient, dry_run=False):
    if dry_run:
        return f'[Dry-Run] Drafted email notification to: {recipient}'
    return f'[API-Success] Email notification dispatch queued to {recipient}.'
