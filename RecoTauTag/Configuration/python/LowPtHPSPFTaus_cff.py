import FWCore.ParameterSet.Config as cms
import copy


'''
Sequences for reconstructing LowPt taus using the HPS algorithm

'''

import CommonTools.ParticleFlow.pfNoPileUp_cff as LowPtTaus
pfPileUpForLowPtTaus = LowPtTaus.pfPileUp.clone(
    PFCandidates = cms.InputTag('particleFlow'),
    checkClosestZVertex = cms.bool(False)
)
pfNoPileUpForLowPtTaus = LowPtTaus.pfNoPileUp.clone(
    topCollection = cms.InputTag('pfPileUpForLowPtTaus'),
    bottomCollection = cms.InputTag('particleFlow')
)


import RecoJets.JetProducers.ak4PFJets_cfi as LowPtTaus2

# reclustering ak8 
betapar = cms.double(0.0)
fatjet_ptmin = 1.0


LowPtTauSeeds = LowPtTaus2.ak4PFJets.clone(     
    doAreaFastjet = cms.bool(True),
    rParam = cms.double(0.8),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin =  cms.double(fatjet_ptmin),   
)


from Configuration.Eras.Modifier_pp_on_XeXe_2017_cff import pp_on_XeXe_2017
pp_on_XeXe_2017.toModify(LowPtTauSeeds, inputEtMin = 999999.0)

LowPtHPSPFTausTask = cms.Task(
    pfPileUpForLowPtTaus,
    pfNoPileUpForLowPtTaus,
    LowPtTauSeeds
)

