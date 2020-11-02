
import click

from ase import Atoms
from ase.io import read
import numpy as np

from lammps_tools.analyze_structure import guess_bonds

@click.command()
@click.argument('cifpath', type=click.Path())
def analyze_bonds_in_file(cifpath):
    atoms = read(cifpath)
    cell_lengths = [21.84996, 21.7404, 6.54892*2]
    cell_angles = [90.03271, 90.02859, 60.17352]
    bond_dict = {'Ni-O':1.9, 'C-O':1.75, 'C-C':1.75, 'C-H':1.3, 'H-O':1.3, 'O-O':0.0, 'default':1.5}

    mol_ids_new = np.ones(len(atoms))

    all_bonds, all_bond_types, all_bond_lengths, all_bonds_across_boundary, bonds_by_mol = guess_bonds(atoms, mol_ids_new, cell_lengths, cell_angles, degrees=True, fractional_in=True, cutoff=bond_dict, periodic='xy')
    print(all_bonds)


if __name__ == '__main__':
    analyze_bonds_in_file()
