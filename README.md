# Structured-Light-Camera
The Structured Light Camera will scan objects and output the 3D model as a CAD compatible file. The system will use an integrated circuit and be a compact device with modular design. This repository will house the code that will operate the system on the frontend.

To set up the dependencies, a Python environment must be set up. The easiest way to do this is to set up a venv (NOTE: Python must be installed on the machine). The command line to do this is:
```python -m venv slcenv```


To start the web application, use the following command in the directory that houses the slc-flask and slcapp folders.
```powershell
python -m flask --app slcapp run --debug
```
