from pyjedai.block_building import *
from pyjedai.block_cleaning import *
from pyjedai.clustering import *
from pyjedai.matching import * 
from pyjedai.comparison_cleaning import *
from pyjedai.joins import *


methods_dict ={

    "block_building": ["StandardBlocking", "QGramsBlocking",
                       "SuffixArraysBlocking", "ExtendedSuffixArraysBlocking",
                       "ExtendedQGramsBlocking"],
    "block_cleaning": ["BlockFiltering", "BlockPurging"],
    "comparison_cleaning": [
        "ComparisonPropagation",
        "WeightedEdgePruning",
        "CardinalityEdgePruning",
        "CardinalityNodePruning",
        "ReciprocalCardinalityNodePruning",
        "WeightedNodePruning",
        "BLAST",
        "ReciprocalWeightedNodePruning"
    ],
    "entity_matching": ["EntityMatching", "VectorBasedMatching"],
    "clustering": ["ConnectedComponentsClustering", "UniqueMappingClustering",
                   "ExactClustering", 'CenterClustering',"BestMatchClustering", 
                   "MergeCenterClustering", "CorrelationClustering", "CutClustering", 
                   "MarkovClustering", "KiralyMSMApproximateClustering",
                   "RicochetSRClustering", "RowColumnClustering"],
    "join" : ["EJoin", "TopKJoin"]

}

methods_mapping = { 
    "StandardBlocking": StandardBlocking,
    "QGramsBlocking": QGramsBlocking,
    "SuffixArraysBlocking": SuffixArraysBlocking,
    "ExtendedSuffixArraysBlocking": ExtendedSuffixArraysBlocking,
    "ExtendedQGramsBlocking": ExtendedQGramsBlocking,
    "BlockFiltering": BlockFiltering, 
    "BlockPurging": BlockPurging,
    "ComparisonPropagation": ComparisonPropagation,
    "WeightedEdgePruning": WeightedEdgePruning,
    "CardinalityEdgePruning": CardinalityEdgePruning,
    "CardinalityNodePruning":  CardinalityNodePruning,
    "ReciprocalCardinalityNodePruning": ReciprocalCardinalityNodePruning,
    "WeightedNodePruning": WeightedNodePruning,
    "BLAST": BLAST,
    "ReciprocalWeightedNodePruning": ReciprocalWeightedNodePruning,
    "EntityMatching": EntityMatching,
    "VectorBasedMatching": VectorBasedMatching,
    "ConnectedComponentsClustering": ConnectedComponentsClustering,
    "UniqueMappingClustering": UniqueMappingClustering,
    "ExactClustering": ExactClustering,
    'CenterClustering': CenterClustering,
    "BestMatchClustering": BestMatchClustering,
    "MergeCenterClustering": MergeCenterClustering,
    "CorrelationClustering": CorrelationClustering,
    "CutClustering": CutClustering,
    "MarkovClustering": MarkovClustering,
    "KiralyMSMApproximateClustering": KiralyMSMApproximateClustering,
    "RicochetSRClustering": RicochetSRClustering,
    "RowColumnClustering": RowColumnClustering,
    "EJoin" : EJoin,
    "TopKJoin": TopKJoin                 
}
