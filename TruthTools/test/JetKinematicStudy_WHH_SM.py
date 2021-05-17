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
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/65D36BA5-B77B-3349-A6F9-A4AAF2E2B3CC.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/775E51C0-445B-7D4E-80C2-F992AEAEC263.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/8DD7342B-DC5C-B841-9E3C-8BBBAC2BE180.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/6B01FDCA-6CB1-1247-A002-D2CE39C1715F.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/458B99CF-8146-114F-A251-8DC5C00012E8.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/1B8BE37B-C969-E64E-A19B-DF5F75BFF235.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/8598C808-F1B3-9F4D-84E1-264799BF4861.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/AE3C8031-EE5A-3044-B685-1A921C4270C7.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/DE144720-E277-CA4E-8483-3D7EA6616B81.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/2CA61EC2-21B9-F243-A1B7-D38576710284.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/33B3EBB4-BD05-9947-B6AC-8EE6C692EC1F.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/B86C3005-A14B-214F-BAF1-F507139500EE.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/E2032A50-5F36-D446-99F4-7EFCCCCAC91B.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/CA5F787A-5C90-F043-A0D6-DEA235308965.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/A6D5E079-4BCF-894F-99FF-044630015C39.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/6A5BC15B-F47B-6F4F-9E2A-C706B40BD1C9.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/343A8A71-46E4-F24B-8AAF-5D13F762B500.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/C6440E25-882B-9747-911B-6BEABD3EF7A8.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/A046D614-132C-B344-B68F-0FC03CA421A0.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/EAAF01F3-910D-E74F-87FE-771A406F3DE2.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/52264F2A-D5FB-1B4B-84D5-C75E8B15FF52.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/058BF1DF-5940-8942-A546-66A3519B3DE9.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/778DDE8B-5198-314C-932E-92318DA28BE0.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/FC0C81EB-60D7-FA42-8E31-A40AC24F230B.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/08422CCE-13E4-0145-80ED-B415C63F76E0.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/807F899D-07D5-9D40-BD11-6BFC197EC301.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/BE4DB4A3-0C58-FC44-8223-CF031A1E99E5.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/F6EECD9B-AAA0-8B47-8C59-7D32D51374FA.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/72EC9E20-DFDA-884C-BFF5-96200C467A24.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/F2191026-713D-0743-9F24-19E22EDD7045.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/7E698067-E6B8-0243-871C-5BD49992219F.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/F3B0DB72-39D4-B848-AFAC-E4CF5B8FB0F7.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/34A7ED8E-98E7-EC4E-93A5-31D2221D97E1.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/116FC95B-983C-2840-BD89-53059821CE47.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/1658D652-2082-E149-AB6F-9B570725CB84.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/6FC5CEF4-2418-5C40-9B0E-FE666BAAD9E7.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/1DFA3FDD-DF5C-C640-997D-B3472274C5CB.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/227BDF53-9907-074D-92B1-DFB75EA8F32D.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/B6DB3BA6-BB92-3F44-AB79-420782D135FB.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/B34FEF77-E7F7-B14C-A598-18F25B7843D9.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/B40C2B50-9DF9-6C4D-8D9F-76126A323C68.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/E7063F3F-536A-A74A-A4C7-621F316B28E9.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/248F7528-2FC9-F24D-9364-1036B0B10610.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/A10AA31B-462A-834A-A3E4-D1FBDBBBFEF8.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/84170233-283D-4748-8954-98B169B5F542.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/5F2B6EEA-B2DD-5A40-A84D-76BAE016B851.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/6C7E0202-9D54-D34B-9283-700C51489AD7.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/0394C410-3A0E-8540-9FA4-77F19A2AF260.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/C51270C1-813E-C448-99DA-6CD807155560.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/0BD5FD7C-791C-C14B-8136-5D8045FE49C9.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/33554995-C8A2-3747-B29F-D93F67088C01.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/979396FA-3602-0246-BBC7-73711FE98E37.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/9106A42C-E915-3046-8113-28455B177FFF.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/B7C16D57-C96E-7044-9FE5-ABDB94002839.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/A7DF7482-8FE2-0C49-AF9C-CE6EBCB6B3AC.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/509AC450-994B-5D4D-803B-F0E2CB6B79C9.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/68F55BAD-B2C3-0744-BA58-8D75AF966C2A.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/F94AD2E6-AE93-DE48-9DC2-AE0A9605DA44.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/D30A737F-8E09-B74D-8EAD-37B68BB95D27.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/F777FEC1-2EC6-9042-90B4-57C2018EB94D.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/2F559C97-C49E-4440-BE67-36F58FFCDAFD.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/5905D84E-D18D-C743-AB35-454E07400FA9.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/D957DD68-5B7E-CE4E-A2CC-9CCD29883BFC.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/41A2E349-4498-7745-B7FE-4D3BFAAC4359.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/F9AE3E65-7113-F948-B81D-46876DFA89EE.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/E44BA1FD-1D45-8241-A9DD-02117D804E13.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/865DFCA6-5704-B441-B8F8-2B5FDBD0ACB6.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/8C062973-8868-734A-B344-16FD2DCAF40D.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/BABBACCD-EA64-1D49-83B7-54E14ECAD85E.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/02C2A77A-2928-D24B-AD87-FC933315F365.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/A70CF987-5FF9-044C-80A9-D48425FD0864.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/27E0D54C-8D3D-7F4B-B246-29AC75071504.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/D25421C6-C895-0542-B82D-3AF3890E260F.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/1935E724-C38F-9B4C-B607-1FF55819F92D.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/99DC19A3-8C0F-4544-A6E9-89715C5D242B.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/8CF550A8-316E-0D4E-893B-8188FC1874DD.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/85AA9922-8E6E-3144-8EF9-15916FC8F413.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/82622668-2400-3F48-BA25-2F04A7C29E99.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/324B98E0-C79F-EE48-A960-07F38E5EEA42.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/F5AB3445-C6D6-694D-B1F4-B4751A4C2A72.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/70E1AF2A-9B66-4D44-A4DD-8F07BFA6FE55.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/797DDD4A-A7F1-FE4E-80F6-01991288CE38.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/433961EC-EB2E-B448-BC0D-731B6A1ECE86.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/9298EE67-D448-4848-A0C2-01FA632CA8FB.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/7A46682B-BCBD-054D-91B6-BA7EE81690DA.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/9BB7B2FA-93D2-3D48-B125-8EEE011BE55B.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/B9A0DCA4-A6DB-3949-91A3-12FD17ABBDE9.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/C107ADE0-2049-144A-B300-19351165DC8F.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/F1D759B8-FF9E-404D-9293-EBBDB8C8026F.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/2D98EEBE-CFAE-5142-89E9-D8A02011ABCC.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/6CC1DC41-93CD-564A-8D91-7F26A61E24DD.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/D6E25E3B-1033-194A-A045-0BEF360E3549.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/43E25208-479F-7147-9047-84FEBF651CAF.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/0937EB47-4E06-3241-9F84-15730FB725BB.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/944B6EF2-6CBB-2342-88F8-D20212BB4EA8.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/FFF536B7-83ED-584A-A3F6-4546A6804DA4.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/A90B5ACF-816D-3045-955B-7B4BA189B168.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/566A39D3-184C-DE4D-A429-2FFA4B2DFCB6.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/3891BB21-9841-8646-B355-F1656DD95124.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/AB4C32FD-2447-0E40-8C7A-DB4970496E09.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/02C5DA9E-42CF-294D-8906-C1038F037D37.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/A1BF576E-8769-B442-96EA-8EFE30BB4C3C.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/5798744B-1E21-DA4D-907B-16C2902B6098.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/0A96BB1A-E1FF-2443-A169-9BF4A9482B76.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/D0C59163-963A-D147-9F2C-95175A977E83.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/F95E77A4-872E-4C4B-BA39-FB51B81A3D88.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/20BF2814-F4A1-7F42-849B-F8829FCC5582.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/BBED209B-176A-7349-9440-67F573C3F551.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/12E132DB-A206-E046-AA3C-12B9D8360543.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/E54D1157-2AF1-2945-9EBE-DCC1B593B1F8.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/38E17E3D-E429-E940-AB28-94028BEC9617.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/7546263D-5967-7C4B-9158-5CE19F3608ED.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/CD9E0DA8-8C8A-064F-8312-EB1D8325F361.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/911E81F1-0C9B-464B-A9FF-9218DE46E91A.root',
        '/store/mc/RunIIAutumn18MiniAOD/WHHTo4B_CV_1_0_C2V_1_0_C3_1_0_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/280000/E9DCE610-6BB8-3346-9B65-0207A63F480D.root',
    )
)

