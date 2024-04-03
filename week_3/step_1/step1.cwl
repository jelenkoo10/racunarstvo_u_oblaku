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

outputs:
  csv:
    type: File
    outputBinding:
      glob: "cleaned_dataset.csv"
