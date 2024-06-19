FROM jupyter/scipy-notebook:latest

FROM quay.io/commonwl/cwltool:latest

WORKDIR /workflow

COPY train.cwl /workflow/train.cwl
COPY input.yml /workflow/input.yml