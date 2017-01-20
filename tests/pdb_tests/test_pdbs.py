from unittest import TestCase
from unittest.mock import patch, Mock, call
from molecupy.pdb.pdb import Pdb
from molecupy.pdb.pdbdatafile import PdbDataFile
from molecupy.structures import Model, SmallMolecule, Chain, Residue, BindSite
from molecupy.structures import AlphaHelix, BetaStrand, Complex

class PdbTest(TestCase):

    def setUp(self):
        self.data_file = Mock(PdbDataFile)
        self.data_file.models.return_value = [
         {"model_id": 1, "start_record": 0, "end_record": 0}
        ]
        self.data_file.heteroatoms.return_value = []
        self.data_file.atoms.return_value = []
        self.data_file.get_remark_by_number.return_value = {}
        self.data_file.connections.return_value = []
        self.data_file.ss_bonds.return_value = []
        self.data_file.links.return_value = []
        self.data_file.sites.return_value = []
        self.data_file.helices.return_value = []
        self.data_file.sheets.return_value = []
        self.data_file.compounds.return_value = []


class PdbCreationTests(PdbTest):

    def test_can_create_pdb(self):
        pdb = Pdb(self.data_file)
        self.assertIs(pdb._data_file, self.data_file)


    def test_pdb_repr(self):
        pdb = Pdb(self.data_file)
        self.data_file.pdb_code.return_value = None
        self.assertEqual(str(pdb), "<Pdb (????)>")
        self.data_file.pdb_code.return_value = "1SAM"
        self.assertEqual(str(pdb), "<Pdb (1SAM)>")



class PdbPropertyTests(PdbTest):

    def test_data_file_property(self):
        pdb = Pdb(self.data_file)
        self.assertIs(pdb._data_file, pdb.data_file())


    def test_can_get_data_attributes(self):
        self.data_file.classification.return_value = "val1",
        self.data_file.deposition_date.return_value = "val2",
        self.data_file.pdb_code.return_value = "val3",
        self.data_file.is_obsolete.return_value = "val4",
        self.data_file.obsolete_date.return_value = "val5",
        self.data_file.replacement_code.return_value = "val6",
        self.data_file.title.return_value = "val7",
        self.data_file.split_codes.return_value = "val8",
        self.data_file.caveat.return_value = "val9",
        self.data_file.keywords.return_value = "val10",
        self.data_file.experimental_techniques.return_value = "val11",
        self.data_file.model_count.return_value = "val12",
        self.data_file.model_annotations.return_value = "val13",
        self.data_file.authors.return_value = "val14",
        self.data_file.revisions.return_value = "val15",
        self.data_file.supercedes.return_value = "val16",
        self.data_file.supercede_date.return_value = "val17",
        self.data_file.journal.return_value = "val18"
        pdb = Pdb(self.data_file)
        self.assertIs(
         pdb.classification(),
         self.data_file.classification()
        )
        self.assertIs(
         pdb.deposition_date(),
         self.data_file.deposition_date()
        )
        self.assertIs(
         pdb.pdb_code(),
         self.data_file.pdb_code(),
        )
        self.assertIs(
         pdb.is_obsolete(),
         self.data_file.is_obsolete()
        )
        self.assertIs(
         pdb.obsolete_date(),
         self.data_file.obsolete_date()
        )
        self.assertIs(
         pdb.replacement_code(),
         self.data_file.replacement_code()
        )
        self.assertIs(
         pdb.title(),
         self.data_file.title()
        )
        self.assertIs(
         pdb.split_codes(),
         self.data_file.split_codes()
        )
        self.assertIs(
         pdb.caveat(),
         self.data_file.caveat()
        )
        self.assertIs(
         pdb.keywords(),
         self.data_file.keywords()
        )
        self.assertIs(
         pdb.experimental_techniques(),
         self.data_file.experimental_techniques()
        )
        self.assertIs(
         pdb.model_count(),
         self.data_file.model_count()
        )
        self.assertIs(
         pdb.model_annotations(),
         self.data_file.model_annotations()
        )
        self.assertIs(
         pdb.revisions(),
         self.data_file.revisions()
        )
        self.assertIs(
         pdb.supercedes(),
         self.data_file.supercedes()
        )
        self.assertIs(
         pdb.supercede_date(),
         self.data_file.supercede_date()
        )
        self.assertIs(
         pdb.journal(),
         self.data_file.journal()
        )



class PdbModelsTests(PdbTest):

    @patch("molecupy.converters.pdbdatafile2model.model_from_pdb_data_file")
    def test_can_create_single_model(self, mock_converter):
        pdb = Pdb(self.data_file)
        value = "Return value"
        mock_converter.return_value = value
        mock_converter.assert_called_once_with(self.data_file, 1)
        self.assertEqual(len(pdb.models()), 1)
        self.assertIs(Pdb(self.data_file).models()[0], value)


    @patch("molecupy.converters.pdbdatafile2model.model_from_pdb_data_file")
    def test_can_create_multiple_model(self, mock_converter):
        self.data_file.models.return_value = [
         {"model_id": 1, "start_record": 1, "end_record": 3},
         {"model_id": 2, "start_record": 4, "end_record": 6}
        ]
        mock_converter.side_effect = ("Return value 1", "Return value 2")
        pdb = Pdb(self.data_file)
        calls = [call(self.data_file, 1), call(self.data_file, 2)]
        mock_converter.assert_has_calls(calls)
        self.assertEqual(len(pdb.models()), 2)
        self.assertEqual(pdb.models()[0], "Return value 1")
        self.assertEqual(pdb.models()[1], "Return value 2")


    def test_one_model_access(self):
        self.data_file.models.return_value = [
         {"model_id": 1, "start_record": 1, "end_record": 3},
         {"model_id": 2, "start_record": 4, "end_record": 6}
        ]
        pdb = Pdb(self.data_file)
        self.assertIs(pdb.models()[0], pdb.model())


    def test_models_are_read_only(self):
        pdb = Pdb(self.data_file)
        self.assertEqual(len(pdb.models()), 1)
        pdb.models().append("crap")
        self.assertEqual(len(pdb.models()), 1)
