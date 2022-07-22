import elegance
import utils


def main():
    instance = elegance.Elegance()

    # check for PEP8 violations
    print('\nfile check:')
    files = utils.get_files_by_dir()
    reports = instance.get_PEP8_metrics(files)
    PEP8_violation_counts = [len(report) for report in reports]
    print('PEP8 violations:', reports)
    print('PEP8 violation counts:', PEP8_violation_counts)

    # check for code metrics
    print('\ncode check:')
    codes = utils.get_codes(files)
    depths = instance.get_cyclomatic_metrics(codes)
    max_depths = [max(depth) if len(depth) > 0 else 0 for depth in depths]
    mi_metrics = instance.get_mi_metrics(codes)
    # raw_metrics = elegance.get_raw_metrics(codes)

    print('depths:', depths)
    print('max depths:', max_depths)
    print('Maintainability Index metrics:', mi_metrics)
    # print('raw metrics:', raw_metrics)

    # check for variable names
    print('\nvariable name check:')
    # test tokens
    tokens = ['test', 'aaa', 'bbb', 'ccc', 'aaba', 'ab']
    violations = instance.check_name_correctness(tokens)
    violation_counts = violations.count(True)
    print('name violation counts:', violation_counts)


if __name__ == '__main__':
    main()
