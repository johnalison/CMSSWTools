from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('analysis')

options.parseArguments()

from CMSSWTools.TruthTools.JetKinematicStudyBase import process, cms

nTruthBosons = 3


members = [attr for attr in dir(process) if not callable(getattr(process, attr)) and not attr.startswith("__")]

for m in members:
    if hasattr(getattr(process,m),"nTruthBosons" ):
        setattr(getattr(process,m),"nTruthBosons",cms.uint32(nTruthBosons))


process.TFileService = cms.Service("TFileService", fileName = cms.string (options.outputFile))



# set the number of events
process.maxEvents = cms.untracked.PSet(
    #input = cms.untracked.int32(100000)
    input = cms.untracked.int32 (options.maxEvents)
)



process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/366FE880-FFCB-D240-91B6-C976FD8A88D9.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/1C98E10B-C129-F14F-8E25-4246EDA66079.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/B400B5F1-74BB-2648-AA96-349D2BC1956D.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/5B876D26-79EC-D447-97A7-1BBE57FD5B91.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/3E99D8B1-F02B-AE49-A209-002A1177DF10.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/27EA6E86-63E4-AA43-BDAA-1EFF176E3628.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/292E908D-2A76-D044-BAD5-A31D86E99D0A.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/23C7811A-FD25-7F4D-8FA2-7206EE30551B.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/1580BDCB-8B55-1948-B045-2359F0953651.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/DCCB056E-57DA-D04A-9CB9-EC691C1FDBD8.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/11FBFDAC-C728-5E46-B970-96F29EEFB9B7.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/D9F49BA9-44CD-D343-9087-42C999480098.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/24E21143-1856-754A-8D5A-542217306AA0.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/94943EC7-05BC-4547-80BC-B15BE03881E7.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/0B81A779-799D-F248-B6E8-E790C435C0A1.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/7EA7B60F-14BE-0F49-944C-9CB42C9908CD.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/7FCB470E-80C1-2747-8F81-397F604B867E.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/F86B2421-4448-3F47-AFEC-A74819D3CC9B.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/72B1CB2E-3F00-E444-AC14-8C9541291540.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/26A9E6F2-8000-7348-80FA-AE07A2646FF4.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/1BB8C286-7EA8-2640-88CC-73A50260CC08.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/CE9791F1-2D66-F747-BD32-E30F5E1085DA.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/E9388DAA-2AE1-A040-A45F-273A20ABD390.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/B5D6B786-4DD4-E14E-BE1A-E50AB7EAA363.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/08066BAA-F4A1-DB48-973E-065625F768DB.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/6FBB3407-A73F-3947-8C6A-4E1D357E1B8F.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/1BF4AC00-3C55-6545-9EC5-41BC49121FFF.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/07141DFD-FBCF-0C4C-880A-9DFBC4770197.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/3340FEE2-46AC-104B-9A30-E772E4759DF9.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/2959A51C-B0AB-F14F-8E46-D4E1B2323DFC.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/9A85F8E1-2093-274C-A7D8-89F3EEEB99BB.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/F0080153-AC8F-9046-883A-652F9759CE0E.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/28343992-4151-4D40-BD52-AFC58DBBDBC2.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/B9299B70-618C-F747-8554-2468BBB3BB80.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/4FFF7453-FDC5-364B-86E0-1A3EE23613A0.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/9B826F06-D0A6-EC42-A165-B99F14EA84BE.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/B722FA9B-CBC7-DF4B-A3C7-CA3A0CD124BC.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/CC4B31CE-6BA6-AD41-B97E-523F579C2857.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/6F94221A-AFB1-5B41-A770-F34B1C06840C.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/CD97F305-914C-6341-90FC-D801276FF76E.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/7A0A5ABC-A10A-8644-A8A1-369FA506F14D.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/DFD375BF-AF8F-524E-ADF2-C38C3D8EE65F.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/D4EFF1DC-1BE8-C042-A047-C215C499EDF9.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/F3F5A295-7742-174B-AF9B-AA141B71398B.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/41F08ADD-4EE4-C746-8A26-91516ECC4F97.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/789A3E7A-8E06-5141-B024-3838C4B2087F.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/C774979F-1161-8946-96DC-F224EBA708DB.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/04F311C7-DA88-A14B-9AC9-377F96CA358F.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/5DD258A0-0E97-6845-8DCC-72B5B3BC76F6.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/EEC60624-BCFC-B24E-ACB2-67EB9C2465A1.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/4C118AA4-16F5-0D4F-B5AF-405DBEB1B7F1.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/B1C6396D-2606-5E43-8DBA-91A367F6CBDC.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/4BF5FE1A-39AA-2E41-818C-396EE4553A2C.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/0AB6E054-1EF4-BD46-B064-45CC37E7F079.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/DE21E0AB-4A70-2941-B33E-9D0A7C8A6869.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/13A42F55-1E9E-ED4A-8C38-AAEA9F2DFD9E.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/BB5384EA-50C8-6947-B727-6BE7ADC8EB24.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/A6268C05-8EBC-4F42-8A50-C395DEC86E2C.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/2E189680-8D98-084E-B1F9-48334E39F693.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/D28999DF-5688-D54A-B7A7-D9BA2FC8A388.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/21F73E34-5213-FE44-8F47-5E14213ECD97.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/547E19A8-28AF-E249-9E3F-D4E7714A3596.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/C15652A2-ED70-514D-BBDF-B23F976AC7F6.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/8BA7BEE0-DB06-4449-B437-D8004A20BBCB.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/2956ABE7-CAFD-1E48-B762-86574DE204DE.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/88242067-2958-6F44-9EB8-54C9025F00A9.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/9E50AC8F-CCF9-594C-8664-756C52B58D1C.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/B77F49A2-5690-E245-8488-78A42D0ACE50.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/C85C2B41-A19B-724A-AE92-69E7B8E780C8.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/38BED505-3E9F-F047-B763-0BD748C5AD50.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/28F8F8DC-40B1-0C48-BD14-A91CF8495FAB.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/7A2012FE-C45B-9149-B9F1-0CFACDCE6D72.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/C0B97B64-84BF-E245-8218-0D788A2C015A.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/E9FFEDF2-5AE4-3147-99F7-EAC069BC89A9.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/C2C07C11-BDF2-1446-8E8D-C63BE4A708E3.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/94AC6D0A-23D5-DB42-B330-65476C7E0C14.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/6E43F263-8A1C-C647-A5E7-4157700F6EF4.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/5D1EA6E5-24FD-2D47-ADF4-CA477352713A.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/8FCD3304-8190-B147-AEA1-E8BCEFFD827D.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/B2E02F67-84FD-654B-871D-C7C1193B638F.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/41DBCE21-ACE8-914D-BA03-53A77D9375BB.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/69948CED-6D8C-EF4C-8620-D4FDCC791E11.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/A091E1F8-68DD-C84F-8585-03826520B97E.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/07493C70-BD3E-794A-9CFA-97EE307CCBFF.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/A538D069-3B37-0847-8C7B-BDA91C317779.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/66EC3AE7-7F2E-EE4F-86A8-E608A70A9B3D.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/D8AF3262-4263-2340-863E-63A3BA085407.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/54CF42AC-101D-0F45-98FE-F04002088E05.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/85465522-5FA0-8E43-9127-10F162B6DF86.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/02E54543-CCC8-9A42-8C69-C6C60CF10D2E.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/F57D4CC0-4A99-4844-80C6-107EEBD42883.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/41A1E6A5-54C0-194A-BB2C-F0232845732E.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/5310344E-2ECB-C34A-89A9-4EEBAD59FC1C.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/EA0A6EF9-0F75-3843-85B9-953E07B7B132.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/84A430FB-4874-8541-95A4-31A50BC7F961.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/1F0FD372-6E8F-2B4F-8F43-540FD427F997.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/A1419295-9F7A-E441-AAAC-4773C6707490.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/9C887E46-6C3D-4745-B9E2-888EE5B32139.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/98E1FC3A-8606-184F-8402-2E07DF91E99B.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/4E9C2D6A-CBD1-224A-9D8A-A7FADBACA698.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/C24C90CA-858C-A747-96C5-5FEC5030AB8A.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/E63E5032-2ED4-5241-9378-CF5AB3A34C4E.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/FAA838E3-B2C4-2442-9FAD-2CF5461422EC.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/1C0A3B09-3831-8542-A91F-28CCCA3C34C9.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/C2C482CD-2AE3-9C4F-8566-603C0785AB89.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/F2533BFD-AB14-E44A-9323-9FD4D322213E.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/977E6BD3-C0C4-D749-92F1-B76924CAF8B1.root",
        "/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_2_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/161C24DE-0533-2347-BC50-2ECCE5BF9E36.root",
    )
)

