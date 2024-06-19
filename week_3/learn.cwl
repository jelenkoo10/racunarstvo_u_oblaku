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

arguments:
  - position: 3
    valueFrom: $(inputs.dataset_file.path)

outputs: []
