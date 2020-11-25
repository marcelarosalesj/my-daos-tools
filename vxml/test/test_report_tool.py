''' Unit Testing for report tool module '''
import os

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
