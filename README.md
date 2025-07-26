# DigitTactileSensor_IITGNRobotics

## Overview
This is a prototype tactile sensor inspired by Meta’s DIGIT, designed to explore touch sensing using simple, affordable components. The system uses a Raspberry Pi Camera V2, RGB LEDs, and a 15A elastomer layer with printed markers to visualize and measure contact deformation.

The goal is to perform normal and shear force estimation by tracking marker displacements during physical interactions.

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

| Folder           | Description                                                           |
| ---------------- | --------------------------------------------------------------------- |
| `Casing/`        | Main 3D model of the sensor body and housing (SolidWorks + STL)       |
| `acrylic_piece/` | Cutout design for the transparent top layer (acrylic faceplate)       |
| `gel_moulds/`    | Moulds used for casting the elastomer layer (15 Shore A silicone)     |
| `Demo/`          | Video representing Hardware Demo of prototype                         |     
