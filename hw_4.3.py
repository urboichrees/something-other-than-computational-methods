{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "3a00779d-0bce-49f7-933e-fff2d9c0f07e",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "usage: ipykernel_launcher.py [-h]\n",
      "ipykernel_launcher.py: error: unrecognized arguments: -f /Users/christopherosorio/Library/Jupyter/runtime/kernel-bf03dac3-30f7-439b-b04f-1104cd3d25c5.json\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "2",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[0;31mSystemExit\u001b[0m\u001b[0;31m:\u001b[0m 2\n"
     ]
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import argparse\n",
    "\n",
    "def fx(x):\n",
    "    return x * (x-1)\n",
    "\n",
    "def derivative(f,x,delta):\n",
    "    return (f(x + delta) - f(x))/delta\n",
    "\n",
    "def fprime(x):\n",
    "    return 2*x-1\n",
    "\n",
    "parser = argparse.ArgumentParser(\n",
    "    description=(\n",
    "        \"This program compares the analytic derivative of f(x)=x(x-1) to a numerical forward-difference approximation and plots the error versus delta \"\n",
    "    )\n",
    ")\n",
    "\n",
    "parser.parse_args()\n",
    "\n",
    "x = 1 \n",
    "delta = [10**-4, 10**-6, 10**-8, 10**-10, 10**-12, 10**-14]\n",
    "\n",
    "values=[]\n",
    "\n",
    "for i in delta:\n",
    "    values.append(fprime(x) - derivative(fx, x, i))\n",
    "\n",
    "plt.xlabel(\"delta values\")\n",
    "plt.ylabel(\"error values\")\n",
    "plt.title(\"delta value vs error\")\n",
    "plt.plot(delta,values)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "05b109b8-ed25-4120-859f-0b52b95ce3ec",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
