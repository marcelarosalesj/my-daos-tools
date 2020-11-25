''' Unit Testing for report module '''
import os

from vxml import VXMLReport
from vxml import VXMLError

CURRENT_PATH = os.getcwd()
TEST_XML_PATH = '{}/vxml/test/xmls'.format(CURRENT_PATH)

def test_report_init():
    ''' Test report constructor '''
    report = VXMLReport()
    assert isinstance(report, VXMLReport)

def test_report_load():
    ''' Test report load function '''
    report = VXMLReport()
    assert len(report.errors) == 0
    report.load('{}/example.xml'.format(TEST_XML_PATH))
    assert len(report.errors) == 31
    # TO-DO: Add asserts for command and file_path

def test_report_len():
    ''' Test report len works '''
    report = VXMLReport()
    report.load('{}/example.xml'.format(TEST_XML_PATH))
    assert len(report) == 31

def test_report_count():
    ''' Test report count function '''
    report = VXMLReport()
    report.load('{}/example.xml'.format(TEST_XML_PATH))
    result = report.count('Leak_StillReachable')
    assert result == 9
    result = report.count('Leak_DefinitelyLost')
    assert result == 16
    result = report.count('Leak_IndirectlyLost')
    assert result == 5
    result = report.count('Leak_PossiblyLost')
    assert result == 1

def test_report_get_kinds():
    ''' Test report get_kinds function '''
    report = VXMLReport()
    report.load('{}/example.xml'.format(TEST_XML_PATH))
    result = report.get_kinds()
    assert set(result) == set(['Leak_StillReachable',
                               'Leak_DefinitelyLost',
                               'Leak_IndirectlyLost',
                               'Leak_PossiblyLost'])

def test_report_print():
    ''' Test report __str__ works '''
    file_line = '{}/example.xml'.format(TEST_XML_PATH)
    command_line = '/home/marosale/Repos/daos/install/bin/vos_tests -A 50'
    expected_string = '\n{}\n'.format('-'*100)
    expected_string += 'File: {}\n'.format(file_line)
    expected_string += 'Number of errors: {}\n'.format('31')
    expected_string += 'Command: {}\n'.format(command_line)
    expected_string += '{}\n'.format('-'*100)
    expected_string += '{}:\t{}\n'.format('Leak_StillReachable', '9')
    expected_string += '{}:\t{}\n'.format('Leak_DefinitelyLost', '16')
    expected_string += '{}:\t{}\n'.format('Leak_IndirectlyLost', '5')
    expected_string += '{}:\t{}\n'.format('Leak_PossiblyLost', '1')
    expected_string += '{}\n'.format('-'*100)
    report = VXMLReport()
    report.load('{}/example.xml'.format(TEST_XML_PATH))
    assert str(report) == expected_string

def test_report_iterate():
    ''' Test report iterator works '''
    report = VXMLReport()
    report.load('{}/example.xml'.format(TEST_XML_PATH))
    for error in report:
        assert isinstance(error, VXMLError)

def test_report_get_file_path():
    ''' Test report get_file_path function '''
    report = VXMLReport()
    report.load('{}/example.xml'.format(TEST_XML_PATH))
    name = report.get_file_path()
    assert name == 'example.xml'
    name = report.get_file_path(complete=True)
    assert name == '{}/example.xml'.format(TEST_XML_PATH)
