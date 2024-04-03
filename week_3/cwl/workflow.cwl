cwlVersion: v1.0
class: Workflow

inputs:
  csvFile:
    type: File
    inputBinding:
      position: 1

outputs:
  performance_metrics:
    type: string

steps:
  preprocess:
    run: step1.cwl
    in:
      csvFile: csvFile
    out:
      cleanedCsvFile: cleaned_dataset.csv

  train_and_evaluate:
    run: step2.cwl
    in:
      cleanedCsvFile: preprocess.cleanedCsvFile
    out:
      performance_metrics: performance_metrics
