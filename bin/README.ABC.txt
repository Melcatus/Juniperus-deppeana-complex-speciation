# ABCtoolbox: Calibration, Sampling, and Estimation Procedures

# This document provides a description of the processes involved in **Calibration**, **Sampling**, and **Estimation** using **ABCtoolbox**. The sections below explain the workflow, required inputs, expected outputs, and key parameters for each step.

## Calibration  
# In this stage, simulation parameters are tuned to ensure that summary statistics generated from 
# simulated datasets are comparable to those observed. Proper calibration improves the accuracy and  efficiency of the subsequent steps.

./ABCsampler depp_completo_cal.input 

# Input also contains pathways to observed statistics, model templates and the fastsimcoal2 executable 

# Sampler is set to 10,000 simulations.
# Check that observed values are within the range of simulated data. 

 Rscript ajuste.R
 
 ./ABCsampler depp_completo.input 
 echo "Muestreo MCMC terminado, 100,000 simulaciones realizadas!"
  Rscript ajuste_2.R
  echo "Ajuste de MCMC graficado"
    cp  MCMC_depp_sampling1.txt depp_completo.obs ./Estimacion
    cd Estimacion
    ./ABCestimator MCMC_depp_estimacion.input > salida_3.txt
    echo "Estimacion posterior realizada"
    R --vanilla MCMC_depp_estimation.input < plotPosteriorsGLM.r 
    echo "Proceso terminado, distribuciones posteriores dibujadas"
scp -r ./../Estimacion alejandra@132.247.213.242:/home/alejandra/rodrigo/

## Sampling  
# This process involves generating a large number of simulations based on prior distributions and calibrated parameters. The goal is to produce a representative set of synthetic datasets for comparison with the observed data.

./ABCsampler depp_completo.input 

## Estimation  

# Using the simulated datasets and observed summary statistics, ABCtoolbox applies approximate Bayesian computation methods to estimate posterior distributions of the parameters of interest.

./ABCestimator MCMC_depp_estimacion.input > salida_3.txt

---
R --vanilla MCMC_depp_estimation.input < plotPosteriorsGLM.r

# To plot approximated posteriors and adjust parameters given the case. 

**Note:**  
Each section in this document includes command-line examples, parameter settings, and file structures needed to replicate the analyses.
