cwlVersion: v1.0
class: Workflow

inputs:
  csvFile:
    type: File
    inputBinding:
      position: 1
  targetColumn:
    type: string
    inputBinding:
      position: 2
  kFold:
    type: int
    inputBinding:
      position: 3

outputs:
  performance_metrics:
    type: string

steps:
  preprocess:
    run: step1.cwl
    in:
      csvFile: csvFile
      targetColumn: targetColumn
    out:
      cleanedCsvFile: cleaned_dataset.csv

  kfold_cross_validation:
    run: step2.cwl
    scatter: [k_fold]
    scatterMethod: dotproduct
    in:
      cleanedCsvFile: preprocess.cleanedCsvFile
      targetColumn: targetColumn
      kFold: kFold
    out:
      performance_metrics: performance_metrics
