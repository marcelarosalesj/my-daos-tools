import pytest
import os

from vxml.report import VXML_Report

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
	report = VXML_Report()
	report.load('{}/example.xml'.format(test_xml_path))
	print(report)
