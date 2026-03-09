{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "196211b1-f761-4272-bc9e-40aa9a60f9db",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "usage: ipykernel_launcher.py [-h] --L L --N N\n",
      "ipykernel_launcher.py: error: the following arguments are required: --L, --N\n"
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
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/anaconda3/lib/python3.12/site-packages/IPython/core/interactiveshell.py:3585: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import argparse\n",
    "from scipy import constants\n",
    "\n",
    "def f(x):\n",
    "    if x == 0:\n",
    "        return 0\n",
    "    return x**3 / (np.exp(x) - 1)\n",
    "\n",
    "parser = argparse.ArgumentParser(\n",
    "    description=\"Computes the blackbody integral with Simpson's rule and use it to estimate the Stefan-Boltzmann constant.\"\n",
    ")\n",
    "\n",
    "parser.add_argument(\n",
    "    \"--L\",\n",
    "    type=float,\n",
    "    required=True,\n",
    "    help=\"Upper limit used to approximate infinity since simpson need a finite inteval #truncate.\"\n",
    ")\n",
    "\n",
    "parser.add_argument(\n",
    "    \"--N\",\n",
    "    type=int,\n",
    "    required=True,\n",
    "    help=\"Number of intervals for Simpson's rule (must be even).\"\n",
    ")\n",
    "\n",
    "args = parser.parse_args()\n",
    "\n",
    "L = args.L\n",
    "N = args.N\n",
    "a = 0\n",
    "b = L\n",
    "\n",
    "if N % 2 != 0:\n",
    "    raise ValueError(\"N must be even for Simpson's rule.\")\n",
    "\n",
    "h = (b - a) / N\n",
    "s = f(a) + f(b)\n",
    "\n",
    "for i in range(1, N):\n",
    "    x = a + i * h\n",
    "    if i % 2 == 1:\n",
    "        s += 4 * f(x)\n",
    "    else:\n",
    "        s += 2 * f(x)\n",
    "\n",
    "integral = (h / 3) * s\n",
    "\n",
    "sigma = (constants.k**4 / (4 * np.pi**2 * constants.c**2 * constants.hbar**3)) * integral\n",
    "\n",
    "print(\"Integral =\", integral)\n",
    "print(\"Stefan-Boltzmann constant =\", sigma)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "790d8ef6-597c-4afb-b4a4-0b41efd274e1",
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
