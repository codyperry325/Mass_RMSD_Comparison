# Mass_RMSD_Comparison
A program to check the RMSD of predicted crystal structures against each other or experimentally determined structures. 

NOTE: This will iterate over all cif files in a forward fashion:

```
file1.cif vs file2.cif --- file(n).cif
file2.cif vs file3.cif --- file(n).cif
file(n-1).cif vs filen.cif
```

Remaining crystals value reports the crystal it is currently comparing against the rest. If there are alof of cif files in the folder, this process could take a long time to iterate through but should not need any monitoring! 

To ensure compatibility, verions of ASE and CCDC are:
```
python = 3.11.5
ase = 3.23.0
csd-python-api = 3.3.0
```

To create an environment ready for this code use:

```
conda create -n csdpy
conda install --channel=https://conda.ccdc.cam.ac.uk csd-python-api
conda install -c conda-forge ase
```

You must have a CCDC license to use this code, if you have already installed the library it should not be a problem. 

To run the program optimally, ensure rmsd.py is in the folder with the cif file:
```
conda activate csdpy
python3 rmsd.py
```

Please enjoy and report any bugs found. I cannot gauruntee it will work with future version of python, ase or the csd api! :) 
