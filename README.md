# Construction Calculator

## Overview

The Construction Calculator is a Python application designed to assist in calculating the number of ceiling panels needed and the area of slabs for construction projects. It includes a graphical user interface (GUI) built using Tkinter.

### Features

- **Ceiling Panel Calculation**: Calculates the number of ceiling panels required based on given dimensions (width and length).
- **Slab Area Calculation**: Calculates the area of a slab, considering different specifications such as width, length, alignment direction, and the presence of supporting tracks.

### Components

- **ConstructionCalculatorEngine Class**:
  - Provides methods for ceiling panel and slab area calculations.
  - Handles different scenarios such as calculating based on dimensions and optional parameters like tracks.
- **ConstructionCalculatorApp Class**:
  - GUI interface built using Tkinter.
  - Allows users to input dimensions and preferences via a user-friendly interface.
  - Displays results for both ceiling panel and slab area calculations.

## Installation

To use the Construction Calculator, ensure you have Python installed on your system.

1. Clone the repository:
   ```
   git clone https://github.com/christianduhp/calculadora-laje-forro.git
   cd construction-calculator
   ```

## Usage

Run the application by executing the `main.py` file:

```
python main.py
```

### Interface

- **Ceiling Panel Calculation**:

  - Enter the width and length of the area to be covered.
  - Click "Calculate" to see suggested panel distributions.

- **Slab Area Calculation**:
  - Choose whether the slab has tracks or not.
  - Enter dimensions and other specifications as needed.
  - Click "Calculate" to see the calculated area or track details.

## Screenshots

![APP - CALCULADORA DE LAJES ](https://user-images.githubusercontent.com/85292359/220915506-294ea264-d7e9-4c56-b4e2-83026854aa49.png#vitrinedev)

## Dependencies

- Python 3.x
- Tkinter (included in Python standard library)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
