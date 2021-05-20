# https://twiki.cern.ch/twiki/bin/view/CMS/Rucio

source /cvmfs/cms.cern.ch/cmsset_default.sh
source /cvmfs/cms.cern.ch/rucio/setup-py3.sh
voms-proxy-init -voms cms -rfc -valid 192:00
export RUCIO_ACCOUNT=`whoami` # Or your CERN username if it differs
