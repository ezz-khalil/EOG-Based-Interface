# EOG Simple Game Interface
Welcome to the EOG Simple Game Interface project, an innovative human-computer interface that utilizes electrooculography (EOG) to detect eye movements and translate them into computer commands.

## Introduction
Our project leverages EOG technology to create a unique way of interacting with a computer. By detecting and interpreting eye movements, we've developed a simple game interface that allows users to play a maze game using only their eyes.

## Key Features
.EOG signal preprocessing with a Butterworth band-pass filter (0 to 30 Hz).
.Resampling of EOG data.
. Baseline and artifact removal.
. Eye movement detection, including Up, Down, Right, Left, and Blink.
. Machine learning models (SVM and Random Forest) for eye movement prediction.
. The maze game interface is controlled by predicted eye movements.
## Project Workflow
Our team followed a structured workflow to create this project:

### EOG Signal Preprocessing:

. Applied a Butterworth band-pass filter (0 to 30 Hz) to the EOG signal.
. Resampled the data for further processing.
. Removed baseline and artifacts to ensure clean input data.
### Eye Movement Detection:

Utilized Wavelet coefficients and Power Spectral Density (PSD) as features for detecting eye movements.
Trained SVM and Random Forest models to classify eye movements, including Up, Down, Right, Left, and Blink.
### Simple Game Interface:

Developed a maze game interface that allows users to navigate a maze using only their eye movements.
The objective of the game is to escape from the maze by controlling the in-game character with predicted eye movements 
