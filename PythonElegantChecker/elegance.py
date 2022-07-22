import os
from nltk.downloader import download as nltk_download
from nltk.corpus import words as nltk_words
from flake8.api import legacy as flake8
from radon import complexity, raw, metrics


class Elegance:
    def __init__(self) -> None:
        """
        Initializes dictionary and the style guide.
        """
        nltk_download('words')
        word_list = nltk_words.words()
        self.word_set = set(word_list)
        self.style_guide = None
        self.reset_style_guide()

    def reset_style_guide(self) -> None:
        """
        Resets the style guide.
        """
        # recommended set of rules by sider
        # https://github.com/sider/runners/blob/bdc863bd5faf78f820fc05dcfad7cd5a27613f78/images/flake8/sider_recommended_flake8.ini
        self.style_guide = flake8.get_style_guide(ignore=['E121', 'E126', 'E127', 'E128', 'E203',
                                                          'E225', 'E226', 'E231', 'E241', 'E251',
                                                          'E261', 'E265', 'E302', 'E303', 'E305',
                                                          'E402', 'E501', 'E741', 'W291', 'W292',
                                                          'W293', 'W391', 'W503', 'W504', 'F403',
                                                          'B007', 'B950'],
                                                  max_line_length=200)
        # self.style_guide = flake8.get_style_guide()

    def __get_flake8_report(self, file_path: str = None) -> flake8.Report:
        """
        Checks the elegance of a file.

        :param file_path: str: file path
        :returns: flake8.api.legacy.Report
        """
        self.reset_style_guide()
        if file_path is None:
            file_path = os.getcwd()
        return self.style_guide.input_file(file_path)

    def get_PEP8_metrics(self, files: list[str]) -> list[list[str]]:
        """
        Returns the PEP8 violations of a list of code files.

        :param files:
        :returns: list[list[str]]
        """
        reports = []
        for file in files:
            report = self.__get_flake8_report(file)
            reports.append(report.get_statistics(''))
        return reports


def get_cyclomatic_metrics(codes: list[str]) -> list[list[int]]:
    """
    Returns the cyclomatic complexities of a list of codes.

    :param codes: strings of raw code
    :returns: list[list[int]]
    """
    depths = []
    for code in codes:
        elements = complexity.cc_visit(code)
        depths.append([element.complexity for element in elements])
    return depths


def get_raw_metrics(codes: list[str]) -> list[list[int]]:
    """
    Returns the raw metrics of a list of codes.

    :param codes: strings of raw code
    :returns: list[list[int]]
    """
    raw_metrics = []
    for code in codes:
        analyzed = raw.analyze(code)
        raw_metrics.append([analyzed.loc, analyzed.sloc, analyzed.comments])
    return raw_metrics


def get_mi_metrics(codes: list[str]) -> list[float]:
    """
    Returns the MI metrics of a list of codes.

    :param codes: strings of raw code
    :returns: list[float]
    """
    return [metrics.mi_visit(code, True) for code in codes]
