import unittest
from html_testRunner import HTMLTestRunner
from html_testRunner import HTMLTestRunner

from your_test_module import TestBooks

if __name__ == '__main__':
    # Definirea testelor care vor fi incluse în raport
    test_classes_to_run = [TestBooks]

    # Crearea unui loader de test
    loader = unittest.TestLoader()

    # Adăugarea testelor în test suite
    test_suite = unittest.TestSuite()
    for test_class in test_classes_to_run:
        tests = loader.loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)

    # Specificarea locației și numele raportului HTML
    report_path = 'test_report.html'

    # Rularea testelor și generarea raportului HTML
    with open(report_path, 'w') as report_file:
        runner = HTMLTestRunner(
            stream=report_file,
            title='Test Report',
            description='Tests for the Books API'
        )
        runner.run(test_suite)
