from unittest import TestCase
from molecupy import exceptions
from molecupy.atomic import Atom, Molecule
from molecupy.polymers import Monomer, MonomericStructure, Polymer

class PolymerTest(TestCase):

    def setUp(self):
        self.atom1 = Atom(1.0, 1.0, 1.0, "H", atom_id=1, atom_name="H1")
        self.atom2 = Atom(1.0, 1.0, 2.0, "C", atom_id=2, atom_name="CA")
        self.atom3 = Atom(1.0, 1.0, 3.0, "O", atom_id=3, atom_name="OX1")
        self.atom2.covalent_bond_to(self.atom1)
        self.atom2.covalent_bond_to(self.atom3)
        self.monomer1 = Monomer(1, "MON1", self.atom1, self.atom2, self.atom3)
        self.atom4 = Atom(1.0, 1.0, 4.0, "H", atom_id=4, atom_name="H1")
        self.atom5 = Atom(1.0, 1.0, 5.0, "C", atom_id=5, atom_name="CA")
        self.atom6 = Atom(1.0, 1.0, 6.0, "O", atom_id=6, atom_name="OX1")
        self.atom5.covalent_bond_to(self.atom4)
        self.atom5.covalent_bond_to(self.atom6)
        self.monomer2 = Monomer(2, "MON2", self.atom4, self.atom5, self.atom6)
        self.atom7 = Atom(1.0, 1.0, 7.0, "H", atom_id=7, atom_name="H1")
        self.atom8 = Atom(1.0, 1.0, 8.0, "C", atom_id=8, atom_name="CA")
        self.atom9 = Atom(1.0, 1.0, 9.0, "O", atom_id=9, atom_name="OX1")
        self.atom8.covalent_bond_to(self.atom7)
        self.atom8.covalent_bond_to(self.atom9)
        self.monomer3 = Monomer(3, "MON3", self.atom7, self.atom8, self.atom9)
        self.monomer1.connect_to(self.monomer2, self.atom3, self.atom4)
        self.monomer2.connect_to(self.monomer3, self.atom6, self.atom7)


    def check_valid_polymer(self, polymer):
        self.assertIsInstance(polymer, Polymer)
        self.assertIsInstance(polymer, MonomericStructure)
        self.assertIsInstance(polymer, Molecule)
        self.assertIsInstance(polymer.monomers, tuple)
        self.assertRegex(
         str(polymer),
         r"<Polymer \((\d+) monomers\)>"
        )



class PolymerCreationTests(PolymerTest):

    def test_can_create_polymer(self):
        polymer = Polymer(
         self.monomer1,
         self.monomer2,
         self.monomer3
        )
        self.check_valid_polymer(polymer)
