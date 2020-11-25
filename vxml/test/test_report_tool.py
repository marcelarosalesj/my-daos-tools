''' Unit Testing for report tool module '''
import os

from vxml import VXMLReportTool
from vxml import VXMLReport
from vxml import VXMLError

CURRENT_PATH = os.getcwd()
TEST_XML_PATH = '{}/vxml/test/xmls'.format(CURRENT_PATH)

def test_report_tool_init():
    ''' Test report tool contructor '''
    report_tool = VXMLReportTool()
    assert isinstance(report_tool, VXMLReportTool)

