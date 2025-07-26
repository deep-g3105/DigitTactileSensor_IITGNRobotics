# DigitTactileSensor_IITGNRobotics

## Overview
This is a prototype tactile sensor inspired by Meta’s DIGIT, designed to explore touch sensing using simple, affordable components. The system uses a Raspberry Pi Camera V2, RGB LEDs, and a 15A elastomer layer with printed markers to visualize and measure contact deformation.


## 🔧 Hardware Summary
Component	Description
Camera	Raspberry Pi Camera V2
Illumination	1 Red, 1 Green, 1 Blue LED
Case	3D printed body with acrylic front window
Sensing Surface	15 Shore A elastomer with printed markers

## 🎯 Goals
Vision-based deformation tracking

Marker displacement analysis

Normal & shear force estimation (basic model)

Modular and open for experimentation

## 🚧 Current Status
This is an early-stage prototype for research and learning purposes. Force estimation is currently being explored using simple geometric displacement models.

## 🧰 Hardware Design
All CAD and manufacturing files needed to build the sensor are included in this repository. The design focuses on simplicity, modularity, and ease of 3D printing.

### 📁 Folder Overview:

| Folder                                    | Description                                                           |
| ----------------------------------------- | --------------------------------------------------------------------- |
| `Hardware_Prototype/Casing/`              | Main 3D model of the sensor body and housing (SolidWorks + STL)       |
| `Hardware_Prototype/acrylic_piece/`       | Cutout design for the transparent top layer (acrylic faceplate)       |
| `Hardware_Prototype/gel_moulds/`          | Moulds used for casting the elastomer layer (15 Shore A silicone)     |
| `Hardware_Prototype/Demo/`                | Video representing Hardware Demo of prototype                         |    


## 📚 Citation
This project is inspired by the DIGIT and DIGIT 360 tactile sensors by Meta AI. If you use this work or build upon it, please consider citing the following:

📝 DIGIT
DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Applications to In-Hand Manipulation
Mike Lambeta, Po-Wei Chou, Stephen Tian, Brian Yang, Benjamin Maloon, Marco Pavone, Ronald Fearing, Roberto Calandra
Published in IEEE Robotics and Automation Letters (RA-L), 2020
[IEEE]

<details> <summary>BibTeX</summary>
bibtex
Copy
Edit
@Article{Lambeta2020DIGIT,
  author  = {Lambeta, Mike and Chou, Po-Wei and Tian, Stephen and Yang, Brian and Maloon, Benjamin and Pavone, Marco and Fearing, Ronald S. and Calandra, Roberto},
  title   = {{DIGIT}: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Applications to In-Hand Manipulation},
  journal = {IEEE Robotics and Automation Letters (RA-L)},
  year    = {2020},
  volume  = {5},
  number  = {3},
  pages   = {3838--3845},
  doi     = {10.1109/LRA.2020.2977257}
}
</details> 
