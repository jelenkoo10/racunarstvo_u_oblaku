cwlVersion: v1.0
class: CommandLineTool

hints:
  DockerRequirement:
    dockerPull: jelenko10/data_preprocessing_image
    
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
  csv:
    type: File
    outputBinding:
      glob: "cleaned_dataset.csv"
