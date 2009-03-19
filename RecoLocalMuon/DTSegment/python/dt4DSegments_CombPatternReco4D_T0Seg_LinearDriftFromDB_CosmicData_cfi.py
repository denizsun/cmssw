import FWCore.ParameterSet.Config as cms

# Module for 4D rechit building 
# The block of the reconstruction algo
from RecoLocalMuon.DTSegment.DTCombinatorialPatternReco4DAlgo_LinearDriftFromDB_CosmicData_cfi import *
dt4DSegments = cms.EDProducer("DTRecSegment4DProducer",
    # The reconstruction algo and its parameter set
    DTCombinatorialPatternReco4DAlgo_LinearDriftFromDB_CosmicData,
    # debuggin opt
    debug = cms.untracked.bool(False),
    # name of the rechit 1D collection in the event
    recHits1DLabel = cms.InputTag("dt1DRecHits"),
    # name of the rechit 2D collection in the event
    recHits2DLabel = cms.InputTag("dt2DSegments")
)

dt4DSegments.Reco4DAlgoConfig.performT0SegCorrection = False
dt4DSegments.Reco4DAlgoConfig.performT0_vdriftSegCorrection = False

dt4DSegments.Reco4DAlgoConfig.Reco2DAlgoConfig.performT0SegCorrection = False
dt4DSegments.Reco4DAlgoConfig.Reco2DAlgoConfig.performT0_vdriftSegCorrection = False
