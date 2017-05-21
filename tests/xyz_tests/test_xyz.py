from unittest import TestCase
from unittest.mock import patch, Mock
from atomium.xyz.xyz import Xyz
from atomium.structures.models import Model

class XyzCreationTests(TestCase):

    def test_can_create_xyz(self):
        xyz = Xyz()
        self.assertEqual(xyz._model, None)
        self.assertEqual(xyz._comment, "")


    def test_can_create_xyz_with_comment(self):
        xyz = Xyz("Glucose molecule")
        self.assertEqual(xyz._model, None)
        self.assertEqual(xyz._comment, "Glucose molecule")


    def test_xyz_comment_must_be_str(self):
        with self.assertRaises(TypeError):
            Xyz(100)



class XyzReprTests(TestCase):

    def test_xyz_repr(self):
        xyz = Xyz("Glucose molecule")
        self.assertEqual(str(xyz), "<Xyz (Glucose molecule)>")



class XyzCommentTests(TestCase):

    def test_comment_property(self):
        xyz = Xyz("Glucose molecule")
        self.assertIs(xyz._comment, xyz.comment())


    def test_can_change_comment(self):
        xyz = Xyz("Glucose molecule")
        xyz.comment("Fructose molecule")
        self.assertEqual(xyz._comment, "Fructose molecule")


    def test_xyz_comment_must_be_str(self):
        xyz = Xyz("Glucose molecule")
        with self.assertRaises(TypeError):
            xyz.comment(100)



class XyzModelTests(TestCase):

    def test_model_property(self):
        xyz = Xyz("Glucose molecule")
        xyz._model = "totally a model"
        self.assertIs(xyz._model, xyz.model())


    def test_can_change_model(self):
        model = Mock(Model)
        xyz = Xyz("Glucose molecule")
        xyz.model(model)
        self.assertIs(xyz._model, model)


    def test_xyz_model_must_be_model(self):
        xyz = Xyz("Glucose molecule")
        with self.assertRaises(TypeError):
            xyz.model(100)