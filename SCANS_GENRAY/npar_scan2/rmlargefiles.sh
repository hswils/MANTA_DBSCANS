rm -rf run.log*
rm -rf dakota*
rm -rf params.in.*
cp *.ipynb /pscratch/sd/h/hswils/github_repos/MANTA_DBSCANS/ANALYSIS_SCRIPTS/
rm *.ipynb
rm -rf .ipynb_checkpoints
rm -rf summary
rm -rf SCAN/simulation_*.conf
rm -rf SCAN/work/DAKOTA_BRIDGE*
rm -rf FWK_COMP*
rm -rf SCAN/simulation_*/simulation_*
rm -rf SCAN/simulation_*/work/fastran_driver*
rm -rf SCAN/simulation_*/work/fastran_lh_genray_*/xgenray.log
rm -rf SCAN/simulation_*/work/fastran_lh_genray_*/plot.ps
rm -rf SCAN/simulation_*/work/plasma_state

