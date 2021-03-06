#
#  2018
#

dasgoclient -query="file dataset=/ZH_HToBB_ZToBB_M125_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"

#
# 2017
#

#dasgoclient  -query="parent dataset=/ZH_HToBB_ZToBB_M125_TuneCP5_13TeV_powheg_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"
#dasgoclient  -query="parent dataset=/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"

#dasgoclient  -query="file dataset=/ZH_HToBB_ZToBB_M125_TuneCP5_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM" > ZH4b2017Files.txt
#dasgoclient  -query="file dataset=/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM"  > ZZ4b2017Files.txt


#
# 2016
#
> dasgoclient -query="parent dataset=/ZH_HToBB_ZToBB_M125_TuneCP5_13TeV_powheg_pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"
/ZH_HToBB_ZToBB_M125_TuneCP5_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM

> dasgoclient -query="parent dataset=/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"
/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM

dasgoclient  -query="file dataset=/ZH_HToBB_ZToBB_M125_TuneCP5_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM" > ZH4b2016Files.txt
dasgoclient -query="file dataset=/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM" > ZZ4b2016Files.txt


dasgoclient -query="file dataset=/GluGluToHHTo4B_node_SM_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM" > HH4b2018Files.txt

# dasgoclient -query="file dataset=/ZHHTo4B_CV_1_0_C2V_1_0_C3_0_0_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM" > 

#
# C2V == 2
#
dasgoclient -query="file dataset=/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"  > WHHTo4B_CV_1_0_C2V_2_0_C3_1_0Files.txt
dasgoclient -query="file dataset=/VBFHHTo4B_CV_1_C2V_2_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM" > VBF_HHTo4B_CV_1_C2V_2_C3_1_Files.txt

#
# SM
#
dasgoclient -query="file dataset=/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM" > WHHTo4B_CV_1_0_C2V_1_0_C3_1_0Files.txt
dasgoclient -query="file dataset=/VBFHHTo4B_CV_1_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM" > VBF_HHTo4B_CV_1_C2V_1_C3_1_Files.txt



