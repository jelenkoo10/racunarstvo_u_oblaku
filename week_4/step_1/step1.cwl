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
      prefix: "--csv"
  targetColumn:
    type: string
    inputBinding:
      position: 2
      prefix: "--target"
  kFold:
    type: integer
    inputBinding:
      position: 3
      prefix: "--k_fold"

outputs:
  csv:
    type: File
    outputBinding:
      glob: "cleaned_dataset.csv"
