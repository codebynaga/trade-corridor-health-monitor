from pathlib import Path
import argparse
import shutil

DATASET = 'sergionefedov/global-supply-chain-and-trade-disruptions-25-years'
EXPECTED = ('trade_flows.csv', 'shipping_rates.csv', 'tariff_timeline.csv', 'commodity_prices_supply_chain.csv', 'disruption_events.csv', 'industry_exposure.csv')

def main():
    parser = argparse.ArgumentParser(description='Download source dataset from Kaggle and locate required CSV files.')
    parser.add_argument('--source-dir', type=Path, help='Use a manually downloaded and extracted Kaggle dataset instead of downloading')
    args = parser.parse_args()
    if args.source_dir:
        source = args.source_dir.expanduser().resolve()
    else:
        try:
            import kagglehub
        except ImportError as exc:
            raise SystemExit('Install kagglehub first: python -m pip install kagglehub') from exc
        source = Path(kagglehub.dataset_download(DATASET)).resolve()
    if not source.is_dir():
        raise SystemExit(f'Dataset directory not found: {source}')
    target = Path(__file__).resolve().parents[1] / 'data' / 'raw'
    target.mkdir(parents=True, exist_ok=True)
    found = {p.name.lower(): p for p in source.rglob('*.csv')}
    missing = []
    for filename in EXPECTED:
        match = found.get(filename.lower())
        if match is None:
            missing.append(filename)
            continue
        destination = target / filename
        if match.resolve() != destination.resolve():
            shutil.copy2(match, destination)
        print(f'OK {filename}')
    if missing:
        print('\nDataset CSV files discovered:')
        for p in sorted(source.rglob('*.csv')):
            print(' -', p.relative_to(source))
        raise SystemExit('Missing expected files: ' + ', '.join(missing) + '. Check source naming/schema before renaming or transforming files.')
    print(f'\nSix source CSVs are available at {target}. This does not validate schemas or model results.')

if __name__ == '__main__':
    main()
