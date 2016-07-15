# OCIMP
Algorithms &amp; Simulations for Online Contextual Influence Maximization Problem (OCIMP)

This repository hosts our implementations of state-of-the-art algorithms for OCIMP. This is a Python 3 codebase and only depends on NumPy in run-time and Cython for linking C++ implementations to Python.

You are free to use these codes for any purpose. The raw results and plots provided in Misc folder are from our work and are only for inspection. Feel free to report problems, suggest improvements. Third-party contributions are more than welcome. If you intend to use these implementations, COIN, COIN+ or PureExploitation algorithms, please cite our paper. (Citation will be added upon acceptance)

We use TIM+ as the offline influence maximization solver for the online algorithms and require the user to cythonize and compile the C++ source of TIM+ according to their own architecture. To do so,

    python ./TIM+/Tim/setup.py build_ext --inplace
    python ./TIM+/UnderTim/setup.py build_ext --inplace

Then, replace the pytim.* and undertim.* files in each of the algorithm's folders. These are the compilations based on the author's computer. Notice that, the graph files and these C++ shared object files are copied in each of the folder independently. This prevents the racing conditions and makes it possible to run multiple algorithms simultaneously without any segmentation fault.

Each algorithm has a class implementation that implements a base class. To run an algorithm, you can simply use *_script.py files and don't need to change the implementations. The tunable parameters for a simulation are explicitly declared in these scripts and can easily be changed.
