#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 20:47:38 2018

@author: gabriel
"""


balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
i = 1

while i <= 12 : 
            MonthlyInterestRate = annualInterestRate/12.0
            minimumMonthlyPayment = monthlyPaymentRate*balance
            MonthlyUnpaidBalance = balance - minimumMonthlyPayment
            UpdateBalanceEachMonth = MonthlyUnpaidBalance + (MonthlyInterestRate*MonthlyUnpaidBalance)
            print('Monthly', i,  'Remaining balance: ', round(UpdateBalanceEachMonth, 2))  
            balance = UpdateBalanceEachMonth
            i += 1
            