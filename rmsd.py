from ccdc import io 
from ccdc.crystal import PackingSimilarity
import glob
from ase.io import read,write
from ase.visualize import view

def write_output(file1,file2,rmsd):
    with open("rsmd_matches.txt", "a+") as match:
        if rmsd == None:
            pass
        else:
            match.write(f"{file1} {file2} {rmsd} \n")

def rmsd_grab(files,i,j):
    reader = io.CrystalReader(files[i])
    atoms = reader[0]
    re = io.CrystalReader(files[j])
    compare = re[0]
    rmsd = PackingSimilarity().compare(atoms,compare)
    if rmsd.nmatched_molecules == 15:
        return rmsd.rmsd,files[i],files[j]
    else:
        return None,None,None
    
def main():
    files = glob.glob("*.cif")
    for i in range(0,len(files)):
        print(f"Remaining Crystals in Sequence: {len(files)-i}")
        for j in range(i+1,len(files)):
            rmsd,file1,file2 = rmsd_grab(files,i,j)
            write_output(file1,file2,rmsd)
    

if __name__ == "__main__":
    main()