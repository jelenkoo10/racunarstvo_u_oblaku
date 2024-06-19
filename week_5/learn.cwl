cwlVersion: v1.0
class: CommandLineTool
baseCommand: python

hints:
  DockerRequirement:
    dockerPull: jupyter/scipy-notebook:latest

inputs:
  dataset_file:
    type: File
    inputBinding:
      position: 2

  script:
    type: File
    inputBinding:
      position: 1
  n_splits:
    type: int
    inputBinding:
      position: 3
  current_fold:
    type: int
    inputBinding:
      position: 4

outputs: []
