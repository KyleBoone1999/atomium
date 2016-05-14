from unittest import TestCase
from molecupy.pdbfile import PdbRecord

class PdbRecordTest(TestCase):

    def setUp(self):
        self.line = "TEST   123  123.8    HYT"


    def check_pdb_record(self, pdb_record):
        self.assertIsInstance(pdb_record, PdbRecord)
        self.assertIsInstance(pdb_record.number, int)
        self.assertIsInstance(pdb_record.name, str)
        self.assertIsInstance(pdb_record.text, str)
        self.assertIsInstance(pdb_record.contents, str)
        self.assertEqual(len(pdb_record.text), 80)
        self.assertEqual(len(pdb_record.contents), 74)
        self.assertRegex(
         str(pdb_record),
         r"<PdbRecord \(.+\)>"
        )



class RecordCreationTests(PdbRecordTest):

    def test_can_create_pdb_record(self):
        pdb_record = PdbRecord(self.line, 23)
        self.check_pdb_record(pdb_record)
        self.assertEqual(pdb_record.number, 23)
        self.assertEqual(pdb_record.name, "TEST")
        self.assertTrue(pdb_record.contents.startswith(" 123  123.8    HYT"))
        self.assertTrue(pdb_record.text.startswith("TEST   123  123.8    HYT"))



class RecordAccessTests(PdbRecordTest):

    def test_can_get_individual_characters(self):
        pdb_record = PdbRecord(self.line, 23)
        self.assertEqual(pdb_record[0], "T")
        self.assertEqual(pdb_record[21], "H")


    def test_can_get_strings_from_record(self):
        pdb_record = PdbRecord(self.line, 23)
        self.assertEqual(pdb_record[1:4], "EST")
        self.assertEqual(pdb_record[21:24], "HYT")


    def test_record_indexes_will_strip_strings(self):
        pdb_record = PdbRecord(self.line, 23)
        self.assertEqual(pdb_record[0:7], "TEST")
        self.assertEqual(pdb_record[19:24], "HYT")
        self.assertEqual(pdb_record[19:34], "HYT")


    def test_records_can_covert_to_int(self):
        pdb_record = PdbRecord(self.line, 23)
        self.assertEqual(pdb_record[5:11], 123)


    def test_records_can_covert_to_float(self):
        pdb_record = PdbRecord(self.line, 23)
        self.assertEqual(pdb_record[10:19], 123.8)


    def test_can_force_record_to_return_string(self):
        pdb_record = PdbRecord(self.line, 23)
        self.assertEqual(pdb_record.get_as_string(5, 11), "123")
        self.assertEqual(pdb_record.get_as_string(10, 19), "123.8")


    def test_empty_sections_return_none(self):
        pdb_record = PdbRecord(self.line, 23)
        self.assertIs(pdb_record[17:21], None)
        self.assertIs(pdb_record.get_as_string(17, 21), None)
