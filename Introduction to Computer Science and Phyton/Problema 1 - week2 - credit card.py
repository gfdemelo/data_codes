#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 12:24:37 2018

@author: gabriel
"""

fatura = 400
JurosAnual = 4.15
TaxadePagamentoMensal = 0.15
i = 1

while i <= 12 :  
        def jurosMensal(JurosAnual):
            MIR = JurosAnual/12.0
            return MIR   
        def pagamentoMinimoMensal(fatura, TaxadePagamentoMensal):
            MMP = TaxadePagamentoMensal*fatura
            return MMP
        def FaturaNaoPagaMensal(balance):
            MUB = fatura - pagamentoMinimoMensal(fatura, TaxadePagamentoMensal)
            return MUB
        def FaturaAtualizada():
            UBEM = FaturaNaoPagaMensal(fatura) + (jurosMensal(JurosAnual)*FaturaNaoPagaMensal(fatura))
            return UBEM
    
        print('Mês', i,  'Fatura restante: ', round(FaturaAtualizada(), 2))  
        fatura = FaturaAtualizada()
        i += 1
 


    