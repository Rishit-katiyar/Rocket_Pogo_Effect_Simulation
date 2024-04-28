# Rocket Pogo Effect Simulation

Welcome to the Rocket Pogo Effect Simulation repository! 🚀

This project aims to simulate the Pogo effect, also known as Pogo oscillation or Pogo instability, observed in rockets and aerospace vehicles during powered flight. The simulation provides insights into the dynamics of the propulsion system and the structural response of the vehicle to mitigate the Pogo effect.

## Overview

The Pogo effect refers to the undesirable oscillations experienced by a rocket along its longitudinal axis during powered flight. These oscillations result from the interaction between the propulsion system dynamics and the structural dynamics of the vehicle.

## Installation

To run the simulation, follow these steps:

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/Rishit-katiyar/Rocket_Pogo_Effect_Simulation.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Rocket_Pogo_Effect_Simulation
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Once you've installed the dependencies, you can run the simulation using the provided Python script:

```bash
python rocket_simulation.py
```

The script will display a menu with options to update simulation parameters, save the animation, show the default simulation (recommended), or quit.

## Mathematical Formulation

The simulation is based on mathematical equations that describe the dynamics of the propulsion system and the structural dynamics of the vehicle. These equations include:

### Propulsion System Dynamics

The dynamics of the propulsion system are described by equations that govern the behavior of various components such as the rocket engine, fuel lines, and valves. These equations typically involve fluid dynamics, combustion processes, and mechanical vibrations.

A simplified representation of the propulsion system dynamics can be expressed using a lumped-parameter model. For example:

- **Mass flow rate equation:**

<p align="center">
    <img width="336" alt="eq00001" src="https://github.com/Rishit-katiyar/Rocket_Pogo_Effect_Simulation/assets/167756997/ebf060ae-2c7d-45b1-a0fc-6bd65a1730d9">
</p>
  
where:
  - \(\dot{m}\) is the mass flow rate,
  - \(C_d\) is the discharge coefficient,
  - \(A\) is the cross-sectional area of the nozzle,
  - \(\Delta P\) is the pressure drop across the nozzle, and
  - \(\rho\) is the density of the propellant.


- **Thrust equation:**

<p align="center">
    <img width="401" alt="eq00002" src="https://github.com/Rishit-katiyar/Rocket_Pogo_Effect_Simulation/assets/167756997/11de9160-b406-4b02-bf34-6d30bb427140">
</p>
  
where:
  - \(F\) is the thrust force,
  - \(v_e\) is the exhaust velocity,
  - \(P_e\) is the pressure at the exit of the nozzle,
  - \(P_a\) is the ambient pressure, and
  - \(A_e\) is the area of the nozzle exit.

### Vehicle Structural Dynamics

The structural dynamics of the vehicle are governed by equations of motion that describe its translational and rotational motion. These equations typically include terms related to mass, stiffness, damping, and external forces.

A simplified model of the vehicle's structural dynamics can be represented by a set of coupled second-order differential equations. For example, considering a one-degree-of-freedom model for longitudinal motion:

<p align="center">
    <img width="375" alt="eq00003" src="https://github.com/Rishit-katiyar/Rocket_Pogo_Effect_Simulation/assets/167756997/1f14d1e7-2315-4798-babe-cd8414c553c4">
</p>

where:
  - \(m\) is the mass of the vehicle,
  - \(x\) is the displacement of the vehicle,
  - \(c\) is the damping coefficient,
  - \(k\) is the stiffness coefficient,
  - \(F_{\text{ext}}\) is the external force acting on the vehicle, and
  - \(F_{\text{Pogo}}\) is the Pogo-induced force.

### Coupling Equations

To model the interaction between the propulsion system and the vehicle structure, coupling equations are used to relate the forces exerted by the propulsion system to the resulting structural displacements. These equations capture the transfer of energy and momentum between the propulsion system and the vehicle.

![rocket_animation](https://github.com/Rishit-katiyar/Rocket_Pogo_Effect_Simulation/assets/167756997/931cfb28-f2bb-47e3-ac89-4ea3cc5fd781){: width="200px"}

The coupling equations typically involve relating the thrust force generated by the propulsion system to the resulting changes in the vehicle's mass distribution and structural stiffness. These equations are often derived based on the specific configuration and dynamics of the vehicle.

## Analysis and Mitigation

The simulation allows for the analysis of Pogo-induced oscillations and the assessment of mitigation strategies. Engineers can explore modifications to the propulsion system, structural enhancements, and active control systems to minimize the Pogo effect and ensure mission safety and stability.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

---

Feel free to explore the simulation and experiment with different parameters to gain insights into the complex dynamics of the Pogo effect in aerospace vehicles! If you have any questions or suggestions, don't hesitate to reach out.
