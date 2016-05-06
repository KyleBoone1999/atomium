from . import atomic
from .exceptions import *

class Monomer(atomic.Molecule):

    def __init__(self, monomer_id, monomer_name, *atoms):
        atomic.Molecule.__init__(self, *atoms, molecule_id=monomer_id, molecule_name=monomer_name)
        self.monomer_id = self.molecule_id
        self.monomer_name = self.molecule_name
        del self.__dict__["molecule_id"]
        del self.__dict__["molecule_name"]


    def __repr__(self):
        return "<Monomer (%s)>" % self.monomer_name



class MonomericStructure(atomic.AtomicStructure):

    def __init__(self, *monomers):
        if not all(isinstance(monomer, Monomer) for monomer in monomers):
            non_monomers = [monomer for monomer in monomers if not isinstance(monomer, Monomer)]
            raise TypeError("MonomericStructure needs monomers, not '%s'" % non_monomers[0])
        if not monomers:
            raise NoMonomersError("Cannot make MonomericStructure with zero monomers")
        monomer_ids = [monomer.monomer_id for monomer in monomers if monomer.monomer_id is not None]
        if len(set(monomer_ids)) < len(monomer_ids):
            raise DuplicateMonomerIdError("Cannot make MonomericStructure with duplicate monomer_ids")
        self.monomers = set(monomers)
        all_atoms = set()
        for monomer in self.monomers:
            all_atoms.update(monomer.atoms)
        atomic.AtomicStructure.__init__(self, *all_atoms)


    def __repr__(self):
        return "<MonomericStructure (%i monomers)>" % len(self.monomers)


    def __contains__(self, monomer):
        return monomer in self.monomers