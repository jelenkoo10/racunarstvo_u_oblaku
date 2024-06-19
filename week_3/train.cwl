cwlVersion: v1.0
class: Workflow

inputs:
  dataset_file: File
  preprocess_script: File
  learn_script: File

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
    in:
      dataset_file: preprocess_step/preprocessed_dataset
      script: learn_script
    out: [] 

