cwlVersion: v1.0
class: CommandLineTool

hints:
  DockerRequirement:
    dockerPull: jelenko10/train_evaluate_model_image

inputs:
  cleanedCsvFile:
    type: File
    inputBinding:
      position: 1

outputs:
  performance_metrics:
    type: string
