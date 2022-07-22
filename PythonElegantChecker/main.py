import elegance
import utils


def main():
    instance = elegance.Elegance()

    print('file check:')
    files = utils.get_files_by_dir()
    reports = instance.get_PEP8_metrics(files)
    violation_counts = [len(report) for report in reports]
    print(violation_counts)

    print('code check:')
    codes = utils.get_codes(files)
    depths = elegance.get_cyclomatic_metrics(codes)
    max_depths = [max(depth) if len(depth) > 0 else 0 for depth in depths]
    raw_metrics = elegance.get_raw_metrics(codes)
    mi_metrics = elegance.get_mi_metrics(codes)

    print('depths:', depths)
    print('max depths:', max_depths)
    print('raw metrics:', raw_metrics)
    print('mi metrics:', mi_metrics)


if __name__ == '__main__':
    main()
