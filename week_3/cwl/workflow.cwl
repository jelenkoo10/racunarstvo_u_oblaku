cwlVersion: v1.0
class: Workflow

inputs:
  csvFile:
    type: File
    inputBinding:
      position: 1
  target_column:
    type: string
    inputBinding:
      position: 2
      prefix: "--target"
  train_percentage:
    type: float
    inputBinding:
      position: 3
      prefix: "--train_percentage"

outputs:
  performance_metrics:
    type: string

steps:
  preprocess:
    run: step1.cwl
    in:
      csvFile: csvFile
      target_column: target_column
      train_percentage: train_percentage
    out:
      cleanedCsvFile: cleaned_dataset.csv

  train_and_evaluate:
    run: step2.cwl
    in:
      cleanedCsvFile: preprocess.cleanedCsvFile
    out:
      performance_metrics: performance_metrics
