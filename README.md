# Qd20
A project for generating truly random rolls of polyhedral dice via quantum computing. An input string of the form "3d4" will be read in, and then used to generate an appropriate quantum circuit. The measured state is converted from binary to decimal, then incremented by 1. For example, state |01> becomes the decimal result 2.

The result of an example call "3d4" is calculated by creating a 4-state (2 qubit) circuit and running it three times, summing the results. For dice sizes that aren't created easily with h gates, the scripts make the smallest quantum circuit needed and reroll anything too high. So, a roll of "1d6" will generate a 8-state (3 qubit) circuit with equal probability amplitudes of all states. When measured, a decimal result greater than 6 will be discarded and the process will be rerun.

Developed on IBM Quantum. Scripts are currently designed to run on AerSimulator for instant runtime, but can easily be converted to run on proper quantum computers.

rand_dice.ipynb is the main script.

rand_dice_testing.ipynb includes framework for testing the quantum circuit, including circuit drawings and histograms.

utils.py includes useful functions for testing.

rand_dice.py is a script format of this project, with CLI enabled

bot.py controls a Discord bot which runs off of the rand_dice.py functions
