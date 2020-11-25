''' Unit Testing for report tool module '''
import os
import pytest

from vxml import VXMLReportTool
from vxml import VXMLReport
from vxml import VXMLError

CURRENT_PATH = os.getcwd()
TEST_XML_PATH = '{}/vxml/test/xmls'.format(CURRENT_PATH)

def test_report_tool_init():
    ''' Test report tool constructor '''
    report_tool = VXMLReportTool()
    assert isinstance(report_tool, VXMLReportTool)

def test_report_tool_setup_path():
    '''Test report tool basic setup with dir path'''
    report_tool = VXMLReportTool()
    report_tool.setup(path=TEST_XML_PATH)
    assert len(report_tool.reports) == 3
    assert isinstance(report_tool.reports[0], VXMLReport)

def test_report_tool_setup_file():
    '''Test report tool basic setup with file path'''
    report_tool = VXMLReportTool()
    report_tool.setup(path='{}/example1.xml'.format(TEST_XML_PATH))
    assert len(report_tool.reports) == 1 
    assert isinstance(report_tool.reports[0], VXMLReport)

def test_report_tool_print_single_report(capsys):
    '''Test report tool print single report'''
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
    report_tool = VXMLReportTool()
    report_tool.setup(path='{}/example.xml'.format(TEST_XML_PATH))
    report_tool.print_reports()
    out, err = capsys.readouterr()
    assert out == expected_string

def test_report_tool_print_three_reports(capsys):
    '''TO-DO'''
    pass

def test_report_tool_print_single_report_reverse(capsys):
    '''TO-DO'''
    pass
