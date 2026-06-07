import argparse
import sys
from tasks import summarize, classify, extract, email

def main():
    parser = argparse.ArgumentParser(description='AI Automation Suite CLI')
    parser.add_argument('--task', required=True, choices=['summarize', 'classify', 'extract', 'email'])
    parser.add_argument('--input', required=True, help='Input target path or recipient')
    parser.add_argument('--dry-run', action='store_true', help='Simulate API query without cost')
    
    args = parser.parse_args()
    
    if args.task == 'summarize':
        res = summarize.run(args.input, args.dry_run)
    elif args.task == 'classify':
        res = classify.run(args.input, args.dry_run)
    elif args.task == 'extract':
        res = extract.run(args.input, args.dry_run)
    elif args.task == 'email':
        res = email.run(args.input, args.dry_run)
        
    print('='*40)
    print('    AUTOMATION SUITE OUTPUT')
    print('='*40)
    print(res)
    print('='*40)

if __name__ == '__main__':
    main()
