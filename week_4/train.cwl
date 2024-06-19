cwlVersion: v1.0
class: Workflow

requirements:
  - class: ScatterFeatureRequirement

inputs:
  dataset_file: File
  preprocess_script: File
  learn_script: File
  folds: int[]
  n_splits: int

outputs: []

steps:
  preprocess_step:
    run: preprocess.cwl
    in:
      dataset_file: dataset_file
      script: preprocess_script
    out: [preprocessed_dataset]

  learn_step:
    run: learn.cwl
    scatter: current_fold
    scatterMethod: dotproduct
    in:
      dataset_file: preprocess_step/preprocessed_dataset
      script: learn_script
      n_splits: n_splits
      current_fold: folds
    out: []

