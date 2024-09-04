# Fast Fourier Transform (FFT) Implementation

This repository contains an implementation of the Fast Fourier Transform (FFT) algorithm, developed as part of a PhD project in the field of Digital Signal Processing (DSP). The project includes both the implementation of the FFT algorithm in Python and an example application. Additionally, a presentation is provided that covers the theoretical background and applications of the Fourier series, Fourier transform, and FFT.

## Project Structure

- **`fft_impl.py`**: This file contains the Python implementation of the FFT algorithm from scratch.
- **`fft_example.py`**: This script demonstrates how to use the FFT implementation on a synthetic sine wave signal and visualize the results.
- **`DSP - Barzegar Castello Di Giovanni.pptx`**: A PowerPoint presentation that covers the theoretical aspects of Fourier series, Fourier transforms, and FFT, including the algorithm used in this implementation.

## Getting Started

### Prerequisites

To run the example script, you'll need the following Python libraries:
- `numpy`
- `matplotlib`
- `scipy`

## Running the Example

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/fft-implementation.git
    cd fft-implementation
    ```

2. Run the example script:

    ```bash
    python fft_example.py
    ```

This will generate and plot a sine wave, apply the FFT, and plot the FFT result.

## Understanding the Implementation

- The FFT algorithm is implemented using the divide-and-conquer approach, with bit-reversal sorting and the butterfly operation for efficient computation.
- The `fft_impl.py` file contains detailed comments explaining each step of the algorithm.

## Theoretical Background

For a deeper understanding of the Fourier series, Fourier transform, and FFT, refer to the PowerPoint presentation (`DSP - Background.pdf`). It provides an overview of the mathematical concepts and the historical development of the FFT algorithm.

