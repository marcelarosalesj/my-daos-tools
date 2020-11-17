import pytest
import os

from vxml.report import VXML_Report
from vxml.error import VXML_Error

current_path = os.getcwd()
test_xml_path = '{}/vxml/test'.format(current_path)

def test_report_init():
	report = VXML_Report()
	assert isinstance(report, VXML_Report)	

def test_report_load():
	report = VXML_Report()
	assert len(report.errors) == 0 
	report.load('{}/example.xml'.format(test_xml_path))
	assert len(report.errors) == 31
	# TO-DO: Add asserts for command and file_path

def test_report_len():
	report = VXML_Report()
	report.load('{}/example.xml'.format(test_xml_path))
	assert len(report) == 31

def test_report_count():
	report = VXML_Report()
	report.load('{}/example.xml'.format(test_xml_path))
	result = report.count('Leak_StillReachable')
	assert result == 9
	result = report.count('Leak_DefinitelyLost')
	assert result == 16
	result = report.count('Leak_IndirectlyLost')
	assert result == 5
	result = report.count('Leak_PossiblyLost')
	assert result == 1

def test_report_get_kinds():
	report = VXML_Report()
	report.load('{}/example.xml'.format(test_xml_path))
	result = report.get_kinds()
	assert set(result) == set(['Leak_StillReachable',
				   'Leak_DefinitelyLost',
				   'Leak_IndirectlyLost',
				   'Leak_PossiblyLost'])	

def test_report_print():
	expected_string = '\n{}\n'.format('-'*100)
	expected_string += 'File: {}\n'.format('/home/marosale/Repos/my-daos-tools/vxml/test/example.xml')
	expected_string += 'Number of errors: {}\n'.format('31')
	expected_string += 'Command: {}\n'.format('/home/marosale/Repos/daos/install/bin/vos_tests -A 50')
	expected_string += '{}\n'.format('-'*100)
	expected_string += '{}:\t{}\n'.format('Leak_StillReachable', '9')
	expected_string += '{}:\t{}\n'.format('Leak_DefinitelyLost', '16')
	expected_string += '{}:\t{}\n'.format('Leak_IndirectlyLost', '5')
	expected_string += '{}:\t{}\n'.format('Leak_PossiblyLost', '1')
	expected_string += '{}\n'.format('-'*100)
	report = VXML_Report()
	report.load('{}/example.xml'.format(test_xml_path))
	assert str(report) == expected_string

def test_report_iterate():
	report = VXML_Report()
	report.load('{}/example.xml'.format(test_xml_path))
	for error in report:
		assert isinstance(error, VXML_Error)

def test_report_get_file_path():
	report = VXML_Report()
	report.load('{}/example.xml'.format(test_xml_path))
	name = report.get_file_path()
	assert name == 'example.xml'
	name = report.get_file_path(complete=True)
	assert name == '{}/example.xml'.format(test_xml_path)

