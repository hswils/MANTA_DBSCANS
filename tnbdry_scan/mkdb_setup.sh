module load python
source activate /global/common/software/atom/perlmutter/cesol/conda/latest


mkgrid () {
grid.py --input=$1 --nsim=$2 #grid.json
}

collect () {
collect.py --rdir0=. --rdir=SCAN --sdir=SUMMARY --input=$1 #collect.json
}

mkdb () {
makedb.py --input=$1 --output=db.dat --rdir=SUMMARY  #makedb.json
}
